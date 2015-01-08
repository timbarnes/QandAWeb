from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.text import slugify
from django.views import generic
from django import forms
from django.contrib import messages
from django.dispatch import receiver
from django.contrib.auth.models import User

from taggit.models import Tag

from pm.models import Note, Task, TaskList, Project
from pm.forms import TaskListForm, NoteForm, TaskForm, ProjectForm


class ProjectsView(generic.FormView):
    """Projects home page.
    """
    template_name = 'pm/projects.html'
    form_class = ProjectForm
    success_url = reverse_lazy('projects')

    def get_context_data(self, **kwargs):
        context = super(ProjectsView, self).get_context_data(**kwargs)
        context.update({
            'projects': Project.objects.filter(user=self.request.user),
            'form': ProjectForm({'user': self.request.user, 'slug':'-',}),
        })
        return context

    def form_invalid(self, form):
        print form
        return super(ProjectsView, self).form_invalid(form)

    def form_valid(self, form):
        p = form.save(commit=False)
        p.user = self.request.user
        p.slug = slugify(form.cleaned_data['name'])
        p.save()
        form.save_m2m()
        messages.success(self.request, 'Project created')
        return super(ProjectsView, self).form_valid(form)


class ProjectView(generic.DetailView):
    """Content of a single project.
    """
    template_name = 'pm/project.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        context.update({
            'tasklists': TaskList.objects.filter(project__slug=self.kwargs['slug']),
            'notes': Note.objects.filter(project__slug=self.kwargs['slug']),
            })
        return context


class EditProjectView(generic.UpdateView):
    """Update an existing project
    """
    template_name = 'pm/editproject.html'
    model = Project

    
class NotesView(generic.FormView):
    """List of all notes.
    """
    template_name = 'pm/notes.html'
    form_class = NoteForm
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('notes', args=[self.kwargs['project']])

    def get_context_data(self, **kwargs):
        context = super(NotesView, self).get_context_data(**kwargs)
        context.update({
            'notes': Note.objects.filter(project__pk=self.kwargs['project']),
            'project': get_object_or_404(Project, pk=self.kwargs['project']),
        })
        return context
    
    def form_valid(self, form):
        print "Form submitted: ", form
        self.kwargs['form_data']=form.cleaned_data
        n = form.save(commit=False)
        n.project = get_object_or_404(Project, pk=self.kwargs['project'])
        n.slug = slugify(form.cleaned_data['title'])
        n.save()
        form.save_m2m()
        messages.success(self.request, 'Note saved')
        return super(NotesView, self).form_valid(form)


class TaskListsView(generic.FormView):
    """Display task lists for a specific project specified by pk
    """
    template_name = 'pm/tasklists.html'
    form_class = TaskListForm
    success_url = '.'

    def get_context_data(self, **kwargs):
        context = super(TaskListsView, self).get_context_data(**kwargs)
        context.update({
            'task_lists': TaskList.objects.filter(project__pk=self.kwargs['pk']),
        })
        return context
    
    def form_valid(self, form):
        t = form.save(commit=False)
        t.project = get_object_or_404(Project, pk=self.kwargs['pk'])
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
            'taskslists': TaskList.objects.filter(project__slug=self.kwargs['slug']),
            'tasklist': get_object_or_404(TaskList, slug=self.kwargs['slug']),
            'tasks': Task.objects.filter(tasklist__slug=self.kwargs['slug']).order_by('done'),
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
            'form': NoteForm(project=self.kwargs['slug']),
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
