from django.conf.urls import patterns, url, include
from educate import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^as/$', views.AllSubjectsView.as_view(), name='all_subjects'),
    url(r'^ac/$', views.AllCategoriesView.as_view(), name='all_categories'),
    url(r'^c/(?P<subject>[a-zA-Z%:,\- \d]+)/$', views.CategoriesView.as_view(), name='categories'),
    url(r'^q/(?P<category>[a-zA-Z%:,\- \d]+)/$', views.QuestionsView.as_view(), name='questions'),
    url(r'^q/(?P<category>[a-zA-Z%:,\- \d]+)/review/$', views.ReviewQuestionsView.as_view(), name='review_questions'),
    url(r'^(?P<question_id>\d+)/$', views.ask, name='ask'),
    url(r'^(?P<question_id>\d+)/answer/$', views.answer, name='answer'),
    url(r'^accounts/', include('registration.backends.default.urls')),
)

