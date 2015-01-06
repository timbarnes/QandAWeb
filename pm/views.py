from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.text import slugify
from django.views import generic
from django import forms
from django.contrib import messages
from django.dispatch import receiver
from django.contrib.auth.models import User

from taggit.models import Tag

from pm.models import Note, Task, TaskList
from pm.forms import TaskListForm, NoteForm, TaskForm


class ProjectsView(generic.TemplateView):
    """Projects home page.
    """
    template_name = 'pm/projects.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectsView, self).get_context_data(**kwargs)
        context.update({
            'profile': get_object_or_404(Profile, user=self.request.user),
            'favorites': Favorites.objects.filter(user=self.request.user),
            'tasklists': TaskList.objects.filter(user=self.request.user),
            'notes': Note.objects.filter(user=self.request.user),
            'subject_subset': Subject.objects.filter(author=self.request.user),
            'category_subset': Category.objects.filter(author=self.request.user),
            'article_subset': Article.objects.filter(author=self.request.user),
        })
        print context
        return context

    
class NotesView(generic.FormView):
    """Home page for each user.
    """
    template_name = 'pm/notes.html'
    form_class = NoteForm
    success_url = reverse_lazy('notes')

    def get_context_data(self, **kwargs):
        context = super(NotesView, self).get_context_data(**kwargs)
        context.update({
            'notes': Note.objects.filter(user=self.request.user),
        })
        return context
    
    def form_valid(self, form):
        print "Form submitted: ", form
        self.kwargs['form_data']=form.cleaned_data
        n = form.save(commit=False)
        n.user = self.request.user
        n.slug = slugify(form.cleaned_data['title'])
        n.save()
        form.save_m2m()
        messages.success(self.request, 'Note saved')
        return super(NotesView, self).form_valid(form)


class TaskListsView(generic.FormView):
    """Display task lists.
    """
    template_name = 'pm/tasklists.html'
    form_class = TaskListForm
    success_url = reverse_lazy('taskLists')

    def get_context_data(self, **kwargs):
        context = super(TaskListsView, self).get_context_data(**kwargs)
        context.update({
            'task_lists': TaskList.objects.filter(user=self.request.user),
        })
        return context
    
    def form_valid(self, form):
        print "Form submitted: ", form
        self.kwargs['form_data']=form.cleaned_data
        t = form.save(commit=False)
        t.user = self.request.user
        t.slug = slugify(form.cleaned_data['name'])
        t.save()
        form.save_m2m()
        messages.success(self.request, 'Task list created')
        return super(TaskListsView, self).form_valid(form)

    
class TasksView(generic.TemplateView):
    """Display tasks associated with a tasklist.
    """
    template_name = 'pm/tasks.html'

    def get_context_data(self, **kwargs):
        context = super(TasksView, self).get_context_data(**kwargs)
        context.update({
            'taskslists': TaskList.objects.filter(user=self.request.user),
            'tasklist': get_object_or_404(TaskList, slug=self.kwargs['slug']),
            'tasks': Task.objects.filter(tasklist__slug=self.kwargs['slug']).order_by('done'),
            'tasklists': TaskList.objects.filter(user=self.request.user),
        })
        return context

    
class NewNoteView(generic.CreateView):
    """Add a note.
    """
    template_name = 'pm/newnote.html'
    model = Note

    def get_context_data(self, **kwargs):
        context = super(NewNoteView, self).get_context_data(**kwargs)
        context.update({
            'form': NoteForm(user=self.request.user),
        })
        return context


class NewTaskView(generic.CreateView):
    """Add a task to an existing tasklist.
    """
    template_name = 'pm/newtask.html'
    model = Task

    def get_success_url(self, **kwargs):
        return reverse('tasks', args=[self.object.tasklist.slug])

    def get_context_data(self, **kwargs):
        context = super(NewTaskView, self).get_context_data(**kwargs)
        tlist = get_object_or_404(TaskList, slug=self.kwargs['slug'])
        context.update({
            'tasklist': tlist,
            'form': TaskForm({'tasklist': tlist.pk, }),
        })
        return context

    def form_valid(self, form):
        if not form.cleaned_data['due']:
            form.cleaned_data['due'] = None
        messages.success(self.request, 'Task created.')
        return super(NewTaskView, self).form_valid(form)
    

class NoteView(generic.UpdateView):
    """Alter an existing user note.
    """
    template_name = 'pm/note.html'
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy('notes')


class TaskView(generic.UpdateView):
    """Alter an existing user task.
    """
    template_name = 'pm/task.html'
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse('tasks', args=[self.object.tasklist.slug])
