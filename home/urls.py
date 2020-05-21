# new s

from django.urls import path

from . import views
from .views import TemplateView, HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('register/', views.registerPage,   name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout')
]
