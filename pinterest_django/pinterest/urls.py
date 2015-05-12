from django.conf.urls import patterns, include, url
from django.contrib import admin

import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pinterest_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^create_pin/$', views.create_pin, name='create_pin'),
    url(r'^(?P<user_id>[\d]+)/my_boards/$', views.my_boards, name='my_boards'),
)
