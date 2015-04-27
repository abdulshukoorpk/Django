from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=100)
    owner = models.ForeignKey(User, related_name='questions')

    def __unicode__(self):
        return self.question_text

    class Meta:
        pass


class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options')
    option_text = models.CharField(max_length=50)
    is_right_answer = models.BooleanField(default=False)

    def __unicode__(self):
        return self.option_text
