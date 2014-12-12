from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django import forms
from taggit.models import Tag

from educate.models import Subject, Category, Question, Article
from educate.score import score

# Create your views here.

class UserMixin(object):
    def get_context_data(self, **kwargs):
        context = super(UserMixin, self).get_context_data(**kwargs)
        context['authenticated'] = self.request.user.is_authenticated()
        context['username'] = self.request.user.username
        return context
    

class MenuMixin(object):
    def get_context_data(self, **kwargs):
        context = super(MenuMixin, self).get_context_data(**kwargs)
        context['article_list'] = Article.objects.order_by('title')
        context['subject_list'] = Subject.objects.order_by('name')
        context['category_list'] = Category.objects.order_by('name')
        context['tag_list'] = Tag.objects.all()
        return context


class TagIndexView(MenuMixin, UserMixin, generic.ListView):
    """Present everything associated with a tag.
    """
    template_name = 'educate/tags.html'
    context_name = 'tag'
    
    def get_context_data(self, **kwargs):
        context = super(TagIndexView, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']
        context.update({
            'subject_subset': Subject.objects.filter(tags__name__in=[slug]),
            'category_subset': Category.objects.filter(tags__name__in=[slug]),
            'article_subset': Article.objects.filter(tags__name__in=[slug]),
        })
        return context

    def get_queryset(self):
        return get_object_or_404(Tag, slug=self.kwargs['slug'])


class ContentView(MenuMixin, UserMixin, generic.ListView):
    """Present everything associated with a category.
    """
    template_name = 'educate/category.html'
    context_name = ''

    def get_context_data(self, **kwargs):
        context = super(ContentView, self).get_context_data(**kwargs)
        cat = self.kwargs['category']
        context.update({
            'subject': get_object_or_404(Subject, category__slug=cat),
            'category': get_object_or_404(Category, slug=cat),
            'article_subset': Article.objects.filter(category__slug=cat),
            'question_subset': Question.objects.filter(category__slug=cat),
            })
        return context

    def get_queryset(self):
        return 
    

class HomeView(MenuMixin, UserMixin, generic.ListView):
    """Home page for the Educate project.
    """
    template_name = 'educate/home.html'
    context_name = 'context'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return

    
class AllArticlesView(MenuMixin, UserMixin, generic.ListView):
    """List of all the articles.
    """
    template_name = 'educate/articles.html'
    context_name = 'article_list'

    def get_context_data(self, **kwargs):
        context = super(AllArticlesView, self).get_context_data(**kwargs)
        context.update({
            'category_list': Category.objects.order_by('name'),
            'subject_list': Subject.objects.order_by('name'),
        })
        return context
    
    def get_queryset(self):
        return Article.objects.order_by('category__name', 'title')


class AllSubjectsView(MenuMixin, UserMixin, generic.ListView):
    """List of all the subjects.
    """
    template_name = 'educate/subjects.html'
    context_name = 'subject_list'

    def get_context_data(self, **kwargs):
        context = super(AllSubjectsView, self).get_context_data(**kwargs)
        context.update({
            'category_list': Category.objects.order_by('name'),
        })
        return context
    
    def get_queryset(self):
        return Subject.objects.order_by('name')


class AllCategoriesView(MenuMixin, UserMixin, generic.ListView):
    """List of all the categories.
    """
    template_name = 'educate/categories.html'
    context_name = 'category_list'

    def get_context_data(self, **kwargs):
        context = super(AllCategoriesView, self).get_context_data(**kwargs)
        context.update({
            'subject_list': Subject.objects.order_by('name'),
            'category_list': Category.objects.order_by('name'),
        })
        return context
    
    def get_queryset(self):
        return Category.objects.order_by('name')


class CategoriesView(MenuMixin, UserMixin, generic.ListView):
    """List of the categories for a specific subject.
    """
    template_name = 'educate/categories.html'
    context_object_name = 'category_subset'

    def get_context_data(self, **kwargs):
        context = super(CategoriesView, self).get_context_data(**kwargs)
        context.update({
            'subject': get_object_or_404(Subject, slug=self.kwargs['subject']),
        })
        return context
    
    def get_queryset(self):
        return Category.objects.filter(subject__slug=self.kwargs['subject'])


class ArticleView(MenuMixin, UserMixin, generic.DetailView):
    """Show a single article.
    """
    template_name = 'educate/article.html'
    model = Article
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        context.update({
            'article': get_object_or_404(Article, slug=self.kwargs['slug']),
        })
        return context
    

class QuestionsView(MenuMixin, UserMixin, generic.ListView):
    """List of all the questions in a category.
    """
    template_name = 'educate/questions.html'
    context_object_name = 'question_list'

    def get_context_data(self, **kwargs):
        context = super(QuestionsView, self).get_context_data(**kwargs)
        context.update({
            'category': get_object_or_404(Category, slug=self.kwargs['category']),
        })
        return context
    
    def get_queryset(self):
        return Question.objects.filter(category__name=self.kwargs['category'])
                

class ReviewQuestionsView(MenuMixin, UserMixin, generic.ListView):
    """List of all the questions in a category.
    """
    template_name = 'educate/questions.html'
    context_object_name = 'question_list'

    def get_context_data(self, **kwargs):
        context = super(ReviewQuestionsView, self).get_context_data(**kwargs)
        context.update({
            'category': self.kwargs['category'],
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
        'tag_list': Tag.objects.order_by('name'),
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


