from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pinterest_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^pinterest/', include('pinterest.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^socialauth/', include('social.apps.django_app.urls',namespace='social')),

)

urlpatterns += patterns('django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )