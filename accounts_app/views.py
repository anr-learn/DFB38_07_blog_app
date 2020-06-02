# DFB38_07_blog_app/accounts_app/views.py

#from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
	""" Sign up a new user """

	form_class = UserCreationForm

	success_url = reverse_lazy("login")

	template_name = "signup.html"


### end ###
