from django.conf.urls import patterns, url, include

from pm import views
from pm import forms

urlpatterns = patterns(
    '',
    url(r'^pm/$', views.ProjectsView.as_view(), name='projects'),
    url(r'^notes/$', views.NotesView.as_view(), name='notes'),
    url(r'^tasklists/$', views.TaskListsView.as_view(), name='taskLists'),
    url(r'^tasks/(?P<slug>[-\w]+)/$', views.TasksView.as_view(), name='tasks'),
    url(r'^note/$', views.NewNoteView.as_view(), name='newNote'),
    url(r'^tasklist/(?P<slug>[-\w]+)/$', views.NewTaskView.as_view(), name='newTask'), # slug is the tasklist
    url(r'^note/(?P<slug>[-\w]+)/$', views.NoteView.as_view(), name='note'), # for editing?
    url(r'^task/(?P<pk>\d+)/$', views.TaskView.as_view(), name='task'), # for editing?
)

