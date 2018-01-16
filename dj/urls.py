from django.urls import include, path
from django.contrib import admin
from django.contrib.auth.views import login, password_change
from educate import views
from users import forms
from users.views import UserRegistrationView

urlpatterns = [
    path(r'', views.HomeView.as_view(), name='home'),
    path(r'educate/', include('educate.urls')),
    path(r'users/', include('users.urls')),
    path(r'accounts/register/', UserRegistrationView.as_view()),
    path(r'accounts/login/', login, {'authentication_form': forms.LoginForm},
         name='login'),
    path(r'accounts/change_password/', password_change,
         {'password_change_form': forms.PasswordForm,
          'template_name': 'registration/password_change.html',
          'post_change_redirect': '/users/profile/',
          'extra_context': {'message': 'Password successfully updated'}},
         name='password_change'),
    path(r'accounts/', include('registration.backends.default.urls')),
    path(r'tinymce/', include('tinymce.urls')),
#    path(r'^admin/filebrowser/', include(site.urls)),
#    path(r'^grappelli/', include('grappelli.urls')),
    path(r'admin/', admin.site.urls),
]
