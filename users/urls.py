from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required

from users import views

urlpatterns = patterns(
    '',
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^myhome/$,', views.MyHomeView.as_view(), name='my_home'),
    url(r'^note/$', views.NewNoteView.as_view(), name='new_note'),
    url(r'^task/$', views.NewTaskView.as_view(), name='new_task'),
    url(r'^note/(P<slug>[-_\w]+)/$', views.NoteView.as_view(), name='note'),
    url(r'^task/(P<slug>[-_\w]+)/$', views.TaskView.as_view(), name='task'),
)

