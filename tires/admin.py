from django.contrib import admin
from .models import Tire, Order, OrderItem

@admin.register(Tire)
class TireAdmin(admin.ModelAdmin):
    list_display = ('brand', 'width', 'height', 'diameter', 'season', 'price')
    list_filter = ('brand', 'season', 'diameter')
    search_fields = ('brand',)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ['name', 'quantity', 'price']
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'fio', 'phone', 'email', 'created_at')
    inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'quantity', 'price')
