from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #/itInventory/
    url(r'^itInventory/', include('itInventory.urls', namespace='itInventory')),
    url(r'^admin/', admin.site.urls),
)
