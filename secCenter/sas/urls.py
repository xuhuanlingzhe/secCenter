from django.conf.urls import url
from views import *
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'decryptindex', decrypt_index),
    url(r'api', api),
]