from django.conf.urls import patterns, url, include
from educate import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^as/$', views.AllSubjectsView.as_view(), name='all_subjects'),
    url(r'^ac/$', views.AllCategoriesView.as_view(), name='all_categories'),
    url(r'^aa/$', views.AllArticlesView.as_view(), name='all_articles'),
    url(r'^c/(?P<subject>[-_\w]+)/$', views.CategoriesView.as_view(), name='categories'),
    url(r'^ca/(?P<category>[-_\w]+)/$', views.contentview, name='content'),
    url(r'^q/(?P<category>[-_\w]+)/$', views.QuestionsView.as_view(), name='questions'),
    url(r'^q/(?P<category>[-_\w]+)/review/$', views.ReviewQuestionsView.as_view(), name='review_questions'),
    url(r'^tag/(?P<slug>[-\w]+)/$', views.tagindexview, name='tagged'),
    url(r'^(?P<question_id>\d+)/$', views.ask, name='ask'),
    url(r'^(?P<question_id>\d+)/answer/$', views.answer, name='answer'),
    url(r'^article/(?P<slug>[-\w]+)/$', views.ArticleView.as_view(), name='article'),
)

