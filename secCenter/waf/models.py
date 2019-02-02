# -*- coding: utf-8 -*-
from django.db import models,connection
from lib.pub import pub
import urllib,urllib2,os,base64

class waf_servers(models.Model):
    #id=models.IntegerField()
    name=models.CharField(max_length=30)
    ip=models.CharField(max_length=16)
    version=models.CharField(max_length=30)
    state=models.IntegerField(default=True)
    master=models.IntegerField(default=False)
    class Meta:
        db_table="waf_servers"
        ordering=['id']

class waf_sites(models.Model):
    domain=models.CharField(max_length=256)
    ip=models.CharField(max_length=512)
    state=models.BooleanField(default=True)
    cc=models.BooleanField(default=False)
    create_time=models.DateTimeField(auto_now_add=True)
    last_update_time=models.DateTimeField(auto_now=True)
    last_attack_time=models.DateTimeField()
    last_attack_type=models.CharField(max_length=16)
    attack_sum=models.IntegerField(default=0)
    http=models.BooleanField(default=True)
    https=models.BooleanField(default=False)
    class Meta:
        db_table="waf_sites"
        ordering=['id']

class xapi():
    def api_get(self,url):
        req = urllib2.Request(url)
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        return res
    def master_waf_api_get(self,url):
        ip=waf_servers.objects.filter(master=True).values_list('ip','name')[0]
        result = []
        cur_url = "http://%s:5460%s" % (ip[0], url)
        ret = self.api_get(cur_url)
        return ret
    def all_waf_api_get(self,url):
        ips = waf_servers.objects.values_list('ip','name')
        result=[]
        for ip in ips:
            cur_url="http://%s:5460%s"%(ip[0],url)
            ret=self.api_get(cur_url)
            tmp={}
            tmp['ip']=ip[0]
            tmp['waf_name']=ip[1]
            tmp['msg']=ret
            result.append(tmp)
        return result

    def api_post(self,url,data):
        try:
            data_urlencode = urllib.urlencode(data)
            req = urllib2.Request(url=url, data=data_urlencode)
            res_data = urllib2.urlopen(req)
            res = res_data.read()
        except Exception as e:
            res=e
        return res
    def all_waf_api_post(self,url,post_data):
        ips = waf_servers.objects.values_list('ip','name')
        result = []
        for ip in ips:
            cur_url="http://%s:5460%s"%(ip[0],url)
            ret=self.api_post(cur_url,post_data)
            tmp={}
            tmp['ip']=ip[0]
            tmp['waf_name']=ip[1]
            tmp['msg']=ret
            result.append(tmp)
        return result

class sitesManage():
    def __init__(self):
        self.pemdir='/opt/openresty/waf/conf/ssl'
    def read_sites_conf(self):
        confs=[]
        return confs
    def create_site_conf(self,site_domain,ips_str,chk_http,chk_https):
        if not pub.isDomain(site_domain):
            return False
        try:
            tm_file_path=os.path.abspath('.')+'/waf/http.conf'
            tm_file_path=os.path.abspath(tm_file_path)
            tm_file=open(tm_file_path,'r')
            buff=tm_file.read()
            tm_file.close()
            stream_name=site_domain.replace('.','_')
            ips=ips_str.split(',')
            server_conf=''
            for ip in ips:
                if not pub.isIP(ip):
                    return False
                server_conf=server_conf+'        server '+ip+' max_fails=1 fail_timeout=10s; \n'
            buff=buff.replace('[stream_name]',stream_name)
            buff =buff.replace('[server_conf]',server_conf)
            buff =buff.replace('[site_domain]',site_domain)
            if chk_https:
                domain_key=pub.get_top_domain(site_domain)+'.pem'
                file_pem_path="%s/%s"%(self.pemdir,domain_key)
                file_key_path="%s/%s"%(self.pemdir,domain_key)
                https_conf_str='ssl_session_timeout  5m;\n    ssl_protocols  TLSv1 TLSv1.1 TLSv1.2;\n    ssl_ciphers  HIGH:!RC4:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!EXP:+MEDIUM;\n    ssl_prefer_server_ciphers   on; \n\
                \n    ssl_certificate %s;\n    ssl_certificate_key %s;\n'%(file_pem_path,file_key_path)
                buff = buff.replace('[https_443]', 'listen     443;')
                buff = buff.replace('[https_cert_conf]',https_conf_str)
            else:
                buff = buff.replace('[https_443]', '')
                buff = buff.replace('[https_cert_conf]', '')
            buff=base64.b64encode(buff)
            x_api = xapi()
            url="/api/nginx_conf?action=add&file=%s"%(site_domain+".conf")
            postdata = {"data": buff}
            result=x_api.all_waf_api_post(url,postdata)
            try:
                waf_sites.objects.create(ip=ips_str, domain=site_domain,http=chk_http,https=chk_https)
            except Exception,e:
                print(e)
        except Exception,e:
            print(e)
            return ""
        return result
