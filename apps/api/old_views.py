from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from apps.questions.models import Question, Option
from apps.exams.models import Exam, Test
from apps.api.serializers import (QuestionSerializer, OptionSerializer,
                                  ExamSerializer, TestSerializer)
# from apps.api.permissions import IsOwnerOrReadOnly

# Create your views here.


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # permission_classes = (IsOwnerOrReadOnly,)

    # def pre_save(self, obj):
    #     obj.owner = self.request.user


@api_view(['GET', 'PUT', 'DELETE'])
def question_details(request, question_id, format=None):
    """
    Lists the question with given id and it's options
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'GET':
        options = question.options.order_by('id')
        serializer = OptionSerializer(options, many=True)
        json = {question.question_text: serializer.data}
        return Response(json)

    elif request.method == 'PUT':
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def exam_list(request):
    """
    Lists all exams
    """
    if request.method == 'GET':
        exams = Exam.objects.all()
        serializer = ExamSerializer(exams, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ExamSerializer(data=request.DATA)
        if serializer.is_valid():
            return Response(serializer.data, status=staus.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


@api_view(['GET', 'PUT', 'DELETE'])
def exam_detail(request, exam_id):
    """
    Lists the questions for given Exam
    """
    print 1
    exam = get_object_or_404(Exam, pk=exam_id)
    print 2
    if request.method == 'GET':
        questions = exam.questions.all()
        serializer = QuestionSerializer(questions, many=True)
        json = {exam.name: serializer.data}
        print 'json is %s' % json
        return Response(json)


@api_view(['GET', 'POST'])
def test_list(request):
    """
    Lists all available test_list
    """
    if request.method == 'GET':
        tests = Test.objects.all()
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data)
