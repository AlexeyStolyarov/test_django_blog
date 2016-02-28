from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.home', name='home' ),
	url(r'^add_comment/(?P<arg_parent_id>\d+)$', 'main.views.add_comment2', name='add_comment_url'),
    url(r'^add_comment/(?P<arg_parent_id>\d+)/(?P<arg_comment_id>\d+)?$', 'main.views.add_comment2', name='edit_comment_url'),
    # url(r'^TestBlog/', include('TestBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)


