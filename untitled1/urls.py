from django.conf.urls import url, include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    #/itInventory/
    url(r'^itInventory/', include('itInventory.urls', namespace='itInventory')),
    url(r'^admin/', admin.site.urls),
]
