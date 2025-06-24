from django.contrib import admin
from .models import Tire

@admin.register(Tire)
class TireAdmin(admin.ModelAdmin):
    list_display = ('brand', 'width', 'height', 'diameter', 'season', 'price')
    list_filter = ('brand', 'season', 'diameter')
    search_fields = ('brand',)
