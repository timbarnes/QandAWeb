from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django import forms
from django.contrib import messages
from django.contrib.auth.models import User

from taggit.models import Tag

from educate.models import Subject, Category, Article
from users.models import Profile, Favorites, Note, Task, TaskList
from users.forms import ProfileForm, UserDataForm, NoteForm, TaskForm


class UserMixin(object):
    def get_context_data(self, **kwargs):
        context = super(UserMixin, self).get_context_data(**kwargs)
        context['authenticated'] = self.request.user.is_authenticated()
        context['username'] = self.request.user.username
        context['user'] = self.request.user
        return context

class ProfileView(UserMixin, generic.TemplateView):
    """View/edit profile data
    """
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        user_form = UserDataForm(instance=context['user'])
        profile = get_object_or_404(Profile, user=context['user'])
        profile_form = ProfileForm(instance=profile)
        user_form.helper.form_action = reverse_lazy('userdataUpdate', args=[context['user'].pk])
        profile_form.helper.form_action = reverse_lazy('profileUpdate', args=[profile.pk])
        context.update({
            'profile': get_object_or_404(Profile, user__username=self.request.user.username),
            'user_form': user_form,
            'profile_form': profile_form,
            })
        return context


class UpdateProfileView(UserMixin, generic.edit.UpdateView):
    """Save updated profile data. Called only with POST.
    """
    model = Profile
    fields = ['picture', 'home', 'interests', 'objectives']
    template_name = 'users/profile.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super(UpdateProfileView, self).get_context_data(**kwargs)
        user_form = UserDataForm(instance=context['user'])
        profile = get_object_or_404(Profile, user=context['user'])
        profile_form = ProfileForm(instance=profile)
        user_form.helper.form_action = reverse_lazy('userdataUpdate', args=[context['user'].pk])
        profile_form.helper.form_action = reverse_lazy('profileUpdate', args=[profile.pk])
        context.update({
            'profile': get_object_or_404(Profile, user__username=self.request.user.username),
            'user_form': user_form,
            'profile_form': profile_form,
            })
        return context


    def form_valid(self, form):
        self.kwargs['form_data']=form.cleaned_data
        messages.success(self.request, 'Profile successfully updated')
        return super(UpdateProfileView, self).form_valid(form)


class UpdateUserDataView(UserMixin, generic.edit.UpdateView):
    """Save updated user data. Called only with POST.
    """
    model = User
    template_name = 'users/profile.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super(UpdateUserDataView, self).get_context_data(**kwargs)
        user_form = UserDataForm(instance=context['user'])
        profile = get_object_or_404(Profile, user=context['user'])
        profile_form = ProfileForm(instance=profile)
        user_form.helper.form_action = reverse_lazy('userdataUpdate', args=[context['user'].pk])
        profile_form.helper.form_action = reverse_lazy('profileUpdate', args=[profile.pk])
        context.update({
            'profile': get_object_or_404(Profile, user__username=self.request.user.username),
            'user_form': user_form,
            'profile_form': profile_form,
            })
        print 'UpdateUserDataView: ', context
        return context

    def form_invalid(self, form):
        print "form invalid", form
        messages.error(self.request, 'User data not successfully updated.')
        return super(UpdateUserDataView, self).form_invalid(form)

    def form_valid(self, form):
        print "Form submitted: ", form
        self.kwargs['form_data']=form.cleaned_data
        messages.success(self.request, 'User data successfully updated')
        return super(UpdateUserDataView, self).form_valid(form)


class MyHomeView(UserMixin, generic.TemplateView):
    """Home page for each user.
    """
    template_name = 'users/myhome.html'

    def get_context_data(self, **kwargs):
        print 'MYHOME'
        context = super(MyHomeView, self).get_context_data(**kwargs)
        user = context['user']
        context.update({
            'profile': get_object_or_404(Profile, user=user),
            'favorites': Favorites.objects.filter(user=user),
            'tasklists': TaskList.objects.filter(user=user),
            'notes': Note.objects.filter(user=user),
            'subject_subset': Subject.objects.filter(author=user),
            'category_subset': Category.objects.filter(author=user),
            'article_subset': Article.objects.filter(author=user),
        })
        print context
        return context

    
class NotesView(UserMixin, generic.FormView):
    """Home page for each user.
    """
    template_name = 'users/notes.html'
    form_class = NoteForm
    success_url = reverse_lazy('notes')

    def get_context_data(self, **kwargs):
        context = super(NotesView, self).get_context_data(**kwargs)
        user = context['user']
        context.update({
            'notes': Note.objects.filter(user=user),
        })
        return context
    

class TaskListsView(UserMixin, generic.FormView):
    """Display task lists.
    """
    template_name = 'users/tasklists.html'
    model = TaskList

    def get_context_data(self, **kwargs):
        context = super(TaskListsView, self).get_context_data(**kwargs)
        user = context['user']
        context.update({
            'task_lists': TaskList.objects.filter(user=user),
            'form': TaskListForm(instance=user),
        })
        return context
    
    
class TasksView(UserMixin, generic.FormView):
    """Display tasks associated with a tasklist.
    """
    template_name = 'users/tasks.html'
    model = Task

    def get_context_data(self, **kwargs):
        context = super(TasksView, self).get_context_data(**kwargs)
        user = context['user']
        context.update({
            'tasks': Task.objects.filter(tasklist__slug=self.kwargs['tasklist']),
            'form': TaskForm(instance=user),
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
            'form': NoteForm(user=user),
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


    
