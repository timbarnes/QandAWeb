from django.conf.urls import patterns, include, url
from django.contrib import admin
from filebrowser.sites import site

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quanda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^educate/', include('educate.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),                       
    url(r'^admin/', include(admin.site.urls)),
)
