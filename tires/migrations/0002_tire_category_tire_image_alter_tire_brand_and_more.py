# Generated by Django 5.2.3 on 2025-06-24 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tires', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tire',
            name='category',
            field=models.CharField(choices=[('light', 'Легковые'), ('commerce', 'Грузовые'), ('disc', 'Диски')], default='light', max_length=10),
        ),
        migrations.AddField(
            model_name='tire',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='tires/'),
        ),
        migrations.AlterField(
            model_name='tire',
            name='brand',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tire',
            name='diameter',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='tire',
            name='height',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='tire',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tire',
            name='season',
            field=models.CharField(choices=[('summer', 'Летняя'), ('winter', 'Зимняя'), ('allseason', 'Всесезонная')], max_length=10),
        ),
        migrations.AlterField(
            model_name='tire',
            name='width',
            field=models.PositiveIntegerField(),
        ),
    ]
