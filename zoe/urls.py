from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zoe.views.home', name='home'),
    # url(r'^zoe/', include('zoe.foo.urls')),
    url(r'^posts/', include('zoe.posts.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        )
