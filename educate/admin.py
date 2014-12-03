from django.contrib import admin
from educate.models import Tag, Subject, Category, Question, Article

# Register your models here.

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name')}

class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('subject__name',)

class QuestionAdmin(admin.ModelAdmin):
    list_filter = ('category')
    list_display = ('question_text', 'answer_text')

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Tag)
admin.site.register(Subject)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Article)
