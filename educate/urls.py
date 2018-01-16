from django.urls import path
from django.contrib.auth.decorators import login_required

from educate import views

urlpatterns = [
    path('as/', views.AllSubjectsView.as_view(), name='all_subjects'),
    path('ac/', views.AllCategoriesView.as_view(), name='all_categories'),
    path('aa/', views.AllArticlesView.as_view(), name='all_articles'),
    path('c/(<slug:subject>/', views.CategoriesView.as_view(),
         name='categories'),
    path('ca/<slug:category>/', views.ContentView.as_view(), name='content'),
    path('q/<slug:category>/', views.QuestionsView.as_view(),
         name='questions'),
    path('q/<slug:category>/review/',
         login_required(views.ReviewQuestionsView.as_view(),
                        login_url='/accounts/login'), name='review_questions'),
    path('tag/<slug:slug>/', views.TagIndexView.as_view(), name='tagged'),
    path('<int:question_id>/', views.AskView.as_view(), name='ask'),
    path('<int:question_id>/answer/', views.AnswerView.as_view(),
         name='answer'),
    path('article/<slug:slug>/', views.ArticleView.as_view(), name='article'),
    path('newarticle/', views.NewArticleView.as_view(), name='new_article'),
    path('newarticle/(<slug:category>/', views.NewArticleView.as_view(),
         name='new_category_article'),
    path('modarticle/<slug:article>/', views.ModArticleView.as_view(),
         name='modify_article'),
]
