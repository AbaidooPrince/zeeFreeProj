#new s

from django.urls import path
from .views import TemplateView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
]





