from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('zoe.posts.views',
    url(r'^$', 'post_list'),
    url(r'^(?P<slug>[\w-]+)/$', 'post_detail'),
)
