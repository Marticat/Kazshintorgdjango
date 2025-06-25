from django.db import models

class Tire(models.Model):
    CATEGORY_CHOICES = [
        ('light', 'Легковые'),
        ('commerce', 'Грузовые'),
        ('disc', 'Диски'),
    ]
    SEASON_CHOICES = [
        ('summer', 'Летняя'),
        ('winter', 'Зимняя'),
        ('allseason', 'Всесезонная'),
    ]

    brand = models.CharField(max_length=100)
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    diameter = models.PositiveIntegerField()
    season = models.CharField(max_length=10, choices=SEASON_CHOICES)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='light')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='tires/', blank=True, null=True)

    def __str__(self):
        return f"{self.brand} {self.width}/{self.height} R{self.diameter} ({self.get_season_display()})"
class Order(models.Model):
    fio = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заказ #{self.id} от {self.fio}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def total_price(self):
        return self.quantity * self.price
