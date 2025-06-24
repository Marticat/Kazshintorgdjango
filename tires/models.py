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
