from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

class LoginPageView(TemplateView):
    template_name = 'login.html'
    
class SignUpPageView(TemplateView):
    template_name = 'signup.html'