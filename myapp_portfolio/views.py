from django.shortcuts import render
from django.conf import settings
from .models import Certifications, Projects



def index(request):
    

    return render(request, "home.html")


def certifications(request):
    
    certificates = Certifications.objects.all().order_by('-id')
    
    context = {
        "certificates": certificates,
    }
    return render(request, "certifications.html", context)




def projects(request):
    
    projects = Projects.objects.all().order_by('-id')
    context = {
        "projects": projects,
    }
    
    return render(request, "projects.html", context)


