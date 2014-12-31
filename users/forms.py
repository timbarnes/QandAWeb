from django import forms
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from crispy_forms.bootstrap import FormActions

from models import Profile, TaskList, Task, Note


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


class PasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_passwordForm'
        self.helper.form_class = 'blueForms'
        self.helper.layout = Layout(
            'old_password',
            'new_password1',
            'new_password2',
            FormActions(Submit('update', 'Update', css_class='btn-primary.btn-block'))
            )
        super(PasswordForm, self).__init__(*args, **kwargs)


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
            'username',
             Field('password', type='hidden'),
             Field('date_joined', type='hidden'),
             Field('last_login', type='hidden'),
            'first_name',
            'last_name',
            'email',
            FormActions(Submit('update', 'Update', css_class='btn-primary.btn-block')))

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name',
                  'email', 'date_joined', 'last_login']

        
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
            'tasklist', 'task', 'due',
            FormActions(Submit('create', 'Create', css_class='btn-primary.btn-block')))

    class Meta:
        model = Task
        fields = ['tasklist', 'task', 'due']


class NoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_noteForm'
        self.helper.form_class = 'blueForms'
        self.helper.layout = Layout(
            'title', 'body', 'tags',
            FormActions(Submit('create', 'Create', css_class='btn-primary.btn-block')))

    class Meta:
        model = Note
        fields = ['title', 'body', 'tags']
