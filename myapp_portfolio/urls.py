
from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index, name="index"),
    path('certifications/', views.certifications, name="certifications"),
    path('projects/', views.projects, name="projects"),
]
