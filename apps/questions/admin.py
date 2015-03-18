from django.contrib import admin

# Register your models here.
from apps.questions.models import Option, Question

class OptionInline(admin.TabularInline):
	model = Option
	# fields = ['option','is_right_answer']
	extra = 4

class QuestionAdmin(admin.ModelAdmin):
	fields = ['question_text']
	inlines = [OptionInline]


admin.site.register(Question, QuestionAdmin)
