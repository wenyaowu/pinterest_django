from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pinterest_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^pinterest/', include('pinterest.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^socialauth/', include('social.apps.django_app.urls',namespace='social')),
)
