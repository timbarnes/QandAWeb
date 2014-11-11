from django.conf.urls import patterns, url

from educate import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'(?P<question_id>\d+)/$', views.ask, name='ask'),
                       url(r'(?P<question_id>\d+)/answer/$', views.answer, name='answer'),
                       )

