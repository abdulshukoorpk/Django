from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from apps.questions.models import Option, Question


class Exam(models.Model):
	name = models.CharField(max_length=50)
	questions = models.ManyToManyField(Question)

	def __unicode__(self):
		return self.name


class Test(models.Model):
	name = models.CharField(max_length=20)
	user = models.ForeignKey(User, related_name='tests')
	exam = models.ForeignKey(Exam, related_name='tests')
	def __unicode__(self):
		return self.name


	@property
	def count_question(self):
		return len(self.exam.questions.all())

	@property
	def count_right(self):
		return len([a for a in self.answers.all() if a.is_correct])

class Answer(models.Model):
	selected_option = models.ForeignKey(Option, related_name='answers')
	test = models.ForeignKey(Test, related_name='answers')
	#user = models.ForeignKey(User, related_name='users')
	
	@property
	def is_correct(self):
		return option.is_right_answer;

	