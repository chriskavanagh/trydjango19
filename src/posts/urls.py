from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from . import views

urlpatterns = [

    # create view
    url(r'^create/$', views.post_create, name='create'),
    # list view
    url(r'^$', views.post_list, name='list'),
    # detail view
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='detail'),
    # update view
    url(r'^(?P<pk>\d+)/update/$', views.post_update, name='update'),
    # delete view
    url(r'^(?P<pk>\d+)/delete/$', views.post_delete, name='delete'),
    # order food_form.html
    url(r'^order/$', views.food_form, name='order'),
    
]
