from django.urls import path
from . import views

urlpatterns = [
    path('miody/', views.miody, name='miody'),
    path('miody/miod_details/<int:id>', views.miod_details, name='miod_details'),
 #   path('miody/', views.MiodyListView.as_view(), name='miody'),
]