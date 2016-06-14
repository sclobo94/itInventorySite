from django.conf.urls import url
from django.conf.urls.static import static
from untitled1 import settings
from . import views

app_name = 'itInventory'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addItem/$', views.addItem, name='addItem'),
    url(r'^viewInventory/$', views.viewInventory, name='viewInventory'),
    url(r'^searchItem/$', views.searchItem, name='searchItem'),
    url(r'^queryInventory/$', views.queryInventory, name='queryInventory'),
    url(r'^itemDetail/(?P<item_ID>[0-9]+)/$', views.itemDetail, name='itemDetail'),
    url(r'^updateItem/(?P<item_ID>[0-9]+)/$', views.updateItem, name='updateItem'),
    url(r'^deleteItem/(?P<item_ID>[0-9]+)/$', views.deleteItem, name='deleteItem'),
]