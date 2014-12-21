from django.contrib import admin
from users.models import Profile, Favorites, TaskList, Task, Note

admin.site.register(Profile)
admin.site.register(Favorites)
admin.site.register(TaskList)
admin.site.register(Task)
admin.site.register(Note)
