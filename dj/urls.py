from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import admin
from filebrowser.sites import site
from django.contrib.auth.views import login, password_change
from educate import views
from users import forms
from users.views import UserRegistrationView

urlpatterns = patterns(
    '',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^educate/', include('educate.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^pm/', include('pm.urls')),
    url(r'^accounts/register/$', UserRegistrationView.as_view()),
    url(r'^accounts/login/$', login, {'authentication_form': forms.LoginForm}, name='login'),
    url(r'^accounts/change_password/$', password_change,
        {'password_change_form': forms.PasswordForm,
         'template_name': 'registration/password_change.html',
         'post_change_redirect': '/users/profile/',
        'extra_context': {'message': 'Password successfully updated'}},
         name='password_change'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),                       
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
)
