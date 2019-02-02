# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from models import *
import json

# Create your views here.
def index(request):
    return render(request, 'waf_summary.html',{'tag2':"active open",'subtag11':"active open"})

def set(request):
    return render(request, 'waf_set.html', {'tag2': "active open", 'subtag26': "active open"})
def sites(request):
    return render(request, 'waf_sites.html', {'tag2': "active open", 'subtag24': "active open"})
def rules_pub(request):
    return render(request, 'waf_rules_pub.html', {'tag2': "active open", 'subtag22': "active open"})

def get_rules(rule_type):
    ips = waf_servers.objects.filter(master=True).values_list('ip')
    cur_url = "http://%s:5460/api/config_dict?action=get&mod=%s" % (ips[0][0],rule_type)
    x_api = xapi()
    ret = x_api.api_get(cur_url)
    ret = json.loads(ret)
    data = []
    ret.pop("state")
    ret.pop("code")
    for n in ret:
        tmp = {}
        tmp["sid"] = n
        tmp["rule"] = ret[n]
        data.append(tmp)
    data = json.dumps(data)
    return data

def save_rule(rule_mod):
    url="/api/config?action=save&mod=%s&debug=no"%(rule_mod)
    x_api = xapi()
    ret = x_api.master_waf_api_get(url)
    return ret

def update_rule(rule_mod,rule_id,rule_txt):
    if rule_mod!='denyMsg':
        rule_mod=rule_mod+'_Mod'
    rule_txt={"value":rule_txt}
    rule_txt=urllib.urlencode(rule_txt)
    url = "/api/config_dict?action=set&mod=%s&id=%s&value_type=json&%s" % (rule_mod,rule_id,rule_txt)
    x_api = xapi()
    ret = x_api.master_waf_api_get(url)
    if ret.find('"code":"error"')>0:
        return ret
    ret=save_rule(rule_mod)
    return ret

def del_rule(rule_mod,rule_id):
    if rule_mod!='denyMsg':
        rule_mod=rule_mod+'_Mod'
    url = "/api/config_dict?action=del&mod=%s&id=%s" % (rule_mod,rule_id)
    x_api = xapi()
    ret = x_api.master_waf_api_get(url)
    if ret.find('"code":"error"')>0:
        return ret
    ret=save_rule(rule_mod)
    return ret

def add_rule(rule_mod,rule_id,rule_txt):
    if rule_mod!='denyMsg':
        rule_mod=rule_mod+'_Mod'
    rule_txt={"value":rule_txt}
    rule_txt=urllib.urlencode(rule_txt)
    url = "/api/config_dict?action=add&mod=%s&id=%s&value_type=json&%s" % (rule_mod,rule_id,rule_txt)
    x_api = xapi()
    ret = x_api.master_waf_api_get(url)
    if ret.find('"code":"error"')>0:
        return ret
    ret=save_rule(rule_mod)
    return ret


