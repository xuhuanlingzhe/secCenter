# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import *
import json

# Create your views here.
def index(request):
    return render(request, 'asset_summary.html',{'tag1':"active open",'subtag1':"active open"})
def domains(request):
    return render(request, 'asset_domains.html',{'tag1':"active open",'subtag14':"active open"})
def rootdomains(request):
    return render(request, 'asset_root_domains.html',{'tag1':"active open",'subtag15':"active open"})
def hosts(request):
    return render(request, 'asset_hosts.html', {'tag1': "active open", 'subtag12': "active open"})
def ports(request):
    return render(request, 'asset_ports.html', {'tag1': "active open", 'subtag13': "active open"})

def api(request):
    mod = request.GET.get('action', '')
    if mod=="":
        data = "fuck you!"
        return HttpResponse(data)
    if mod=="listdomains":
        rows = xdomain.objects.all()
        data = []
        for row in rows:
            tmp = {}
            tmp['domain'] = row.domain
            tmp['ip'] = row.ip
            tmp['state'] = row.state
            tmp['time'] = row.ctime.strftime('%Y-%m-%d %H:%M:%S')
            tmp['ssl'] = row.ssl_info
            data.append(tmp)
        data = json.dumps(data)
        return HttpResponse(data, content_type="json")
    if mod=="listhosts":
        rows = xhosts.objects.all()
        data = []
        for row in rows:
            tmp = {}
            tmp['hn'] = row.hostname
            tmp['ip'] = row.ip
            tmp['ht'] = row.dev_type
            tmp['os'] = row.os
            tmp['av'] = row.asset_value
            tmp['vs'] = row.vul_sum
            tmp['as'] = row.alert_sum
            data.append(tmp)
        data = json.dumps(data)
        return HttpResponse(data, content_type="json")
    if mod=="listports":
        rows = xports.objects.all()
        data = []
        for row in rows:
            tmp = {}
            tmp['ip'] = row.ip
            tmp['port'] = row.port
            tmp['stype'] = row.stype
            tmp['service'] = row.service
            tmp['state'] = row.state
            tmp['proto'] = row.protocol
            tmp['tags'] = row.tags
            data.append(tmp)
        data = json.dumps(data)
        return HttpResponse(data, content_type="json")
    if mod=="listrootdomains":
        rows = rootdomain.objects.all()
        data = []
        for row in rows:
            tmp = {}
            tmp['domain'] = row.name
            tmp['etime'] = row.etime.strftime('%Y-%m-%d %H:%M:%S')
            ssl_rows=xdomain.objects.filter(ssl_info__icontains=tmp['domain'])
            if ssl_rows.count()<1:
                tmp['ssl']=""
                tmp['ssltime']=""
            else:
                tmp['ssltime']=xdomain.objects.filter(ssl_info__icontains=tmp['domain'])[0].ssl_etime.strftime('%Y-%m-%d %H:%M:%S')
                tmp['ssl'] = xdomain.objects.filter(ssl_info__icontains=tmp['domain'])[0].ssl_info[0:-(len(tmp['ssltime'])+1)]
            data.append(tmp)
        data = json.dumps(data)
        return HttpResponse(data, content_type="json")
    if mod=="edit_domain_person":
        str_domain = request.GET.get('lb_domain', '')
        str_usage=request.GET.get('tb_usage', '')
        str_sysname=request.GET.get('tb_sysname', '')
        str_yf_name=request.GET.get('tb_yf', '')
        str_cp_name = request.GET.get('tb_cp', '')
        str_sy_name=request.GET.get('tb_sy', '')
        str_other = request.GET.get('tb_other', '')
        try:
            dp = domain_person.objects.get(domain=str_domain)
        except:
           dp = None
        if not dp:
            dp = domain_person(domain=str_domain)
        dp.name=str_sysname
        dp.usage=str_usage
        dp.yf_person=str_yf_name
        dp.cp_person = str_cp_name
        dp.sy_person=str_sy_name
        dp.other=str_other
        dp.save()
        return HttpResponse('ok')
    if mod == "get_domain_person":
        str_domain = request.GET.get('domain', '')
        data = {}
        try:
            dp = domain_person.objects.get(domain=str_domain)
            data['domain'] = str_domain
            data['name'] = dp.name
            data['usage'] = dp.usage
            data['yf_person'] = dp.yf_person
            data['cp_person'] = dp.cp_person
            data['sy_person'] = dp.sy_person
            data['other'] = dp.other
            data['ltime'] = dp.last_time.strftime('%Y-%m-%d %H:%M:%S')
        except:
           pass
        data = json.dumps(data)
        return HttpResponse(data, content_type=json)


