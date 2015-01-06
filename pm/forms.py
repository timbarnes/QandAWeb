from django import forms
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Row, Fieldset, Div
from crispy_forms.bootstrap import FormActions, AppendedText

from models import TaskList, Task, Note


class TaskListForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskListForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_tasklistForm'
        self.helper.form_class = 'blueForms'
        self.helper.layout = Layout(
            'name', 'tags',
            FormActions(Submit('create', 'Create', css_class='btn-primary.btn-block')))

    class Meta:
        model = TaskList
        fields = ['name', 'tags']


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.layout = Layout(
            Fieldset('',
                     'task',
                      AppendedText('resolution', 'Optional')),
            Fieldset('',
                Div('tasklist', css_class='col-xs-4'),
                Div(AppendedText('due', 'Optional'), css_class='col-xs-4'),
                Div('done', css_class='col-xs-2'),
                css_class='row-fluid'),
            FormActions(Submit('submit', 'Submit', css_class='btn-primary.btn-block')))

    class Meta:
        model = Task
        fields = ['tasklist', 'task', 'due', 'done', 'resolution']


class NoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.layout = Layout(
            'title', 'body', 'tags',
            FormActions(Submit('submit', 'Submit', css_class='btn-primary.btn-block')))

    class Meta:
        model = Note
        fields = ['title', 'body', 'tags']
