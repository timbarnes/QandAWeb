from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.db.models import Q
from django.contrib import messages
from django.utils.text import slugify
from django import forms
from taggit.models import Tag
from braces import views

from educate.forms import AnswerForm, SubjectForm, CategoryForm, ArticleForm
from educate.models import Subject, Category, Question, Article
from educate.score import score


class MenuMixin(object):
    """Gets public articles, subjects and categories. All tags are public.
    """
    def get_context_data(self, **kwargs):
        context = super(MenuMixin, self).get_context_data(**kwargs)
        context['article_list'] = Article.objects.filter(public=True)
        context['subject_list'] = Subject.objects.filter(public=True)
        context['category_list'] = Category.objects.filter(public=True)
        context['tag_list'] = Tag.objects.all()
        return context


class TagIndexView(MenuMixin, generic.TemplateView):
    """Present everything associated with a tag.
    """
    template_name = 'educate/tags.html'
    
    def get_context_data(self, **kwargs):
        context = super(TagIndexView, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']
        context.update({
            'tag': get_object_or_404(Tag, slug=slug),
            'subject_subset': Subject.objects.filter(tags__name__in=[slug]),
            'category_subset': Category.objects.filter(tags__name__in=[slug]),
            'article_subset': Article.objects.filter(tags__name__in=[slug]),
        })
        return context

    def get_queryset(self):
        return get_object_or_404(Tag, slug=self.kwargs['slug'])


class ContentView(MenuMixin, generic.ListView):
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
    

class HomeView(MenuMixin, generic.TemplateView):
    """Home page for the Educate project.
    """
    template_name = 'educate/home.html'

    
class AllArticlesView(MenuMixin, generic.ListView):
    """List of all the public articles.
    """
    template_name = 'educate/articles.html'
    context_name = 'article_list'

    def get_queryset(self):
        return Article.objects.order_by('category__name', 'title')


class AllSubjectsView(MenuMixin, generic.FormView):
    """List of all the subjects.
    """
    template_name = 'educate/subjects.html'
    form_class = SubjectForm
    success_url = '.'

    def get_context_data(self, **kwargs):
        context = super(AllSubjectsView, self).get_context_data(**kwargs)
        context.update({
            'form': SubjectForm(initial={'author': self.request.user, 'public': False}),
            'subject_list': Subject.objects.order_by('name').filter(public=True),
        })
        return context
    
    def form_valid(self, form):
        self.kwargs['form_data']=form.cleaned_data
        n=form.save(commit=False)
        n.slug = slugify(form.cleaned_data['name'])
        n.save()
        form.save_m2m()
        messages.success(self.request, 'Subject created')
        return super(AllSubjectsView, self).form_valid(form)


class AllCategoriesView(MenuMixin, generic.TemplateView):
    """List of all the categories.
    """
    template_name = 'educate/categories.html'

    def get_context_data(self, **kwargs):
        context = super(AllCategoriesView, self).get_context_data(**kwargs)
        context.update({
            'subject_list': Subject.objects.order_by('name'),
            'category_list': Category.objects.order_by('name').filter(public=True),
        })
        return context
    

class CategoriesView(MenuMixin, generic.FormView):
    """List of the categories for a specific subject.
       Enables creation of new category for that subject.
    """
    template_name = 'educate/categories.html'
    form_class = CategoryForm
    success_url = '.'

    def get_context_data(self, **kwargs):
        context = super(CategoriesView, self).get_context_data(**kwargs)
        context.update({
            'subject': get_object_or_404(Subject, slug=self.kwargs['subject']),
            'category_subset': Category.objects.filter(subject__slug=self.kwargs['subject']),
            'form': CategoryForm(initial={'author': self.request.user, 'public': False})
        })
        return context

    def form_invalid(self, form):
        messages.error(self.request, 'Error: please try again')
        return super(CategoriesView, self).form_invalid(form)

    def form_valid(self, form):
        self.kwargs['form_data']=form.cleaned_data
        n=form.save(commit=False)
        n.subject = get_object_or_404(Subject, slug=self.kwargs['subject'])
        n.slug = slugify(form.cleaned_data['name'])
        n.save()
        form.save_m2m()
        messages.success(self.request, 'Category created')
        return super(CategoriesView, self).form_valid(form)


class ArticleView(MenuMixin, generic.DetailView):
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
    

class NewArticleView(MenuMixin, generic.CreateView):
    """Create a new article.
    """
    model = Article
    form_class = ArticleForm
    template_name = 'educate/modarticle.html'
    success_url = reverse_lazy('all_articles')

    def get_initial(self):
        return {'author': self.request.user, 'slug':'temp_slug'}

    def form_invalid(self, form):
        messages.error(self.request, 'Error: please try again')
        print form
        return super(NewArticleView, self).form_invalid(form)
        
    def form_valid(self, form):
        a = form.save(commit=False)
        a.slug = slugify(form.cleaned_data['title'])
        a.save()
        form.save_m2m()
        messages.success(self.request, 'Article created.')
        return super(NewArticleView, self).form_valid(form)


class ModArticleView(MenuMixin, generic.UpdateView):
    """Modify an existing article.
    """
    template_name = 'educate/modarticle.html'
    form_class = ArticleForm


class QuestionsView(MenuMixin, generic.ListView):
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
        return Question.objects.filter(category__slug=self.kwargs['category'])
                

class ReviewQuestionsView(MenuMixin, generic.ListView):
    """List of all the questions in a category.
    """
    template_name = 'educate/questions.html'
    context_object_name = 'question_list'

    def get_context_data(self, **kwargs):
        context = super(ReviewQuestionsView, self).get_context_data(**kwargs)
        context.update({
            'category': get_object_or_404(Category, slug=self.kwargs['category']),
            'review': True,
        })
        return context
    
    def get_queryset(self):
        return Question.objects.filter(category__slug=self.kwargs['category'])


class AskView(MenuMixin, generic.FormView):
    """Ask a single question.
    """
    form_class = AnswerForm
    success_url = reverse_lazy('answer')
    template_name = 'educate/ask.html'

    def get_context_data(self, **kwargs):
        context = super(AskView, self).get_context_data(**kwargs)
        context.update({
            'question': get_object_or_404(Question, pk=self.kwargs['question_id'])
            })
        return context

    def form_valid(self, form):
        self.kwargs['user_answer'] = form.cleaned_data['user_answer']
        return super(AskView, self).form_valid(form)
        

class AnswerView(MenuMixin, generic.TemplateView):
    """Display the answer to a single question.
    """
    template_name = 'educate/answer.html'

    def get_context_data(self, **kwargs):
        context = super(AnswerView, self).get_context_data(**kwargs)
        context.update({
            'question': get_object_or_404(Question, pk=self.kwargs['question_id']),
            'answer': self.request.GET['user_answer'],
            })
        return context
        


    

