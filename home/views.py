from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def project(request):
    return render(request, 'home/project.html')

def resume(request):
    return render(request, 'home/resume.html')
