from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django import forms

from educate.models import Subject, Category, Question
from educate.score import score

# Create your views here.


class AnswerForm(forms.Form):
    """Answer to a specific question
    """
    user_answer = forms.CharField(label='Your answer', max_length=100)


def home(request):
    """Home page for the Educate project.
    """
    return render(request, 'educate/home.html',
                  {'subject_list': Subject.objects.order_by('name'),
                   'category_list': Category.objects.order_by('name')
               })

    
class AllSubjectsView(generic.ListView):
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


class AllCategoriesView(generic.ListView):
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


class CategoriesView(generic.ListView):
    """List of the categories for a specific subject.
    """
    template_name = 'educate/categories.html'
    context_object_name = 'category_subset'

    def get_context_data(self, **kwargs):
        context = super(CategoriesView, self).get_context_data(**kwargs)
        context.update({
            'subject': self.kwargs['subject'],
            'subject_list': Subject.objects.order_by('name'),
            'category_list': Category.objects.order_by('name'),
        })
        return context
    
    def get_queryset(self):
        return Category.objects.filter(subject__name=self.kwargs['subject'])


class QuestionsView(generic.ListView):
    """List of all the questions in a category.
    """
    template_name = 'educate/questions.html'
    context_object_name = 'question_list'

    def get_context_data(self, **kwargs):
        context = super(QuestionsView, self).get_context_data(**kwargs)
        context.update({
            'category': self.kwargs['category'],
            'subject_list': Subject.objects.order_by('name'),
            'category_list': Category.objects.order_by('name'),
        })
        return context
    
    def get_queryset(self):
        return Question.objects.filter(category__name=self.kwargs['category'])
                

class ReviewQuestionsView(generic.ListView):
    """List of all the questions in a category.
    """
    template_name = 'educate/questions.html'
    context_object_name = 'question_list'

    def get_context_data(self, **kwargs):
        context = super(ReviewQuestionsView, self).get_context_data(**kwargs)
        context.update({
            'category': self.kwargs['category'],
            'subject_list': Subject.objects.order_by('name'),
            'category_list': Category.objects.order_by('name'),
            'review':True,
        })
        return context
    
    def get_queryset(self):
        return Question.objects.filter(category__name=self.kwargs['category'])
                

def ask(request, question_id):
    """Ask a single question.
    """
    question = get_object_or_404(Question, pk=question_id)
    form = AnswerForm()
    return render(request, 'educate/ask.html', {
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
            'question': question,
            'answer': form.cleaned_data['user_answer'],
            'score': sc,
            'subject_list': Subject.objects.order_by('name'),
            'category_list': Category.objects.order_by('name'),
        })
    else:
        return render(request, 'educate/answer.html', {
            'question': question,
            'answer': '(No answer provided)',
            'score': 0,
            'subject_list': Subject.objects.order_by('name'),
            'category_list': Category.objects.order_by('name'),
        })

