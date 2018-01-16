from django.urls import path, re_path
from django.contrib.auth.decorators import login_required

from users import views
from users import forms

urlpatterns = [
    path(r'myhome/', views.MyHomeView.as_view(), name='myHome'),
    path(r'profile/', views.ProfileView.as_view(), name='profile'),
    re_path(r'profile/p/(?P<pk>[0-9]+)/', views.UpdateProfileView.as_view(), name='profileUpdate'),
    re_path(r'profile/u/(?P<pk>[0-9]+)/', views.UpdateUserDataView.as_view(), name='userdataUpdate'),
    path(r'notes/', views.NotesView.as_view(), name='notes'),
    path(r'tasklists/', views.TaskListsView.as_view(), name='taskLists'),
    re_path(r'tasks/(?P<slug>[-\w]+)/', views.TasksView.as_view(), name='tasks'),
    path(r'note/', views.NewNoteView.as_view(), name='newNote'),
    re_path(r'tasklist/(?P<slug>[-\w]+)/', views.NewTaskView.as_view(), name='newTask'), # slug is the tasklist
    re_path(r'note/(?P<slug>[-\w]+)/', views.NoteView.as_view(), name='note'), # for editing?
    re_path(r'task/(?P<slug>[-\w]+)/', views.TaskView.as_view(), name='task'), # for editing?
]
