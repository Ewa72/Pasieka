from django.urls import path
from . import views

urlpatterns = [
    path('miody/', views.miody, name='miody'),
]