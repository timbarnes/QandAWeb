from django.urls import path, re_path
from django.contrib.auth.decorators import login_required

from educate import views

urlpatterns = [
    path(r'as/', views.AllSubjectsView.as_view(), name='all_subjects'),
    path(r'ac/', views.AllCategoriesView.as_view(), name='all_categories'),
    path(r'aa/', views.AllArticlesView.as_view(), name='all_articles'),
    re_path(r'c/(?P<subject>[-_\w]+)/', views.CategoriesView.as_view(), name='categories'),
    re_path(r'ca/(?P<category>[-_\w]+)/', views.ContentView.as_view(), name='content'),
    re_path(r'q/(?P<category>[-_\w]+)/', views.QuestionsView.as_view(), name='questions'),
    re_path(r'q/(?P<category>[-_\w]+)/review/',
        login_required(views.ReviewQuestionsView.as_view(),
                       login_url='/accounts/login'), name='review_questions'),
    re_path(r'tag/(?P<slug>[-\w]+)/', views.TagIndexView.as_view(), name='tagged'),
    re_path(r'(?P<question_id>\d+)/', views.AskView.as_view(), name='ask'),
    re_path(r'(?P<question_id>\d+)/answer/', views.AnswerView.as_view(), name='answer'),
    re_path(r'article/(?P<slug>[-\w]+)/', views.ArticleView.as_view(), name='article'),
    re_path(r'newarticle/', views.NewArticleView.as_view(), name='new_article'),
    re_path(r'newarticle/(?P<category>[-\w]+)/', views.NewArticleView.as_view(),
        name='new_category_article'),
    re_path(r'modarticle/(?P<article>[-\w]+)/', views.ModArticleView.as_view(),
        name='modify_article'),
]
