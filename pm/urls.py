from django.conf.urls import patterns, url, include

from pm import views
from pm import forms

urlpatterns = patterns(
    '',
    url(r'^projects/$', # All projects
        views.ProjectsView.as_view(), name='projects'),
    url(r'^project/(?P<slug>[-\w]+)/$', # View a specific project
        views.ProjectView.as_view(), name='viewProject'),
    url(r'^project/(?P<slug>[-\w]+)/edit/$', # Edit a specific project
        views.EditProjectView.as_view(), name='editProject'),
    url(r'^notes/(?P<project>[-\w]+)/$', # View notes for a project
        views.NotesView.as_view(), name='notes'),
    url(r'^tasklists/(?P<pk>[-\w]+)/$', # View tasklists for a project
        views.TaskListsView.as_view(), name='taskLists'),
    url(r'^tasks/(?P<project>[-\w]+)/(?P<slug>[-\w]+)/$', # View tasks for a tasklist
        views.TasksView.as_view(), name='tasks'),
    url(r'^note/(?P<slug>[-\w]+)/$', # Create a note for a project
        views.NewNoteView.as_view(), name='newNote'),
    url(r'^task/(?P<project>[-\w]+)/(?P<slug>[-\w]+)/$', # Create a new task for a tasklist in a project
        views.NewTaskView.as_view(), name='newTask'),
    url(r'^note/(?P<project>[-\w]+)/(?P<slug>[-\w]+)/$', # Edit an existing note
        views.NoteView.as_view(), name='note'),
    url(r'^task/(?P<project>[-\w]+)/(?P<slug>[-\w]+)/(?P<pk>\d+)/$', # Edit a task
        views.TaskView.as_view(), name='task'),
)

