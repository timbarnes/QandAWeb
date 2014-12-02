from django.contrib import admin
from educate.models import Subject, Category, Question, Article

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_filter = ('category')
    list_display = ('question_text', 'answer_text')

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Subject)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Article)
