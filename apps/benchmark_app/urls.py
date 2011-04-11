# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.defaults import *
from benchmark_app.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home, name='home'),

    url(r'^static/$', static, name='static'),

    url(r'^simple_db_query/$', simple_db_query, name='simple_db_query'),
    url(r'^sequential_db_query/$', sequential_db_query, name='sequential_db_query'),
    url(r'^complex_db_query/$', complex_db_query, name='complex_db_query'),

    url(r'^db_write/$', db_write, name='db_write'),

    url(r'^upload/$', upload, name='upload'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
