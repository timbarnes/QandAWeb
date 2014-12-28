from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required

from users import views
from users import forms

urlpatterns = patterns(
    '',
    url(r'^myhome/$', views.MyHomeView.as_view(), name='myHome'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^profile/p/(?P<pk>[0-9]+)/$', views.UpdateProfileView.as_view(), name='profileUpdate'),
    url(r'^profile/u/(?P<pk>[0-9]+)/$', views.UpdateUserDataView.as_view(), name='userdataUpdate'),
    url(r'^notes/$', views.NotesView.as_view(), name='notes'),
    url(r'^tasklists/$', views.TaskListsView.as_view(), name='taskLists'),
    url(r'^tasks/(?P<slug>[-\w]+)/$', views.TasksView.as_view(), name='tasks'),
    url(r'^note/$', views.NewNoteView.as_view(), name='newNote'),
    url(r'^tasklist/(?P<slug>[-\w]+)/$', views.NewTaskView.as_view(), name='newTask'), # slug is the tasklist
    url(r'^note/(?P<slug>[-\w]+)/$', views.NoteView.as_view(), name='note'), # for editing?
    url(r'^task/(?P<slug>[-\w]+)/$', views.TaskView.as_view(), name='task'), # for editing?
)

