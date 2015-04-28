from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response

# Create your views here.
from apps.exams.models import Exam, Test, Answer
from apps.questions.models import Option, Question
from apps.exams.forms import ExamForm, TestForm


@login_required
def exam_list(request):
    user = request.user
    test_name = Test.objects.filter(user=user).exclude(status=2)
    if test_name:
        for test in test_name:
            exam_name = test.exam.name
            exam_id = test.exam.id
        context = {'user': user, 'exam_name': exam_name, 'exam_id': exam_id}
    else:
        status_message = 'You have no pending test'
        context = {'user': user, 'status_message': status_message}
    return render_to_response('exam_display.html', context)


@login_required
def exam_list(request):
    user = request.user
    test_name = Test.objects.filter(user=user).exclude(status=2)
    if test_name:
        for test in test_name:
            exam_name = test.exam.name
            exam_id = test.exam.id
        context = {'user': user, 'exam_name': exam_name, 'exam_id': exam_id}
    else:
        status_message = 'You have no pending test'
        context = {'user': user, 'status_message': status_message}
    return render_to_response('exam_display.html', context)


@login_required
@csrf_exempt
def get_question(request, test_id, index):

    user = request.user
    test = get_object_or_404(Test, pk=test_id)
    exam = test.exam
    exam_id = exam.id
    question = exam.questions.all()[int(index) - 1]
    question_count = test.count_question
    question_id = question.id
    options = question.options.filter(question=question)
    context = {
        'user': user,
        'test': test,
        'exam': exam,
        'exam_id': exam_id,
        'question': question,
        'options': options,
        'question_id': question_id,
        'index': index,
        'question_count': question_count

    }

    return render_to_response('question_display.html', context)


@login_required
@csrf_exempt
def save_answer(request, test_id, index):
    if request.method == 'POST':
        user = request.user
        test = get_object_or_404(Test, pk=test_id)
        exam = test.exam
        question_count = test.count_question
        question = exam.questions.all()[int(index) - 1]
        options = question.options.filter(question=question)
        selected_option_id = request.POST.get(key='option')
        selected_option = Option.objects.get(pk=selected_option_id)
        answer = Answer.objects.create(
            selected_option=selected_option, test=test
        )
        answer.save()
        index = int(index) + 1

        if question_count >= index:
            return HttpResponseRedirect('/exams/%s/%s' % (test_id, index))

        else:
            return HttpResponseRedirect('/exams/%s/result' % test_id)


@login_required
@csrf_exempt
def result(request, test_id):
    user = request.user
    test = get_object_or_404(Test, pk=test_id)
    exam = test.exam
    question_count = test.count_question
    currect_answer_count = test.count_right
    mark = currect_answer_count * 5
    test.status = 2
    test.save()
    context = {
        'user': user,
        'test': test,
        'currect_answer_count': currect_answer_count,
        'question_count': question_count,
        'mark': mark,
    }
    return render(request, 'result_display.html', context)
