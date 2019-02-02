from django.conf.urls import url
from views import *
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'index', index),
    url(r'domains', domains),
    url(r'rds', rootdomains),
    url(r'api', api),
    url(r'hosts', hosts),
    url(r'ports', ports),
]