from django.shortcuts import render
from django.conf import settings
from .models import Certifications, Projects



def index(request):
    
    certificates = Certifications.objects.all().order_by('-id')
    projects = Projects.objects.all().order_by('-id')
    context = {
        "certificates": certificates,
        "projects": projects,
    }
    
    return render(request, "home.html", context)
