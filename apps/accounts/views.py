from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from apps.accounts.forms import RegistrationForm
from django.shortcuts import render
# Create your views here.


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
            )
            return HttpResponseRedirect('success/')

    else:
        form = RegistrationForm()

    variables = RequestContext(request, {
        'form': form
    })
    return render_to_response('registration/register.html',
                              variables)


def register_success(request):
    return render_to_response('registration/success.html')


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/accounts/')


@login_required
def home(request):
    return render_to_response('registration/home.html', {'user': request.user})
