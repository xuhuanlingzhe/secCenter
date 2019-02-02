# -*- coding: utf-8 -*-
# @File  : run.py.py
# @Author: 张杰 (虚幻灵者)
# @Date  : 2017/9/28 0028
# @Desc  :
from sslinfo import sslinfo
#from sec_redis import sec_redis
from threading import Timer

def two_hour_func():
    print 'start sslinfo'
    ssl_obj=sslinfo()
    ssl_obj.get_domain_json()
    Timer(43200, two_hour_func).start()

def five_minute_func():
    sr=sec_redis()
    sr.cache_main()
    Timer(300, five_minute_func).start()

if __name__== '__main__':
    Timer(43200,two_hour_func).start()   #12小时循环任务
    #Timer(1800,two_hour_func).start()
    #Timer(300, five_minute_func).start()  # 5分钟，循环任务
    #sr=sec_redis()
    #sr.cache_main()

