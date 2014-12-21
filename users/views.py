from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django import forms

from taggit.models import Tag

from users.models import Profile, Favories, Personal, Note, Task, TaskList
from users.forms import TemplateForm, NoteForm, TaskForm

class UserMixin(object):
    def get_context_data(self, **kwargs):
        context = super(UserMixin, self).get_context_data(**kwargs)
        context['authenticated'] = self.request.user.is_authenticated()
        context['username'] = self.request.user.username
        return context

class ProfileView(UserMixin, generic.FormView):
    """View/edit profile data
    """
    template_name = 'users/profile.html'
    form_class = TemplateForm
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context.update({
            'profile': get_object_or_404(Profile, slug=self.kwargs['slug']),
            })

    def form_valid(self, form):
        self.kwargs['form_data']=form.cleaned_data
        return super(ProfileView, self).form_valid(form)
