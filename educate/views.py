from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django import forms
from taggit.models import Tag
from django.contrib.auth.decorators import login_required

from educate.models import Subject, Category, Question, Article
from educate.score import score

# Create your views here.

class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tag_list'] = Tag.objects.all()
        return context
    

class TagIndexView(TagMixin, generic.ListView):
    template_name = 'educate/tags.html'
    model = Category
    context_object_name = 'category_list'

    def get_queryset(self):
        return Category.objects.filter(tags__slug=self.kwargs.get('slug'))
    

def home(request):
    """Home page for the Educate project.
    """
    registered = request.user.is_authenticated()
    return render(request, 'educate/home.html',
                  {
                      'registered': registered,
                      'username': request.user.username,
                      'subject_list': Subject.objects.order_by('name'),
                      'category_list': Category.objects.order_by('name'),
                      'tag_list': Tag.objects.order_by('name'),
                  })

    
class AllArticlesView(TagMixin, generic.ListView):
    """List of all the articles.
    """
    template_name = 'educate/articles.html'
    context_name = 'article_list'

    def get_context_data(self, **kwargs):
        context = super(AllArticlesView, self).get_context_data(**kwargs)
        context.update({
            'registered': self.request.user.is_authenticated(),
            'username': self.request.user.username,
            'category_list': Category.objects.order_by('name'),
            'subject_list': Subject.objects.order_by('name'),
        })
        return context
    
    def get_queryset(self):
        return Article.objects.order_by('category__name', 'title')


class AllSubjectsView(TagMixin, generic.ListView):
    """List of all the subjects.
    """
    template_name = 'educate/subjects.html'
    context_name = 'subject_list'

    def get_context_data(self, **kwargs):
        context = super(AllSubjectsView, self).get_context_data(**kwargs)
        context.update({
            'registered': self.request.user.is_authenticated(),
            'username': self.request.user.username,
            'category_list': Category.objects.order_by('name'),
        })
        return context
    
    def get_queryset(self):
        return Subject.objects.order_by('name')


class AllCategoriesView(TagMixin, generic.ListView):
    """List of all the categories.
    """
    template_name = 'educate/categories.html'
    context_name = 'category_list'

    def get_context_data(self, **kwargs):
        context = super(AllCategoriesView, self).get_context_data(**kwargs)
        context.update({
            'registered': self.request.user.is_authenticated(),
            'username': self.request.user.username,
            'subject_list': Subject.objects.order_by('name'),
            'category_list': Category.objects.order_by('name'),
        })
        return context
    
    def get_queryset(self):
        return Category.objects.order_by('name')


class CategoriesView(TagMixin, generic.ListView):
    """List of the categories for a specific subject.
    """
    template_name = 'educate/categories.html'
    context_object_name = 'category_subset'

    def get_context_data(self, **kwargs):
        context = super(CategoriesView, self).get_context_data(**kwargs)
        context.update({
            'registered': self.request.user.is_authenticated(),
            'username': self.request.user.username,
            'subject': self.kwargs['subject'],
            'subject_list': Subject.objects.order_by('name'),
            'category_list': Category.objects.order_by('name'),
            'article_list': Article.objects.order_by('title'),
        })
        return context
    
    def get_queryset(self):
        return Category.objects.filter(subject__name=self.kwargs['subject'])


class ArticleView(TagMixin, generic.DetailView):
    """Show a single article.
    """
    template_name = 'educate/article.html'
    model = Article
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        context.update({
            'registered':self.request.user.is_authenticated(),
            'username': self.request.user.username,
            'article': get_object_or_404(Article, slug=self.kwargs['slug']),
            'category_list': Category.objects.order_by('name'),
            'article_list': Article.objects.order_by('title'),
        })
        return context
    

class QuestionsView(TagMixin, generic.ListView):
    """List of all the questions in a category.
    """
    template_name = 'educate/questions.html'
    context_object_name = 'question_list'

    def get_context_data(self, **kwargs):
        context = super(QuestionsView, self).get_context_data(**kwargs)
        context.update({
            'registered':self.request.user.is_authenticated(),
            'username': self.request.user.username,
            'category': self.kwargs['category'],
            'subject_list': Subject.objects.order_by('name'),
            'category_list': Category.objects.order_by('name'),
        })
        return context
    
    def get_queryset(self):
        return Question.objects.filter(category__name=self.kwargs['category'])
                

#@login_required
class ReviewQuestionsView(TagMixin, generic.ListView):
    """List of all the questions in a category.
    """
    template_name = 'educate/questions.html'
    context_object_name = 'question_list'

    def get_context_data(self, **kwargs):
        context = super(ReviewQuestionsView, self).get_context_data(**kwargs)
        context.update({
            'registered':self.request.user.is_authenticated(),
            'username': self.request.user.username,
            'category': self.kwargs['category'],
            'subject_list': Subject.objects.order_by('name'),
            'category_list': Category.objects.order_by('name'),
            'review':True,
        })
        return context
    
    def get_queryset(self):
        return Question.objects.filter(category__name=self.kwargs['category'])
                

class AnswerForm(forms.Form):
    """Answer to a specific question
    """
    user_answer = forms.CharField(label='Your answer', max_length=100)


def ask(request, question_id):
    """Ask a single question.
    """
    question = get_object_or_404(Question, pk=question_id)
    form = AnswerForm()
    return render(request, 'educate/ask.html', {
        'registered': request.user.is_authenticated(),
        'username': request.user.username,
        'question': question,
        'form': form,
        'subject_list': Subject.objects.order_by('name'),
        'category_list': Category.objects.order_by('name'),
    })


def answer(request, question_id):
    """Display the answer to a single question.
    """
    question = get_object_or_404(Question, pk=question_id)
    form = AnswerForm(request.POST)
    if form.is_valid():
        sc = score(str(question.answer), form.cleaned_data['user_answer'])
        return render(request, 'educate/answer.html', {
            'registered': request.user.is_authenticated(),
            'username': request.user.username,
            'question': question,
            'answer': form.cleaned_data['user_answer'],
            'score': sc,
            'subject_list': Subject.objects.order_by('name'),
            'category_list': Category.objects.order_by('name'),
        })
    else:
        return render(request, 'educate/answer.html', {
            'registered': request.user.is_authenticated(),
            'username': request.user.username,
            'question': question,
            'answer': '(No answer provided)',
            'score': 0,
            'subject_list': Subject.objects.order_by('name'),
            'category_list': Category.objects.order_by('name'),
        })


