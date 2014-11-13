from django.db import models

# Create your models here.

class Category(models.Model):
    category_text = models.CharField(max_length=40)
    category_description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.category_text


class Question(models.Model):
    category = models.ForeignKey(Category)
    question_text = models.CharField(max_length=200)
    answer_text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.question_text
