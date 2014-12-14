from django.conf.urls import patterns, include, url
from django.contrib import admin
from filebrowser.sites import site
from educate import views

urlpatterns = patterns(
    '',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^educate/', include('educate.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),                       
    url(r'^admin/', include(admin.site.urls)),
)
