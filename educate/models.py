from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200, default='-description-')

    def __unicode__(self):
        return self.name


class Category(models.Model):
    subject = models.ForeignKey(Subject)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200, default='-description-')

    def __unicode__(self):
        return self.name


class Question(models.Model):
    category = models.ForeignKey(Category)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

    def __unicode__(self):
        return self.question
