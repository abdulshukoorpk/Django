from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from apps.questions.models import Option, Question
from apps.exams.models import Exam, Test, Answer

# admin.site.register(User)
admin.site.register(Exam)
admin.site.register(Test)
admin.site.register(Answer)
