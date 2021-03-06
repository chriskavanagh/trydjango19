"""trydjango19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    url(r'^posts/', include('posts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.HomePageView, name='home'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^my-login/$', views.my_login, name='my_login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.sign_up, name='register'),
    #url(r'^form/$', views.user_form, name='form'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
