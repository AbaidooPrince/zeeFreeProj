from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'index.html'


def registerPage(request):
    context = {}
    return render(request, 'base/register.html', context)


def loginPage(request):
    context = {}
    return render(request, 'base/login.html', context)
