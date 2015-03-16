from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from views import *


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       
    url(r'^$', TemplateView.as_view(template_name='home.html')),                

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^(?P<year>\d\d\d)/new/$', register, name='add-participant'),
    url(r'^sponsor_logos/', list_sponsor_logos, name='list_sponsor_logos'),
    
    
)

# TODO: Add production collecting of files
urlpatterns += staticfiles_urlpatterns()

