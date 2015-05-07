from rest_framework import serializers
from django.contrib.auth.models import User

from apps.questions.models import Question, Option
from apps.exams.models import Exam, Test


class QuestionSerializer(serializers.ModelSerializer):

    # owner = serializers.Field('owner.username')

    class Meta:
        model = Question
        fields = ('id', 'question_text', )


class OptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Option
        fields = ('option_text',)


class ExamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exam
        # fields = ('name', 'questions')
        fields = ('name',)


class TestSerializer(serializers.ModelSerializer):

    exam = ExamSerializer()

    class Meta:
        model = Test
        fields = ('id', 'name', 'user', 'exam', 'status')
