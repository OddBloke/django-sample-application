# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', include('benchmark_app.urls')),
)

# the assets
if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^assets/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
