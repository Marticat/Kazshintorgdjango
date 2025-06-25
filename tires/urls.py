from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('service/', views.service, name='service'),
    path('blog/', views.blog, name='blog'),
    path('details/', views.details, name='details'),
    path('calculator/', views.calculator, name='calculator'),
    path('cart/', views.cart, name='cart'),
    path('main/', views.main, name='main'),
    path('order-success/', views.order_success, name='order_success'),
    path('place_order/', views.place_order, name='place_order'),  # ← ПЕРЕМЕЩЁН ВЫШЕ

    path('light/', lambda request: views.tire_list_by_category(request, 'light'), name='light'),
    path('commerce/', lambda request: views.tire_list_by_category(request, 'commerce'), name='commerce'),
    path('disc/', lambda request: views.tire_list_by_category(request, 'disc'), name='disc'),
    path('tire/<int:pk>/', views.tire_detail, name='tire_detail'),
    path('tire/<int:pk>/add/', views.add_to_cart, name='add_to_cart'),

    path('<str:category>/', views.tire_list_by_category, name='tire_by_category'),  # ← ДОЛЖЕН БЫТЬ ПОСЛЕДНИМ
]
