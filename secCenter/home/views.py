# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'user_login.html')
def home(request):
    try:
        #uid=request.session['uid']
        return render(request, 'index.html')
    except:
        return render(request, 'user_login.html')