from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from apps.questions.models import Option, Question

# Create your views here.


def index(request):
    question_list = Question.objects.order_by('id')
    context = {'question_list': question_list}
    return render(request, 'index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    option = question.options.order_by('id')
    context = {'question': question, 'option': option}
    return render(request, 'detail.html', context)
