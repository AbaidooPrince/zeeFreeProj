#new s

from django.urls import path
from .views import TemplateView, HomePageView, LoginPageView, SignUpPageView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('login/', LoginPageView.as_view(), name = 'login'),
    path('register', SignUpPageView.as_view(), name = 'signup'),
]





