from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
from taggit.managers import TaggableManager


class Project(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.CharField(max_length=200, null=True, blank=True)
    tags = TaggableManager(blank=True)

    class Meta:
        unique_together = ('user', 'slug')

    def __unicode__(self):
        return self.slug


class TaskList(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    tags = TaggableManager(blank=True)

    class Meta:
        unique_together = ('project', 'slug')

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
    project = models.ForeignKey(Project)
    title = models.CharField(max_length=200)
    body = tinymce_models.HTMLField()
    edit_date = models.DateField(auto_now=True)
    slug = models.SlugField()
    tags = TaggableManager(blank=True)

    class Meta:
        unique_together = ('project', 'slug')

    def __unicode__(self):
        return self.slug



    
