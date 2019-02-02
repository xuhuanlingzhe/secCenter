from django.db import models

class xhosts(models.Model):
    ip=models.CharField(max_length=15)
    hostname=models.CharField(max_length=32)
    os=models.CharField(max_length=64)
    dev_type=models.IntegerField()
    asset_value=models.IntegerField()
    vul_sum=models.IntegerField()
    alert_sum=models.IntegerField()
    ctime=models.DateTimeField()
    class Meta:
        db_table="asset_hosts"
        ordering=['ip']

class xports(models.Model):
    ip=models.CharField(max_length=15)
    port=models.IntegerField()
    stype=models.CharField(max_length=128)
    service=models.CharField(max_length=128)
    version=models.CharField(max_length=256)
    state=models.CharField(max_length=50)
    protocol=models.CharField(max_length=50)
    tags=models.CharField(max_length=256)
    #service_info=service.join(version)
    class Meta:
        db_table="asset_ports"
        ordering=['ip']

class xdomain(models.Model):
    domain=models.CharField(max_length=64)
    ip=models.CharField(max_length=128)
    state=models.IntegerField()
    ctime=models.DateTimeField()
    ssl_info=models.CharField(max_length=1024)
    ssl_etime=models.DateTimeField()
    class Meta:
        db_table="asset_sslinfo"
        ordering=['-ctime']

class rootdomain(models.Model):
    name=models.CharField(max_length=64)
    reg_email=models.CharField(max_length=64)
    etime=models.DateTimeField()
    tmp=models.DateTimeField()
    class Meta:
        db_table="asset_domains"
        ordering=['id']

class domain_person(models.Model):
    domain=models.CharField(max_length=64)
    name=models.CharField(max_length=64)
    usage=models.CharField(max_length=256)
    yf_person=models.CharField(max_length=32)
    cp_person=models.CharField(max_length=32)
    sy_person=models.CharField(max_length=32)
    other=models.CharField(max_length=512)
    last_time=models.DateTimeField()
    class Meta:
        db_table="asset_domains_person"
        ordering=['id']