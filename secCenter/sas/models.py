import time,datetime
import urllib,json
import hashlib
from pyes import *
from harpc import client
from harpc.common.config import Config
from tigercipher.cipher import CipherService
from tigercipher.client import CipherClient

class decrypt_log():
    def __init__(self):
        self.APP_KEY = 'ohnuToo5Se1rea'
        self.APP_SECRET = 'Hahpie4ohzie7aequulohjie7sah2Eev'
        try:
            self.conn = ES(['172.29.52.111:9200'])
        except Exception as e:
            print e
    def get_app_name(self,app_key):
        data={'Ka7Kohng2jahvaiz':'oauth.itiger.com',
              'eimooR6ohboo4ahk':'customer.tigerfintech.com',
              'Kahghiech7seighe':'www.itiger.com',
              'iewiy5eiViishiem':'crm.tigerfintech.com',
              'beepeingaeT8Yoor':'v.tigerfintech.com',
              'ShahraighooThe1n':'report',
              'li9dau9Xohro5ahj':'sms',
              'VeiH2Thael5enoh3':'script',
              'kegBTVnPP6WPMk2g':'excalibur',
              'bfQbKJXJOvWAUeoz':'payserver',
              'oRae9eethai0sh':'roc',
              'equobe5johtaBo':'am.itiger.com',
              'ohnuToo5Se1rea':'security'}
        return data[app_key]
    def search_es(self,index_type,str,userid,stime,etime):
        if index_type==1:
            self.conn.default_indices = ["secure*"]
        else:
            self.conn.default_indices = ["secure*"]
        atime = datetime.datetime.strptime(stime, "%Y-%m-%d %H:%M:%S")
        start_str = (atime - datetime.timedelta(hours=8)).strftime('%Y-%m-%dT%H:%M:%S.0Z')
        btime = datetime.datetime.strptime(etime, "%Y-%m-%d %H:%M:%S")
        end_str = (btime - datetime.timedelta(hours=8)).strftime('%Y-%m-%dT%H:%M:%S.0Z')
        q1=TermQuery('message','decrypt')
        q2 = TermQuery('message', 'success')
        if not userid:
            q3 = QueryStringQuery('*', 'message')
        else:
            q3 = QueryStringQuery(userid, 'message')
            #TermQuery('params_json.user_id', 'zhuzhengqing')
        if not str:
            q4 = QueryStringQuery('*', 'message')
        else:
            q4 = QueryStringQuery(str, 'message')
        q5=RangeQuery(qrange=ESRange('@timestamp',from_value=start_str,to_value=end_str))
        sq = BoolQuery(must=[q1,q2,q3,q4,q5])
        results=self.conn.search(sq)
        result=[]
        for  item in results:
            tmp={}
            tmp['client_ip']=item['params_json']['ip']
            tmp['app'] = self.get_app_name(item['params_json']['app_key'])
            tmp['server_ip'] = item['params_json']['client_ip']
            tmp['phone'] = item['params_json']['text']
            tmp['user'] = item['params_json']['user_id']
            timeStamp = item['params_json']["timestamp"]
            timeArray = time.localtime(int(timeStamp))
            tmp["ctime"] = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            result.append(tmp)
        return result
    def encrypt(self,str):
        zk_hosts = '172.31.48.17:2181,172.31.48.18:2181,172.31.48.20:2181'
        zk_path = '/cipher_internal'
        app_key = 'ohnuToo5Se1rea'
        app_secret = 'Hahpie4ohzie7aequulohjie7sah2Eev'
        cipher = CipherClient(zk_hosts, zk_path, app_key, app_secret)
        user_id = 'secCenter'
        ip = '172.30.65.2'
        result = cipher.encrypt(str, user_id, ip)
        return result
    def xhash(self, str):
        zk_hosts = '172.31.48.17:2181,172.31.48.18:2181,172.31.48.20:2181'
        zk_path = '/cipher_internal'
        app_key = 'ohnuToo5Se1rea'
        app_secret = 'Hahpie4ohzie7aequulohjie7sah2Eev'
        cipher = CipherClient(zk_hosts, zk_path, app_key, app_secret)
        user_id = 'secCenter'
        ip = '172.30.65.2'
        result = cipher.hash(str, user_id, ip)
        return result

        '''
    def signature(self,data):
        data['text'] = data['text'].encode('utf8')
        params = '&'.join(['{}={}'.format(k, v) for k, v in sorted(data.iteritems())])
        m = hashlib.md5()
        m.update(params + self.APP_SECRET)
        return m.hexdigest()
        
        #conf = Config()
        #conf.set("client", "use_zk", "False")
        #conf.set("client", "direct_address", "172.31.49.11:8801;172.31.49.11:8802")

        #manager = client.Client(CipherService.Client, conf)
        proxy_client = manager.create_proxy()
        data = {
            'text': str,
            'app_key': self.APP_KEY,
            'user_id': 150224,
            'ip': '192.168.9.100',
            'timestamp': int(time.time())
        }
        data['signature'] = self.signature(data)
        params = urllib.urlencode(data)
        return proxy_client.encrypt(params)
        '''

