from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit

from models import Profile

class TemplateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_templateForm'
        self.helper.form_class = 'blueForms'
        self.helper.layout = Layout(
            'picture'
            'home',
            'interests',
            'objectives',
            ButtonHolder(Submit('update', 'Update', css_class='btn-primary.btn-block')))

    class Meta:
        model = Profile
        fields = ['picture', 'home', 'interests', 'objectives']


class TaskForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_noteForm'
        self.helper.form_class = 'blueForms'
        super(forms.Form, self).__init__(*args, **kwargs)


class NoteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_noteForm'
        self.helper.form_class = 'blueForms'
        super(forms.Form, self).__init__(*args, **kwargs)

        
