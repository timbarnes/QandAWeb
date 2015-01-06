from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
from taggit.managers import TaggableManager


class TaskList(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return self.slug


class Task(models.Model):
    tasklist = models.ForeignKey(TaskList)
    task = models.CharField(max_length=200)
    due = models.DateField(null=True, blank=True)
    resolution = models.CharField(max_length=200, null=True, blank=True)
    done = models.BooleanField(default=False)

    def __unicode__(self):
        return self.slug

    
class Note(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    body = tinymce_models.HTMLField()
    edit_date = models.DateField(auto_now=True)
    slug = models.SlugField()
    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return self.slug



    
