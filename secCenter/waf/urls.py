from django.conf.urls import url
from views import *
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'index', index),
    url(r'set', set),
    url(r'sites', sites),
    url(r'api', api),
    url(r'pubrules', rules_pub),
]