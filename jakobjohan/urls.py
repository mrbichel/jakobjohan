from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^a/', include(admin.site.urls)),

    url(r'^$', 'views.home', name='home'),
    url(r'^leather-sleeves/$', 'views.sleeves', name='leather-sleeves'),
    url(r'^contact/$', direct_to_template, {'template': 'contact.html'}, name='contact'),
    url(r'^story/$', 'views.story', name='story'),


)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
    (r'^m/(?P<path>.*)$',
        'serve', {
        'document_root': settings.MEDIA_ROOT,
        'show_indexes': True }),)