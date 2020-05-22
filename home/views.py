from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

# @login_required(login_url='login')

class HomePageView(TemplateView):
    template_name = 'index.html'


def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            return redirect('login')
    else:
        context = {'form': form}
        return render(request, 'base/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username Or password incorrect')

    context = {}
    return render(request, 'base/login.html', context)


def logoutUser(request):
    logout = (request)
    return redirect('login')
