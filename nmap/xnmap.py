#/usr/bin/env python
# -*- coding:UTF-8 -*-

import sys,nmap,MySQLdb,threading,Queue,urllib2,re,ssl,json,base64,requests,StringIO,gzip
reload(sys)
#sys.setdefaultencoding('utf-8')
#ip_list="192.168.110.56"
ports="1-65535"
#ports="1-10000"
conn=None
db=None
queue=Queue.Queue()

#sys.setrecursionlimit(100000)
try:
    _create_unverified_https_context = ssl._create_unverified_context  # 忽略证书错误
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

def get_code(header, html):
    try:
        m = re.search(r'<meta.*?charset=(.*?)"(>| |/)', html, flags=re.I)
        if m: return m.group(1).replace('"', '')
    except:
        pass
    try:
        if 'Content-Type' in header:
            Content_Type = header['Content-Type']
            m = re.search(r'.*?charset=(.*?)(;|$)', Content_Type, flags=re.I)
            if m: return m.group(1)
    except:
        pass

def get_tag(html):
    try:
	try:
	    db.ping()
	except:
	    init_db()
        sql = "select name,tag from asset_tags_tmp"
	try:
            num = conn.execute(sql)
	except:
	    init_db()
	    num = conn.execute(sql)
        rows = conn.fetchall()
        for row in rows:
            name=row[0]
            tag=row[1]
            m = re.search(tag, html, flags=re.I)
            if m: return name
    except Exception,e:
	print Exception,':7',e
        return None

def tryweb(ip_port):
    title_str,html='',''
#    if port<80: return
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        if ip_port[-3:]=='443':
            req = urllib2.Request(url="https://%s" % (ip_port), headers=headers)
            info=urllib2.urlopen(req,timeout=5)
        else:
            req = urllib2.Request(url="http://%s"%(ip_port), headers=headers)
            info=urllib2.urlopen(req,timeout=2)
        html=info.read()
        header=info.headers
    except urllib2.HTTPError,e:
        try:
            html=e.read()
            header=e.headers
        except Exception,e:
	    print Exception,':4',e
            return
    except Exception,e:
	#print Exception,':5',e
        return
    if not header: 
	return
    if 'Content-Encoding' in header and 'gzip' in header['Content-Encoding']:  # 解压gzip
        html_data = StringIO.StringIO(html)
        gz = gzip.GzipFile(fileobj=html_data)
        html = gz.read()
    try:
        title = re.search(r'<title>(.*?)</title>', html, flags=re.I | re.M)
        if title: title_str = title.group(1)
    except Exception,e:
	print Exception,':3',e
        pass
    tag=get_tag(str(header)+html)
    if not tag:
        tag=title_str
    if (not tag) or tag=="":
        return
    n=ip_port.index(':')
    UpdatePortTag(ip_port[:n],ip_port[n+1:],tag)
    #print tag

def UpdatePortTag(ip,port,tagname):
    try:
	db.ping()
    except:
	init_db()
    try:
        sql="update asset_ports_tmp set tags='%s' where  ip='%s' and port=%s"%(tagname,ip,port)
        conn.execute(sql)
    except Exception,e:
	print Exception,':1',e	
        pass
    try:
        sql="update asset_tags_tmp set num=num+1 where name='%s'"%(tagname)
        conn.execute(sql)
    except Exception,e:
	print Exception,':2',e
        pass

def UpdateHostName():
    url ='http://ebs.guazi-corp.com/Service/API/index/api/EbsInterface/action/getServerInfo/token/sec-get-info/type/3/info/'
    headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
            'Accept': 'text / html, application / xhtml + xml,application / xml;',
            'Accept - Encoding': 'gzip, deflate',
    }
    try:
	db.ping()
    except:
	init_db()
    try:
        conn.execute("select ip from asset_hosts_tmp")
    except:
	init_db()
	conn.execute("select ip from asset_hosts_tmp")
    rows=conn.fetchall()
    data = []
    for row in rows:
        data.append(str(row[0]))
    datas=json.dumps(data)
    datas1=base64.b64encode(datas)
    params={
        'token':'sec-get-info',
        'type':'3',
        'info':datas1
    }
    resp = requests.get(url,params=params, headers=headers)
    text = resp.text
    data=json.loads(text)
    data=json.loads(data['info'])
    for it in data:
        for item in it:
            ip=item
            tmp=it[item]
            for ha in tmp:
                #print ip
                #print ha
                conn.execute("update asset_hosts set hostname='%s' where ip='%s'"%(ha,ip))

def init_db():
    global db
    db = MySQLdb.connect(host='127.0.0.1',port=3306,user='sec_db_w',passwd='123456',db='sec_db',charset='utf8')
    global conn
    conn=db.cursor()

def InsertHost(ip,hostname,os):
    try:
        db.ping()
    except:
        init_db()
    #conn=db.cursor()
    sql="insert into asset_hosts_tmp(ip,hostname,os) values('%s','%s','%s')"%(ip,hostname,os)
    try:
        conn.execute(sql)
    except:
        init_db()
	conn.execute(sql)
    return conn.lastrowid

