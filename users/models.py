from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
from educate.models import Subject, Category, Article
from taggit.managers import TaggableManager


class Profile(models.Model):
    user = models.ForeignKey(User)
    picture = models.ImageField(upload_to='/media/profilepics/', blank=True)
    home = models.CharField(max_length=100, blank=True)
    interests = models.CharField(max_length=200, blank=True)
    objectives = models.CharField(max_length=200, blank=True)
    joined = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user.username


class Favorites(models.Model):
    user = models.ForeignKey(User)
    subjects = models.ManyToManyField(Subject, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    articles = models.ManyToManyField(Article, blank=True)

    def __unicode__(self):
        return self.user.username


class TaskList(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    tags = TaggableManager()

    def __unicode__(self):
        return slug


class Task(models.Model):
    tasklist = models.ForeignKey(TaskList)
    task = models.CharField(max_length=200)
    due = models.DateField(blank=True)
    slug = models.SlugField()

    def __unicode__(self):
        return slug

    
class Note(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    body = tinymce_models.HTMLField()
    edit_date = models.DateField(auto_now=True)
    slug = models.SlugField()
    tags = TaggableManager()

    def __unicode__(self):
        return slug



    
