from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response

# Create your views here.
from apps.exams.models import Exam, Test, Answer
from apps.questions.models import Option, Question
from apps.exams.forms import ExamForm, TestForm

@login_required
def exam_list(request):
	user = request.user
	test_name = Test.objects.filter(user=user)
	for test in test_name:
		exam_name = test.exam.name
		exam_id = test.exam.id
	context = {'user': user, 'exam_name': exam_name, 'exam_id':exam_id }
	return render_to_response('exam_display.html', context)

@login_required
@csrf_exempt
def get_question(request, test_id, index):

	user = request.user
	test = get_object_or_404(Test, pk=test_id)
	exam = test.exam
	print exam
	exam_id = exam.id
	print exam.id
	question = exam.questions.all()[int(index) - 1]
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
	 'index': index
		 
	 }

	'''if request.method == 'POST':
		save_answer(test_id, index)
		print 'hiiiiii'
	else:
		print 'kkkkkk' '''
	
	return render_to_response('question_display.html', context)

	

@login_required
@csrf_exempt
def save_answer(request, test_id,index):
	if request.method == 'POST':

		user = request.user
		test = get_object_or_404(Test, pk=test_id)
		exam = test.exam
		question = exam.questions.all()[int(index)]
		options = question.options.filter(question=question)
		selected_option_id = request.POST.get(key = 'option')
		selected_option = Option.objects.get(pk=selected_option_id)
		print "selected option is %s" % selected_option
		answer = Answer.objects.create(
			selected_option = selected_option, test = test
			)

		answer.save()
		index = int(index)+1
		return HttpResponseRedirect('/exams/%s/%s' % (test_id,index))

@login_required
def result(request, test_id):
	
	test = get_object_or_404(Test, pk=exam_id)
	questions = exam_name.questions.all()
	#for question in questions:
	currect_options = Option.objects.filter(is_right_answer=True)
	print '0004444'
	print currect_options
	print Answer.objects.all()
	return HttpResponse('Site under construction')


