from django import forms
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import FormActions

from models import Profile


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
            FormActions(Submit('register', 'Register', css_class='btn-primary.btn-block'))
            )
        super(RegistrationForm, self).__init__(*args, **kwargs)
        

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_loginForm'
        self.helper.form_class = 'blueForms'
        self.helper.layout = Layout(
            'username',
            'password',
            FormActions(Submit('login', 'Login', css_class='btn-primary.btn-block'))
            )
        super(LoginForm, self).__init__(*args, **kwargs)


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_profileForm'
        self.helper.form_class = 'blueForms'
        self.helper.layout = Layout(
            'picture',
            'home',
            'interests',
            'objectives',
            FormActions(Submit('update', 'Update', css_class='btn-primary.btn-block')))

    class Meta:
        model = Profile
        fields = ['picture', 'home', 'interests', 'objectives']


class UserDataForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserDataForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_userdataForm'
        self.helper.form_class = 'blueForms'
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            FormActions(Submit('update', 'Update', css_class='btn-primary.btn-block')))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class TaskForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_noteForm'
        self.helper.form_class = 'blueForms'
        super(forms.Form, self).__init__(*args, **kwargs)


class NoteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_noteForm'
        self.helper.form_class = 'blueForms'
        super(forms.Form, self).__init__(*args, **kwargs)

        
