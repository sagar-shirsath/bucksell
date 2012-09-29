from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()
import registration

urlpatterns = patterns('',
    # Examples:
    #    url(r'^$', 'test1.views.home', name='home'),
    # url(r'^test1/', include('test1.foo.urls')),
    url(r'^$','user_profiles.views.home',{},name = "home"),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('user_profiles.urls')),
    url(r'^ads/', include('ads.urls')),
    url(r'^items/', include('items.urls')),
    url(r'^payments/', include('payments.urls')),
    url(r'^universities/', include('universities.urls')),
    (r'^accounts/', include('registration.backends.default.urls')),

)
#
#if settings.DEBUG:
#    urlpatterns += patterns('',
#        url(r'^site_static/(?P<path>.*)$', 'django.views.static.serve', {
#            'document_root': settings.STATIC_ROOT,
#            'show_indexes': True,
#            }),
#    )

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
#        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
