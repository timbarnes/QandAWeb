from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django import forms

from educate.models import Question

# Create your views here.


class AnswerForm(forms.Form):
    """Answer to a specific question
    """
    user_answer = forms.CharField(label='Your answer', max_length=100)

    
def index(request):
    """Lists the questions on a single page.
    """
    latest_question_list = Question.objects.all().order_by('category')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'educate/index.html', context)


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
                      {'question': question, 'answer': 'No answer'})


