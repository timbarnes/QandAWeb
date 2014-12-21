from django.conf.urls import patterns, include, url
from django.contrib import admin
from filebrowser.sites import site
from registration.views import RegistrationView
from django.contrib.auth.views import login
from educate import forms
from educate import views

urlpatterns = patterns(
    '',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^educate/', include('educate.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^accounts/register/$', RegistrationView.as_view(form_class=forms.RegistrationForm)),
    url(r'^accounts/login/$', login, {'authentication_form': forms.LoginForm}, name='login'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),                       
    url(r'^admin/', include(admin.site.urls)),
)
