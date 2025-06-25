from django.http import HttpResponseRedirect, JsonResponse, HttpResponseBadRequest
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Tire, Order, OrderItem


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

    # Фильтрация по параметрам из GET
    season = request.GET.get('season')
    width = request.GET.get('width')
    height = request.GET.get('height')
    diameter = request.GET.get('diameter')
    search = request.GET.get('search')

    if season:
        tires = tires.filter(season=season)
    if width:
        tires = tires.filter(width=width)
    if height:
        tires = tires.filter(height=height)
    if diameter:
        tires = tires.filter(diameter=diameter)
    if search:
        tires = tires.filter(brand__icontains=search)

    context = {
        'tires': tires,
        'category': category,
    }
    return render(request, f'tires/{category}.html', context)

def tire_detail(request, pk):
    tire = get_object_or_404(Tire, pk=pk)
    return render(request, 'tires/tire_detail.html', {'tire': tire})
def add_to_cart(request, pk):
    tire = get_object_or_404(Tire, pk=pk)
    quantity = int(request.POST.get('quantity', 1))

    cart = request.session.get('cart', {})
    cart[str(pk)] = cart.get(str(pk), 0) + quantity
    request.session['cart'] = cart

    return HttpResponseRedirect(reverse('tire_detail', args=[pk]))
def order_success(request):
    return render(request, 'tires/order_success.html')

def place_order(request):
    if request.method == 'POST':
        fio = request.POST.get('fio')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        items_json = request.POST.get('items_json')

        if not items_json:
            return HttpResponseBadRequest("Нет товаров в заказе")

        try:
            items = json.loads(items_json)
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Ошибка в формате JSON")

        order = Order.objects.create(
            fio=fio,
            phone=phone,
            email=email,
            comment=comment
        )

        for item in items:
            OrderItem.objects.create(
                order=order,
                name=item.get('name', 'Без названия'),
                quantity=item.get('quantity', 1),
                price=item.get('price', 0)
            )

        return redirect('order_success')  # ✅ this is correct

    return HttpResponseBadRequest("Ошибка запроса")  # ✅ for non-POST requests
