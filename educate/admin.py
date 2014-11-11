from django.contrib import admin
from educate.models import Category, Question

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_filter = ('category')
    list_display = ('question_text', 'answer_text')

admin.site.register(Question)

admin.site.register(Category)


