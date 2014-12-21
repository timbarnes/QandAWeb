from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django import forms

from taggit.models import Tag

from users.models import Profile, Favorites, Note, Task, TaskList
from users.forms import TemplateForm, NoteForm, TaskForm

class UserMixin(object):
    def get_context_data(self, **kwargs):
        context = super(UserMixin, self).get_context_data(**kwargs)
        context['authenticated'] = self.request.user.is_authenticated()
        context['username'] = self.request.user.username
        context['user'] = self.request.user
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
            'profile': get_object_or_404(Profile, user__username=self.request.user.username),
            })
        return context

    def form_valid(self, form):
        print "Form: ", form
        self.kwargs['form_data']=form.cleaned_data
        return super(ProfileView, self).form_valid(form)


class MyHomeView(UserMixin, generic.TemplateView):
    """Home page for each user.
    """
    template_name = 'users/myhome.html'

    def get_context_data(self, **kwargs):
        context = super(MyHomeView, self).get_context_data(**kwargs)
        context.update({
            'profile': get_object_or_404(Profile, slug=self.kwargs['slug']),
        })
        return context

    
class NewNoteView(UserMixin, generic.FormView):
    """Add a note.
    """
    template_name = 'users/newnote.html'


    def get_context_data(self, **kwargs):
        context = super(NewNoteView, self).get_context_data(**kwargs)
        context.update({
            'profile': get_object_or_404(Profile, slug=self.kwargs['slug']),
        })
        return context


class NewTaskView(UserMixin, generic.FormView):
    """Add a note.
    """
    template_name = 'users/newtask.html'


    def get_context_data(self, **kwargs):
        context = super(NewTaskView, self).get_context_data(**kwargs)
        context.update({
            'profile': get_object_or_404(Profile, slug=self.kwargs['slug']),
        })
        return context


class NoteView(UserMixin, generic.TemplateView):
    """Display user notes.
    """
    template_name = 'users/note.html'


    def get_context_data(self, **kwargs):
        context = super(NoteView, self).get_context_data(**kwargs)
        context.update({
            'profile': get_object_or_404(Profile, slug=self.kwargs['slug']),
        })
        return context


class TaskView(UserMixin, generic.TemplateView):
    """Display a user task.
    """
    template_name = 'users/task.html'


    def get_context_data(self, **kwargs):
        context = super(TaskView, self).get_context_data(**kwargs)
        context.update({
            'profile': get_object_or_404(Profile, slug=self.kwargs['slug']),
        })
        return context


    
