from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django import forms

from educate.models import Category, Question

# Create your views here.


class AnswerForm(forms.Form):
    """Answer to a specific question
    """
    user_answer = forms.CharField(label='Your answer', max_length=100)


def home(request):
    """Home page for the Educate project.
    """
    return render(request, 'educate/home.html')

    
class CategoriesView(generic.ListView):
    """List of all the categories.
    """
    template_name = 'educate/categories.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        return Category.objects.order_by('category_text')

class QuestionsView(generic.ListView):
    """List of all the questions in a category.
    """
    template_name = 'educate/questions.html'
    context_object_name = 'questions'

    def get_queryset(self):
        cat = self.kwargs['category']
        print 'Category was:', cat
        print Question.objects.filter(category__category_text=cat)
        return Question.objects.filter(category__category_text=cat)
                

def ask(request, question_id):
    """Ask a single question.
    """
    question = get_object_or_404(Question, pk=question_id)
    form = AnswerForm()
    return render(request, 'educate/ask.html', {'question': question, 'form': form})


def answer(request, question_id):
    """Display the answer to a single question.
    """
    question = get_object_or_404(Question, pk=question_id)
    form = AnswerForm(request.POST)
    if form.is_valid():
        return render(request, 'educate/answer.html',
                      {'question': question, 'answer': form.cleaned_data['user_answer']})
    else:
        return render(request, 'educate/answer.html',
                      {'question': question, 'answer': '(No answer provided)'})


