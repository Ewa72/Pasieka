from django.urls import path
from . import views

urlpatterns = [
    #path('miody/', views.miody, name='miody'),
    path('Produkty/miody/', views.miody, name='miody'),
    path('miody/', views.miody, name='miody'),
    path('miod/<int:pk>',views.MiodyDetailView.as_view(), name='miod-detail'),
]