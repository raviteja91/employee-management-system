from django.conf.urls.defaults import *

from django.contrib import admin
from django.contrib import databrowse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic.simple import direct_to_template, redirect_to
from django.contrib.auth.views import password_change
from django.core.urlresolvers import reverse
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

try:
    admin.autodiscover()
except admin.sites.AlreadyRegistered:
    # This try-except is required to make nose doctest happy
    pass

urlpatterns = patterns('',

    url(r'^$', redirect_to,
        {'url': '/admin'},
        name='home'),

    url(r'^favicon\.ico$', redirect_to,
        {'url': '%s/images/favicon.ico' % settings.MEDIA_URL}),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin_tools/', include('admin_tools.urls')),
    #(r'^browse/(.*)', login_required(databrowse.site.root)),

)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    )
