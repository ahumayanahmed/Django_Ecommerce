# Generated by Django 5.1.5 on 2025-02-08 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoris', '0004_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='position',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
