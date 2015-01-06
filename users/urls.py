from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required

from users import views
from users import forms

urlpatterns = patterns(
    '',
    url(r'^myhome/$', views.MyHomeView.as_view(), name='myHome'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^profile/p/(?P<pk>\d+)/$', views.UpdateProfileView.as_view(), name='profileUpdate'),
    url(r'^profile/u/(?P<pk>\d+)/$', views.UpdateUserDataView.as_view(), name='userdataUpdate'),
)

