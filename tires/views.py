# tires/views.py
from django.shortcuts import render
from .models import Tire
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
def calculator(request):
    return render(request, 'tires/calculator.html')
def cart(request):
    return render(request, 'tires/cart.html')
def main(request):
    return render(request, 'tires/main.html')
def light(request):
    return render(request, 'tires/light.html')
def commerce(request):
    return render(request, 'tires/commerce.html')
def disc(request):
    return render(request, 'tires/disc.html')

def tire_list_by_category(request, category):
    tires = Tire.objects.filter(category=category)
    return render(request, f'tires/{category}.html', {'tires': tires})

