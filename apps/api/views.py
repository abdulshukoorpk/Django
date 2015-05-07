from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from rest_framework import status
from rest_framework.decorators import api_view, detail_route, list_route
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions


from apps.questions.models import Question, Option
from apps.exams.models import Exam, Test
from apps.api.serializers import (QuestionSerializer, OptionSerializer,
                                  ExamSerializer, TestSerializer)
from apps.api import permissions


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def list(self, request, exams_pk=None):

        exam = get_object_or_404(Exam, pk=exams_pk)
        question_list = exam.questions.all()
        serializer = QuestionSerializer(question_list, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, exams_pk=None):
        exam = get_object_or_404(Exam, pk=exams_pk)
        question = exam.questions.get(pk=pk)
        options = question.options.order_by('id')
        serializer = OptionSerializer(options, many=True)
        json = {question.question_text: serializer.data}
        return Response(json)


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

    def list(self, request, tests_pk=None):
        test = get_object_or_404(Test, pk=tests_pk)
        exam = test.exam.all()
        print exam
        serializer = ExamSerializer(exam, many=True)
        return Response(serializer.data)


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = (permissions.IsAssignedUser,)

    @list_route(methods=['get'], permission_classes=(permissions.IsAssignedUser,))
    def user(self, request):
        self.queryset = self.queryset.filter(user=request.user)
        return super(TestViewSet, self).list(self, request)
