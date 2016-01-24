from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^item/(?P<item_id>\d+)/?$', views.item, name='view_item'),
]
