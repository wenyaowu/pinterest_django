from django.conf.urls import patterns, include, url
from django.contrib import admin

import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pinterest_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^create_pin/$', views.create_pin, name='create_pin'),
    url(r'^create_board/$', views.create_board, name='create_board'),
    url(r'^(?P<user_id>[\d]+)/boards/$', views.boards, name='boards'),
    url(r'^(?P<user_id>[\d]+)/boards/(?P<board_slug>[\w\-]+)/$', views.board, name='board'),
)
