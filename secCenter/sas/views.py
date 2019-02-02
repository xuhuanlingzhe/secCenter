# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from models import *

def decrypt_index(request):
    return render(request, 'sas_decrypt_index.html', {'tag3': "active open", 'subtag36': "active open"})
def api(request):
    mod = request.GET.get('action', '')
    if mod=="":
        data = "fuck you!"
        return HttpResponse(data)
    if mod=="en_phone":
        phone_str = request.GET.get('phone', '')
        d_api=decrypt_log()
        data=d_api.encrypt(phone_str)
        items=data.split(':')
        if len(items)>1:
            data=items[1]
        return HttpResponse(data)
    if mod=="hash_phone":
        phone_str = request.GET.get('phone', '')
        d_api=decrypt_log()
        data=d_api.xhash(phone_str)
        data=data[0]
        return HttpResponse(data)
    if mod=="index_phone":
        phone_str = request.GET.get('enphone', '')
        user_str = request.GET.get('user', '')
        itype = request.GET.get('type', '')
        stime = request.GET.get('stime', '')
        etime = request.GET.get('etime', '')
        d_api = decrypt_log()
        data=d_api.search_es(int(itype),phone_str,user_str,stime,etime)
        data=json.dumps(data)
        return HttpResponse(data,content_type="json")

