from django.contrib import admin
from pm.models import TaskList, Task, Note

admin.site.register(TaskList)
admin.site.register(Task)
admin.site.register(Note)
