from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    return render(request, 'index.html')

def service_view(request):
    return render(request, 'service.html')

def skills_view(request):
    return render(request, 'skills.html')

def education_view(request):
    return render(request, 'education.html')

def resume_view(request):
    return render(request, 'resume.html')

def contact_view(request):
    return render(request, 'contact.html')


def contact_view(request):
    if request.method == 'POST':
        print("------------post5 ----------")
        data = request.POST
        fname = data.get('fname')
        lname = data.get('lname')
        email = data.get('email')
        message = data.get('message')
        print(fname,lname,email,message)

        new_entry = Port(fname=fname, lname = lname, email=email, message=message)
        new_entry.save()
        


    return render(request, 'contact.html')
    



