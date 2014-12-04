from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from tinymce import models as tinymce_models
from taggit.managers import TaggableManager


class Subject(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200, default='-description-')
    slug = models.SlugField()
    tags = TaggableManager()

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Category(models.Model):
    subject = models.ForeignKey(Subject)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200, default='-description-')
    slug = models.SlugField()
    tags = TaggableManager()

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'
        
    def __unicode__(self):
        return self.name


class Question(models.Model):
    category = models.ForeignKey(Category)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    tags = TaggableManager()

    class Meta:
        ordering = ['question']

    def __unicode__(self):
        return self.question


class Article(models.Model):
    author = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=200)
    body = tinymce_models.HTMLField()
    published = models.BooleanField(default=False)
    edit_date = models.DateField(default=datetime.now)
    slug = models.SlugField()
    tags = TaggableManager()

    class Meta:
        ordering = ['-edit_date']

    def __unicode__(self):
        return self.title
