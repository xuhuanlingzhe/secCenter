# encoding=utf-8
import redis,MySQLdb,os,json,sys

class sec_redis():
    def __init__(self):
        self.obj_redis=redis.Redis('10.16.192.13',port=6379,db=0)
        self.obj_secdb_cur=self.__init_secdb()
        self.obj_relay_cur=self.__init_relaydb()

    def __init_secdb(self):
        db = MySQLdb.connect(host='g1-sec-ku-m.dns.fuck.com', port=3410, user='sec_db_w', passwd='123456',
                             db='sec_db',
                             charset='utf8')
        db.autocommit(1)
        return db.cursor()

    def __init_relaydb(self):
        #db = MySQLdb.connect(host='10.16.208.9', port=443, user='relay_admin', passwd='Relay@2015',db='relay',charset='utf8')
        db = MySQLdb.connect(host='10.16.17.109', port=3409, user='relay_admin', passwd='Relay@2015',db='relay',charset='utf8')
        db.autocommit(1)
        return db.cursor()

    def cache_relay_ldap_users_count(self,type=0):
        p = os.popen(
            'bash -c \'ldapsearch -x -D "cn=Admin,dc=fuck,dc=com" -h ldap-s1.dns.fuck.com -w 123456 -b "dc=fuck,dc=com"|grep uidNumber|wc -l\'')
        x = p.read()
        p.close()
        if type==0:
            self.obj_redis.set('relay_ldap_users_count',x)
            print sys._getframe().f_code.co_name
        else:
            return x

    def cache_relay_hosts_count(self,type=0):
        sql = "select count(id) from asset_hosts"
        self.obj_secdb_cur.execute(sql)
        x = self.obj_secdb_cur.fetchall()[0][0]
        if type==0:
            self.obj_redis.set('relay_hosts_count', x)
            print sys._getframe().f_code.co_name
        else:
            return x

    def cache_relay_online_users_count(self):
        p = os.popen('bash -c \'ansible 10.16.11.119 -m shell -a "/usr/bin/who | wc -l"\'')
        x = p.read()
        x=x[x.rindex(">")+2:]
        p.close()
        self.obj_redis.set('relay_onlie_users_count', x)
        print sys._getframe().f_code.co_name

    def cache_relay_conn_hosts_count(self):
        p = os.popen('bash -c \'ansible 10.16.11.119 -m shell -a \'who | awk \'{print $6}\' | uniq -c | wc -l\'\'')
        x = p.read()
        p.close()
        self.obj_redis.set('relay_conn_hosts_count', x)
        print sys._getframe().f_code.co_name

    def cache_relay_month_linechart(self):
        sql='SELECT COUNT(DISTINCT sessionid) AS a,COUNT(DISTINCT ldap_user) AS b,COUNT(DISTINCT server_ip) AS c,DATE(cur_time) AS e FROM inlog WHERE DATE_SUB(CURDATE(), INTERVAL 1 MONTH) <= DATE(cur_time) GROUP BY DAY(cur_time) order by cur_time ASC'
        self.obj_relay_cur.execute(sql)
        data = self.obj_relay_cur.fetchall()
        buf = []
        for item in data:
            tmp = {}
            tmp['luc'] = item[0]
            tmp['ouc'] = item[1]
            tmp['lhc'] = item[2]
            tmp['date'] = item[3].strftime('%Y-%m-%d')
            buf.append(tmp)
        data = json.dumps(buf)
        self.obj_redis.set('relay_month_linechart_data', data)
        print sys._getframe().f_code.co_name

    def cache_relay_month_onlie_users(self):
        ldap_users_count = self.cache_relay_ldap_users_count(1)
        sql = 'SELECT COUNT(DISTINCT ldap_user) AS a FROM inlog WHERE DATE_SUB(CURDATE(), INTERVAL 1 MONTH) <= DATE(cur_time)'
        self.obj_relay_cur.execute(sql)
        online_users = self.obj_relay_cur.fetchall()[0][0]
        data = []
        tmp = {}
        tmp['value'] = int(ldap_users_count) - online_users
        tmp['name'] = '月未活跃用户'
        data.append(tmp)
        tmp = {}
        tmp['value'] = online_users
        tmp['name'] = '月活跃用户'
        data.append(tmp)
        data = json.dumps(data)
        self.obj_redis.set('relay_month_onlie_users_data', data)
        print sys._getframe().f_code.co_name

    def cache_relay_month_onlie_hosts(self):
        host_count = self.cache_relay_hosts_count(1)
        sql='SELECT COUNT(DISTINCT server_ip) AS b FROM inlog WHERE DATE_SUB(CURDATE(), INTERVAL 1 MONTH) <= DATE(cur_time)'
        self.obj_relay_cur.execute(sql)
        online_host = self.obj_relay_cur.fetchall()[0][0]
        data = []
        tmp = {}
        tmp['value'] = host_count - online_host
        tmp['name'] = '月未登录主机'
        data.append(tmp)
        tmp = {}
        tmp['value'] = online_host
        tmp['name'] = '月登录主机'
        data.append(tmp)
        data = json.dumps(data)
        self.obj_redis.set('relay_month_onlie_hosts_data', data)
        print sys._getframe().f_code.co_name

    def cache_relay_top_login_hosts(self):
        sql='SELECT COUNT(id) AS a,server_ip AS b FROM inlog as tb1 WHERE isLogin=1 AND DATE_SUB(CURDATE(), INTERVAL 1 WEEK) <= DATE(cur_time) GROUP BY server_ip ORDER BY a DESC LIMIT 10'
        self.obj_relay_cur.execute(sql)
        rows=self.obj_relay_cur.fetchall()
        data=[]
        for item in rows:
            tmp = {}
            tmp['sum']=item[0]
            tmp['ip']=item[1]
            sql='select ldap_user,cur_time from inlog where isLogin=1 and server_ip=\''+item[1]+'\' order by cur_time DESC limit 1'
            self.obj_relay_cur.execute(sql)
            row = self.obj_relay_cur.fetchall()
            tmp['user']=row[0][0]
            tmp['ltime']=row[0][1].strftime('%Y-%m-%d %H:%M:%S')
            data.append(tmp)
        data = json.dumps(data)
        self.obj_redis.set('relay_top_login_hosts_data', data)
        print sys._getframe().f_code.co_name

    def cache_relay_top_login_users(self):
        sql='SELECT COUNT(id) AS a,ldap_user AS b FROM inlog WHERE isLogin=1 AND DATE_SUB(CURDATE(), INTERVAL 1 WEEK) <= DATE(cur_time) GROUP BY ldap_user ORDER BY a DESC LIMIT 10'
        self.obj_relay_cur.execute(sql)
        rows=self.obj_relay_cur.fetchall()
        data=[]
        for item in rows:
            tmp = {}
            tmp['sum']=item[0]
            tmp['user']=item[1]
            sql='select server_ip,cur_time from inlog where isLogin=1 and ldap_user=\''+item[1]+'\' order by cur_time DESC limit 1'
            self.obj_relay_cur.execute(sql)
            row = self.obj_relay_cur.fetchall()
            tmp['ip']=row[0][0]
            tmp['ltime']=row[0][1].strftime('%Y-%m-%d %H:%M:%S')
            data.append(tmp)
        data = json.dumps(data)
        self.obj_redis.set('relay_top_login_users_data', data)
        print sys._getframe().f_code.co_name
    '''
    def cache_relay_last_logins(self):
        sql='SELECT server_ip,ldap_user,cur_time FROM inlog WHERE isLogin=1 ORDER BY cur_time DESC LIMIT 10'
        self.obj_relay_cur.execute(sql)
        rows=self.obj_relay_cur.fetchall()
        data=[]
        for item in rows:
            tmp = {}
            tmp['ip']=item[0]
            tmp['user']=item[1]
            tmp['ltime']=item[2].strftime('%Y-%m-%d %H:%M:%S')
            data.append(tmp)
        data = json.dumps(data)
        self.obj_redis.set('relay_last_logins_data', data)
        print sys._getframe().f_code.co_name
        '''

    def relay_ldap_users_list(self,type=0):
	p = os.popen('bash -c \'ldapsearch -x -D "cn=Admin,dc=fuck,dc=com" -h ldap-s1.dns.fuck.com -w 123456 -b "dc=fuck,dc=com"|grep uid:|cut -b 6-\'')
        x = p.read()
        p.close()
	if type==0:
	    self.obj_redis.set('relay_ldap_users_list',x)
            print sys._getframe().f_code.co_name
        else:
            return x

    def cache_relay_ldap_month_botusers(self,type=0):
	sql='SELECT DISTINCT ldap_user AS b FROM inlog WHERE DATE_SUB(CURDATE(), INTERVAL 1 MONTH) <= DATE(cur_time)'
	self.obj_relay_cur.execute(sql)
        rows=self.obj_relay_cur.fetchall()
	allusers=self.relay_ldap_users_list(1).split('\n')
	ret_list=[]
	login_users=[]
	for i in rows:
	    login_users.append(i[0])
        for item in allusers:
            if item not in login_users:
                if item=='': continue
                tmp={}
                tmp['user']=item
                p = os.popen('bash -c \'ldapsearch -x -D "cn=Admin,dc=fuck,dc=com" -h ldap-s1.dns.fuck.com -w 123456 -b "cn=%s,ou=people,dc=fuck,dc=com"|grep userPassword\''%(item))
                x = p.read().strip()
                p.close()
                if len(x)<28:
                    tmp['state']='用户从未登陆过'
                else:
                    tmp['state']='超过30天未登录'
                tmp['ltime']=''
                tmp['ip']=''
                ret_list.append(tmp)
	data = json.dumps(ret_list)
	if type==0:
	    self.obj_redis.set('relay_ldap_month_botusers',data)
	    print sys._getframe().f_code.co_name
	else:
	    return data
    
    def cache_relay_month_botip(self,type=0):
        sql='SELECT ip FROM asset_hosts'
        self.obj_secdb_cur.execute(sql)
        rows = self.obj_secdb_cur.fetchall()
        all_ips=[]
        for ip in rows:
            all_ips.append(ip[0])
        sql='SELECT DISTINCT server_ip FROM inlog WHERE DATE_SUB(CURDATE(), INTERVAL 1 MONTH) <= DATE(cur_time)'
        self.obj_relay_cur.execute(sql)
        rows=self.obj_relay_cur.fetchall()
        logins_ips=[]
        for ip in rows:
            logins_ips.append(ip[0])
        data=[]
        for item in all_ips:
            if item not in logins_ips:
                tmp={}
                tmp['ip']=item
                tmp['state']='该IP在30天内未被访问'
                tmp['ltime']=''
                tmp['user']=''
                data.append(tmp)
        data = json.dumps(data)
        if type==0:
            self.obj_redis.set('relay_ldap_month_botips',data)
            print sys._getframe().f_code.co_name
        else:
            print data

    def cache_main(self):
        self.cache_relay_ldap_users_count()
        self.cache_relay_hosts_count()
        self.cache_relay_online_users_count()
        self.cache_relay_conn_hosts_count()
        self.cache_relay_month_linechart()
        self.cache_relay_month_onlie_users()
        self.cache_relay_month_onlie_hosts()
        self.cache_relay_top_login_hosts()
        self.cache_relay_top_login_users()
	self.cache_relay_ldap_month_botusers()
        #self.cache_relay_last_logins()







