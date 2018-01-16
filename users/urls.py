from django.urls import path
from django.contrib.auth.decorators import login_required

from users import views

urlpatterns = [
    path('myhome/', views.MyHomeView.as_view(), name='myHome'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/p/<int:pk>/', views.UpdateProfileView.as_view(),
         name='profileUpdate'),
    path('profile/u/<int:pk>/', views.UpdateUserDataView.as_view(),
         name='userdataUpdate'),
    path('notes/', views.NotesView.as_view(), name='notes'),
    path('tasklists/', views.TaskListsView.as_view(), name='taskLists'),
    path('tasks/<slug:slug>/', views.TasksView.as_view(), name='tasks'),
    path('note/', views.NewNoteView.as_view(), name='newNote'),
    path('tasklist/<slug:slug>/', views.NewTaskView.as_view(),
         name='newTask'),  # slug is the tasklist
    path('note/<slug:slug>/', views.NoteView.as_view(), name='note'),
    # for editing?
    path('task/<slug:slug>/', views.TaskView.as_view(), name='task'),
    # for editing?
]
