from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from tinymce import models as tinymce_models
from taggit.managers import TaggableManager


class EContent(models.Model):
    author = models.ForeignKey(User)
    public = models.BooleanField(default=True)
    tags = TaggableManager()

    class Meta:
        abstract = True
    

class Subject(EContent):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200, default='-description-')
    slug = models.SlugField()

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Category(EContent):
    subject = models.ForeignKey(Subject)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200, default='-description-')
    slug = models.SlugField()

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'
        unique_together = ('subject', 'slug')
        
    def __unicode__(self):
        return self.name


class Question(EContent):
    category = models.ForeignKey(Category)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

    class Meta:
        ordering = ['question']
        unique_together = ('category', 'question')

    def __unicode__(self):
        return self.question


class Article(EContent):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=200)
    body = tinymce_models.HTMLField()
    summary = models.CharField(max_length=200, default="")
    edit_date = models.DateField(default=datetime.now)
    slug = models.SlugField()

    class Meta:
        ordering = ['-edit_date']
        unique_together = ('category', 'slug')

    def __unicode__(self):
        return self.title
