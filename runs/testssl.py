from sslinfo import sslinfo
#from sec_redis import sec_redis

#print 'start sslinfo'
ssl_obj=sslinfo()
ssl_obj.get_domain_json()
#sr=sec_redis()
#a=sr.relay_ldap_users_list(1)
#a=sr.cache_relay_month_botip(1)
#print a

