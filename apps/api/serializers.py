from rest_framework import serializers
from django.contrib.auth.models import User

from apps.questions.models import Question, Option
from apps.exams.models import Exam, Test


class QuestionSerializer(serializers.ModelSerializer):

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
        fields = ('name',)


class TestSerializer(serializers.ModelSerializer):

    # exam = ExamSerializer()
    class Meta:
        model = Test
        read_only_fields = ('user',)
        fields = ('id', 'name', 'user','exam', 'status')


    def create(self, request):
        request['user'] = self.context['request'].user
        return super(TestSerializer, self).create(request)

