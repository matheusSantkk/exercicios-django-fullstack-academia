from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('turmas/', views.grade_turmas, name='turmas'),
]