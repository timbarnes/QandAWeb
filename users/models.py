from django.db import models
from django.contrib.auth.models import User
from educate import Subject, Category, Article

class Profile(models.Model):
    user = models.ForeignKey(User)
    picture = models.ImageField(upload_to='/media/profilepics/')
    home = models.CharField(max_length=100)
    interests = models.CharField(max_length=200)
    objectives = models.CharField(max_length=200)
    joined = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return user.username


class Favorites(models.Model):
    user = models.ForeignKey(User)
    subjects = ManyToManyField(Subject)
    categories = ManyToManyField(Category)
    articles = ManyToManyField(Article)

    def __unicode__(self):
        return user.username


class Personal(models.Model):
    user = models.ForeignKey(User)
    to_do = models.ForeignKey(ToDoList)
    notes = models.ForeignKey(Notes)

    def __unicode__(self):
        return user.username


class Note(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    body = tinymce_models.HTMLField()
    edit_date = models.Datefield(auto_now=True)
    slug = models.SlugField()

    def __unicode__(self):
        return slug

    
class Task(models.Model):
    tasklist = models.ForeignKey(TaskList)
    task = models.CharField(max_length=200)
    due = models.DateField()
    slug = models.SlugField()

    def __unicode__(self):
        return slug

    
class TaskList(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __unicode__(self):
        return slug

    
