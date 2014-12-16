from django.contrib.auth.forms import UserCreationForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit

class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_registrationForm'
        self.helper.form_class = 'blueForms'
        self.helper.layout = Layout(
            'username',
            'password1',
            'password2',
            ButtonHolder(Submit('register', 'Register', css_class='btn-primary.btn-block'))
            )
        super(RegistrationForm, self).__init__(*args, **kwargs)
        

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
        