def api(request):
    mod = request.GET.get('action', '')
    if mod=="":
        data = "fuck you!"
        return HttpResponse(data)
    if mod=="listwaf":
        itemlist=waf_servers.objects.all()
        data = json.dumps(list(itemlist.values()))
        return HttpResponse(data, content_type="json")
    if mod=="listsite":
        itemlist=waf_sites.objects.all()
        data=[]
        for item in itemlist.values():
            tmp = {}
            tmp['id']=item['id']
            tmp['domain']=item['domain']
            tmp['ip']=item['ip']
            if item['state']:
                tmp['state']='waf open</br>'
            else:
                tmp['state'] ='waf close</br>'
            if item['cc']:
                tmp['state']+="cc open"
            tmp['last_attack']="%s</br>%s"%(item['last_attack_time'].strftime('%Y-%m-%d %H:%M:%S'),item['last_attack_type'])
            tmp['attack_sum']=item['attack_sum']
            data.append(tmp)
        data=json.dumps(data)
        return HttpResponse(data, content_type="json")
        # wafip = waf_servers.objects.values('ip')[0]
        # #domain = "http://"+urlparse.urlparse(request.get_host()).path
        # wafurl="http://"+wafip["ip"]+":5460/api/nginx_config?action=list"
        # xapi1=xapi()
        # data=xapi1.api_get(wafurl).replace('_','.').replace('.conf','')
        # data = json.dumps(data)
        # return HttpResponse(data, content_type="json")
    if mod=="getsiteinfo":
        domain_id = request.GET.get('id', '')
        item = waf_sites.objects.filter(id=domain_id)
        data=item.values_list("ip")[0]
        return HttpResponse(data, content_type="json")
    if mod=="getsite":
        domain_str = request.GET.get('domain', '')
        url='/api/nginx_conf?action=get&file=%s.conf'%(domain_str)
        x_api=xapi()
        data=x_api.master_waf_api_get(url)
        return HttpResponse(data)
    if mod=="editsite":
        domain_str = request.POST.get('site_domain', '')
        domain_data=request.POST.get('site_conf_txt', '')
        buff = base64.b64encode(domain_data)
        x_api = xapi()
        url = "/api/nginx_conf?action=add&file=%s" % (domain_str + ".conf")
        postdata = {"data": buff}
        data = x_api.all_waf_api_post(url, postdata)
        return HttpResponse(data)
    if mod=="addsite":
        domain_str = request.POST.get('domain', '')
        http_str = bool(request.POST.get('http', True))
        https_str = bool(request.POST.get('https', False))
        ips_str = request.POST.get('ips', '')
        site_info=waf_sites.objects.filter(domain=domain_str)
        if site_info:
            return HttpResponse(domain_str+' already have!')
        sm=sitesManage()
        ret= sm.create_site_conf(domain_str, ips_str, http_str, https_str)
        return HttpResponse(ret)
    if mod=="delsite":
        domain_str=request.GET.get('domain', '')
        url='/api/nginx_conf?action=del&file=%s.conf'%(domain_str)
        x_api=xapi()
        ret=x_api.all_waf_api_get(url)
        obj=waf_sites.objects.filter(domain=domain_str)
        obj.delete()
        return HttpResponse(ret)
    if mod=="reloadnginx":
        url='/api/nginx?action=reload'
        x_api=xapi()
        ret=x_api.all_waf_api_get(url)
        return HttpResponse(ret)
    if mod=="getrules":
        rule_type = request.GET.get('mod', '')
        if rule_type=='args':
            data=get_rules('args_Mod')
            return HttpResponse(data)
        if rule_type=='post':
            data=get_rules('post_Mod')
            return HttpResponse(data)
        if rule_type=='uri':
            data=get_rules('uri_Mod')
            return HttpResponse(data)
        if rule_type=='network':
            data=get_rules('network_Mod')
            return HttpResponse(data)
        if rule_type=='method':
            data=get_rules('host_method_Mod')
            return HttpResponse(data)
        if rule_type=='header':
            data=get_rules('header_Mod')
            return HttpResponse(data)
        if rule_type=='referer':
            data=get_rules('referer_Mod')
            return HttpResponse(data)
        if rule_type=='useragent':
            data=get_rules('useragent_Mod')
            return HttpResponse(data)
        if rule_type=='rewrite':
            data=get_rules('rewrite_Mod')
            return HttpResponse(data)
        if rule_type=='cookie':
            data=get_rules('cookie_Mod')
            return HttpResponse(data)
        if rule_type=='replace':
            data=get_rules('replace_Mod')
            return HttpResponse(data)
        if rule_type=='realIpfrom':
            data=get_rules('realIpFrom_Mod')
            return HttpResponse(data)
        if rule_type=='denymsg':
            data=get_rules('denyMsg')
            return HttpResponse(data)
    if mod=="editrule":
        rmod = request.GET.get('type', '')
        rid = request.POST.get('rule_id', '')
        rtxt=request.POST.get('rule_txt', '')
        data=update_rule(rmod,rid,rtxt)
        return HttpResponse(data)
    if mod=="delrule":
        rmod=request.GET.get('type', '')
        rid=request.GET.get('rule_id', '')
        data=del_rule(rmod,rid)
        return HttpResponse(data)
    if mod=="addrule":
        rmod = request.GET.get('type', '')
        rid = request.POST.get('input_rule_id', '')
        rtxt = request.POST.get('rule_txt1', '')
        data=add_rule(rmod,rid,rtxt)
        return HttpResponse(data)





