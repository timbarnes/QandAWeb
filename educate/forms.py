from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Field
from crispy_forms.bootstrap import FormActions

from models import Subject, Category, Article
        

class AnswerForm(forms.Form):
    """Answer to a specific question
    """
    user_answer = forms.CharField(
        label = 'Enter your answer:',
        )

    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.form_id = 'user_answer'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'get'
        self.helper.form_action = 'answer/'
        self.helper.add_input(Submit('submit', 'Submit your answer'))
        

class SubjectForm(forms.ModelForm):
    """Add a new subject.
    """

    def __init__(self, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.layout = Layout(
            'name', 'description', 'public',
            Field('author', type='hidden'),
            FormActions(Submit('create', 'Create', css_class='btn-primary.btn-block')))

    class Meta:
        model = Subject
        fields = ['name', 'description', 'author', 'public']
