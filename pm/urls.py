from django.conf.urls import patterns, url, include

from pm import views
from pm import forms

urlpatterns = patterns(
    '',
    url(r'^pm/$', views.ProjectsView.as_view(), name='projects'),
    #url(r'^pmnew/$', views.CreateProjectView.as_view(), name='newProject'),
    url(r'^project/(?P<slug>[-\w]+)/$', views.ProjectView.as_view(), name='viewProject'),
    url(r'^editproject/(?P<slug>[-\w]+)/$', views.EditProjectView.as_view(), name='editProject'),
    url(r'^notes/(?P<project>[-\w]+)/$', views.NotesView.as_view(), name='notes'),
    url(r'^tasklists/(?P<project>[-\w]+)/$', views.TaskListsView.as_view(), name='taskLists'),
    url(r'^tasks/(?P<slug>[-\w]+)/$', views.TasksView.as_view(), name='tasks'),
    url(r'^note/(?P<project>[-\w]+)/$', views.NewNoteView.as_view(), name='newNote'),
    url(r'^tasklist/(?P<slug>[-\w]+)/$', views.NewTaskView.as_view(), name='newTask'), # slug is the tasklist
    url(r'^note/(?P<slug>[-\w]+)/$', views.NoteView.as_view(), name='note'), # for editing?
    url(r'^task/(?P<pk>\d+)/$', views.TaskView.as_view(), name='task'), # for editing?
)

