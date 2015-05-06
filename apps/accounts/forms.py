from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.forms.formsets import formset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


class RegistrationForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(
        attrs=dict(max_length=30, required=True)),
        label='User name',
        error_messages={'requred': 'Please enter a user name'}
    )

    email = forms.EmailField(widget=forms.EmailInput(
        attrs=dict(max_length=60, required=True)),
        label='Email address',
        # error_messages={'requred':'Please enter a valid email address'}
    )

    password = forms.CharField(widget=forms.PasswordInput(
        attrs=dict(max_length=30, required=True)),
        label='Enter a password',
        # error_messages={'requred':'Please enter a password'}
    )

    password_confirm = forms.CharField(widget=forms.PasswordInput(
        attrs=dict(max_length=30, required=True)),
        label='Repeat password',
        # error_messages={'requred':'Please repeat the password'}
    )

    helper = FormHelper()
    helper.form_method = "POST"
    helper.add_input(Submit('register', 'Register', css_class='btn-primary'))
    # helper.add_input(Submit('login', 'Login', css_class='btn-secondary'))

    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        user_count = User.objects.filter(username=username)
        email_count = User.objects.filter(email=email)
        if user_count:
            raise forms.ValidationError('User name already exist!')
        elif email_count:
            raise forms.ValidationError('That email ID is already registered')
        elif password != password_confirm:
            raise forms.ValidationError("Passwords do not match")
        return self.cleaned_data
