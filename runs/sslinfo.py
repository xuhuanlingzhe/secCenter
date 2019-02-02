# encoding=utf-8
import requests,json,socket,MySQLdb,time
from OpenSSL.SSL import Connection, Context, TLSv1_METHOD

class sslinfo():
    def __init__(self):
        self.conn=None
        self.__init_db()

    def __init_db(self):
        db = MySQLdb.connect(host='127.0.0.1', port=3306, user='sec_db_w', passwd='123456', db='sec_db',
                             charset='utf8')
        db.autocommit(1)
        self.conn = db.cursor()

    def __InsertDomainData(self,domain_str,email,end_time):
        try:
            self.conn.ping()
        except:
            self.__init_db()
        sql = "insert into asset_domains(name,reg_email,etime) values(%s,%s,%s)"
        end_time=end_time.replace(u'年','-').replace(u'月','-').replace(u'日','')
        val = (domain_str,email,end_time)
        try:
            ret = self.conn.execute(sql, val)
        except Exception,e:
            self.__init_db()
            ret = self.conn.execute(sql, val)
        return ret

    def __get_domain_info(self,domain_name):
        url = 'https://cloud.baidu.com/api/bcd/whois/detail'
        headers = {
            'Host': 'cloud.baidu.com',
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept - Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'X - Requested - With': 'XMLHttpRequest',
            'Referer': 'https: // cloud.baidu.com / product / bcd / whois.html?domain = '+domain_name
        }
        params = {
            'domain': domain_name,
            'type': 'NORMAL'
        }
	n=0
        while True:
	    if n>3:
		return
            resp = requests.post(url, data=json.dumps(params), headers=headers)
            print domain_name
            data = json.loads(resp.text)
            if len(data)>2:
                break
            time.sleep(1000)
	    n=n+1
	try:
            data=data['result']['data']
	except:
	    return
        try:
            reg_email=data['registrantEmail']
        except:
            reg_email=''

        self.__InsertDomainData(data['domain'],reg_email,data['expirationDate'])
        return

    def __InsertData(self,domain_str,ip,state,ctime,ssl_info,ssl_etime):
        try:
            self.conn.ping()
        except:
            self.__init_db()
        """if len(ssl_etime)>2:
            ssl_etime1=ssl_etime[0:4]+'-'+ssl_etime[4:6]+'-'+ssl_etime[6:8]+' '+ssl_etime[8:10]+':'+ssl_etime[10:12]+':'+ssl_etime[12:14]
        else:
            ssl_etime1=''"""
        sql = "insert into asset_sslinfo(domain,ip,state,ctime,ssl_info,ssl_etime) values(%s,%s,%s,%s,%s,%s)" #('%s','%s',%s,'%s','%s','%s')"%(domain_str,ip,state,ctime,ssl_info,ssl_etime1)
        val = (domain_str,ip,state,ctime,ssl_info,ssl_etime)
        try:
            ret = self.conn.execute(sql, val)
            #ret = self.conn.execute(sql)
        except Exception,e:
            self.__init_db()
            ret = self.conn.execute(sql, val)
        return ret

    def __test_domain_conn(self, domain_str):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        try:
            s.connect((domain_str, 443))
            s.settimeout(None)
        except:
            result = 0
        else:
            result = 1
        s.close()
        return result

    def __get_CN(self, data):
        for item in data:
            if item[0] == 'CN':
                return item[1]
        return ''

    def __read_cert(self, domain_str):
        sslcontext = Context(TLSv1_METHOD)
        sslcontext.set_timeout(30)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print domain_str
        try:
            s.connect((domain_str, 443))
        except Exception,e:
            print e
            return ''
        try:
            c = Connection(sslcontext, s)
            c.set_tlsext_host_name(str(domain_str))
            c.set_connect_state()
            c.do_handshake()
            cert = c.get_peer_certificate()
            issuer = cert.get_issuer().get_components()
            result = self.__get_CN(issuer),self.__get_CN(cert.get_subject().get_components()),cert.get_notAfter()
            c.shutdown()
        except Exception,e:
            print e
            return ''
        s.close()
        return result

    def __get_ssl_info(self, domain_str):
        if self.__test_domain_conn(domain_str) > 0:
            x = self.__read_cert(str(domain_str))
            return x
        else:
            return ""

    def __get_subdomain_list(self, domain_id):
        url = 'https://dnsapi.cn/Record.List'
        headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
            'Accept': 'text / html, application / xhtml + xml,application / xml;',
            'Accept - Encoding': 'gzip, deflate',
        }
        params = {
            'login_token': '64611,9999999995c2cac5ff4c067777777777',
            'format': 'json',
            'type': 'all',
            'domain_id': domain_id
        }
        resp = requests.post(url, data=params)
	#print resp.text
        data = json.loads(resp.text)
        root_domain = data['domain']['name']
        buff = []
        for item in data['records']:
            if item['name'] == '@': continue
            domain_str=item['name'] + '.' + root_domain
            if int(item['enabled'])==0:
                state_str=False
                ssl_info_str=''
                self.__InsertData(domain_str, item['value'], state_str, item['updated_on'], ssl_info_str, '')
            else:
                state_str=True
                if item['name']=='*':
                    tmp=self.__get_ssl_info(root_domain)
                    if len(tmp)==0:
                        ssl_info_str=''
                        ssl_etime=''
                    else:
                        ssl_etime=tmp[2]
                        ssl_etime = ssl_etime[0:4] + '-' + ssl_etime[4:6] + '-' + ssl_etime[6:8] + ' ' + ssl_etime[8:10] + ':' + ssl_etime[10:12] + ':' + ssl_etime[12:14]
                        ssl_info_str = tmp[0]+'|'+tmp[1]+'|'+ssl_etime
                else:
                    tmp=self.__get_ssl_info(domain_str)
                    if len(tmp) == 0:
                        ssl_info_str = ''
                        ssl_etime = ''
                    else:
                        ssl_etime = tmp[2]
                        ssl_etime = ssl_etime[0:4] + '-' + ssl_etime[4:6] + '-' + ssl_etime[6:8] + ' ' + ssl_etime[8:10] + ':' + ssl_etime[10:12] + ':' + ssl_etime[12:14]
                        ssl_info_str = tmp[0] + '|' + tmp[1] + '|' + ssl_etime
                self.__InsertData(domain_str,item['value'],state_str,item['updated_on'],ssl_info_str,ssl_etime)

    def get_domain_json(self):
        url = 'https://dnsapi.cn/Domain.List'
        headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
            'Accept': 'text / html, application / xhtml + xml,application / xml;',
            'Accept - Encoding': 'gzip, deflate',
        }
        params = {
            'login_token': '64611,9999999995c2cac5ff4c067777777777',
            'format': 'json'
        }
        resp = requests.post(url, data=params)
        text = resp.text
        data = json.loads(text)
        try:
            self.conn.execute('truncate table asset_sslinfo')
            self.conn.execute('truncate table asset_domains')
        except:
            self.conn.execute('truncate table asset_sslinfo')
            self.conn.execute('truncate table asset_domains')
        for item in data['domains']:
            id=item['id']
            self.__get_subdomain_list(id)
            root_domain=item['name']
            self.__get_domain_info(root_domain)
        return 1
