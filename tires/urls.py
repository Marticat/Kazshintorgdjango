from django.urls import path
from .views import tire_list_by_category, home, contacts, service, blog, details, calculator, cart, main, light, commerce, disc

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('service/', service, name='service'),
    path('blog/', blog, name='blog'),
    path('details/', details, name='details'),
    path('calculator/', calculator, name='calculator'),
    path('cart/', cart, name='cart'),
    path('main/', main, name='main'),
    path('light/', lambda request: tire_list_by_category(request, 'light'), name='light'),
    path('commerce/', lambda request: tire_list_by_category(request, 'commerce'), name='commerce'),
    path('disc/', lambda request: tire_list_by_category(request, 'disc'), name='disc'),


    path('<str:category>/', tire_list_by_category, name='tire_by_category'),
]
