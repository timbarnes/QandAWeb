from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required

from educate import views

urlpatterns = patterns(
    '',
    url(r'^as/$', views.AllSubjectsView.as_view(), name='all_subjects'),
    url(r'^ac/$', views.AllCategoriesView.as_view(), name='all_categories'),
    url(r'^aa/$', views.AllArticlesView.as_view(), name='all_articles'),
    url(r'^c/(?P<subject>[-_\w]+)/$', views.CategoriesView.as_view(), name='categories'),
    url(r'^ca/(?P<category>[-_\w]+)/$', views.ContentView.as_view(), name='content'),
    url(r'^q/(?P<category>[-_\w]+)/$', views.QuestionsView.as_view(), name='questions'),
    url(r'^q/(?P<category>[-_\w]+)/review/$',
        login_required(views.ReviewQuestionsView.as_view(),
                       login_url='/accounts/login'), name='review_questions'),
    url(r'^tag/(?P<slug>[-\w]+)/$', views.TagIndexView.as_view(), name='tagged'),
    url(r'^(?P<question_id>\d+)/$', views.AskView.as_view(), name='ask'),
    url(r'^(?P<question_id>\d+)/answer/$', views.AnswerView.as_view(), name='answer'),
    url(r'^article/(?P<slug>[-\w]+)/$', views.ArticleView.as_view(), name='article'),
    url(r'^newarticle/$', views.NewArticleView.as_view(), name='new_article'),
    url(r'^newarticle/(?P<category>[-\w]+)/$', views.NewArticleView.as_view(),
        name='new_category_article'),
    url(r'^modarticle/(?P<article>[-\w]+)/$', views.ModArticleView.as_view(),
        name='modify_article'),
)

