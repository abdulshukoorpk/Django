from django import forms
from django.contrib.auth.models import User

from apps.exams.models import Answer, Exam, Test 

class ExamForm(forms.ModelForm):
	class Meta:
		model = Exam
		fields = ['name', 'questions']

	def exam_set(self):
		exam = Exam.objects.all()
		return self.exam

class TestForm(forms.ModelForm):
	class Meta:
		model = Test
		fields = ['user', 'exam']

class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ['selected_option', 'test']




    