def InsertPort(ip,port,stype,service,version,state,protocol):
    try:
        db.ping()
    except:
        init_db()
    #conn=db.cursor()
    sql="insert into asset_ports_tmp(ip,port,stype,service,version,state,protocol) value(%s,%s,%s,%s,%s,%s,%s)"
    val=[ip,port,stype,service,version,state,protocol]
    #ret = None
    try:
        ret = conn.execute(sql,val)
    except:
	init_db()
	ret = conn.execute(sql,val)
    return ret

def scan(ip_list):
    try:
        nm=nmap.PortScanner()
    except:
        print('nmap not fount',sys.exc_info()[1])
        sys.exit(0)

    try:
        nm.scan(ip_list.encode('utf8'),arguments=' -sT -O -p ' + ports)
    except Exception,e:
        print("scan error:"+str(e))
    for host in nm.all_hosts():
        #print("host:%s"%host)
#	print nm[host].state()
	host_os=''
        if 'osmatch' in nm[host]:
            for osmatch in nm[host]['osmatch']:
                host_os=format(osmatch['name'])
                #print('Os : {0}'.format(osmatch['name']))
        InsertHost(host,nm[host].hostname(),host_os)
        for proto in nm[host].all_protocols():
            #print("Protocol:%s"%proto)
            lport=nm[host][proto].keys()
            lport.sort()
            for port in lport:
		#print 'insert port start'
                InsertPort(host,port,nm[host][proto][port]['name'],nm[host][proto][port]['product'],nm[host][proto][port]['version'],nm[host][proto][port]['state'],proto)
                tryweb(host+':'+str(port))
                #print("port:%s\tstate:%s"%(port,nm[host][proto][port]['state']))
                #print("\tname:%s"%nm[host][proto][port]['name'])
                #print("\tservice:%s"%nm[host][proto][port]['product'])
                #print("\tversion:%s"%nm[host][proto][port]['version'])
def InitTables():
    #删除2号表
    try:
        conn.execute("drop table asset_hosts_tmp,asset_ports_tmp,asset_tags_tmp")
    except:
        print("")
    conn.execute("create table asset_hosts_tmp like asset_hosts")
    conn.execute("create table asset_ports_tmp like asset_ports")
    conn.execute("create table asset_tags_tmp like asset_tags")
    conn.execute("insert into asset_tags_tmp select * from asset_tags")
    conn.execute("update asset_tags_tmp set num=0")

def EndTables():
    #删除2号表
    try:
        conn.execute("drop table asset_hosts5,asset_ports5")
    except:
        print("no tables5")
    #将表1重命名为表2
    try:
        conn.execute("rename table asset_hosts4 to asset_hosts5")
        conn.execute("rename table asset_ports4 to asset_ports5")
        conn.execute("rename table asset_hosts3 to asset_hosts4")
        conn.execute("rename table asset_ports3 to asset_ports4")
        conn.execute("rename table asset_hosts2 to asset_hosts3")
        conn.execute("rename table asset_ports2 to asset_ports3")
        conn.execute("rename table asset_hosts1 to asset_hosts2")
        conn.execute("rename table asset_ports1 to asset_ports2")
        conn.execute("rename table asset_hosts to asset_hosts1")
        conn.execute("rename table asset_ports to asset_ports1")
        conn.execute("rename table asset_hosts_tmp to asset_hosts")
        conn.execute("rename table asset_ports_tmp to asset_ports")
    except:
        print("renname asset tables error!")
    try:
	conn.execute("drop table asset_tags")
        conn.execute("rename table asset_tags_tmp to asset_tags")
    except:
	print('rename table asset_tags error!')

def Tmain():
    while True:
        if not queue.empty():
            ip_str=queue.get()
            print(ip_str+" start")
            scan(ip_str)
            queue.task_done()
        else:
            break
	
def AllScan():
    sql="select ips from asset_iplist"
    num = conn.execute(sql)
    rows = conn.fetchall()
    global queue
    for row in rows:
        tmp=row[0]
        tmp=tmp.split(",")
        for ips in tmp:
            queue.put(ips)
        #scan()
    Tmain()
    #threads = []
    #for i in xrange(0,5):
    #    t1=threading.Thread(target=Tmain)
    #    threads.append(t1)
    #for t in threads:
    #    t.start()
    #for t in threads:
    #    if t.isAlive():
    #        t.join()
    #print "Update hostname now!"
    #UpdateHostName()
    EndTables()
    print "scan all end"
	
if __name__=='__main__':
    init_db()
    for arg in sys.argv:
        if arg=="test":
	    InitTables()
            print "test"
	    global ports
	    ports="1-1000"
            scan('172.30.65.0/30')
	    EndTables()
            sys.exit(0)
    InitTables()
    AllScan()

