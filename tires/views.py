# tires/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'tires/index.html')

def contacts(request):
    return render(request, 'tires/contacts.html')

def service(request):
    return render(request, 'tires/service.html')

def blog(request):
    return render(request, 'tires/blog.html')
def details(request):
    return render(request, 'tires/details.html')