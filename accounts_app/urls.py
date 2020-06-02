# DFB38_07_blog_app/accounts_app/urls.py

from django.urls import path

from .views import SignUpView

urlpatterns = [
	path("signup/", SignUpView.as_view(), name="signup"),
	]



### end ###
