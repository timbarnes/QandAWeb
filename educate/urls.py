from django.conf.urls import patterns, url

from educate import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^categories/$', views.CategoriesView.as_view(), name='categories'),
    url(r'^categories/(?P<category>[a-zA-Z d]+)/$', views.QuestionsView.as_view(), name='questions'),
    url(r'^(?P<question_id>\d+)/$', views.ask, name='ask'),
    url(r'^(?P<question_id>\d+)/answer/$', views.answer, name='answer'),
)

