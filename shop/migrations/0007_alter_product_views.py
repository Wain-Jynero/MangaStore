# Generated by Django 4.2.1 on 2023-05-23 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_product_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='views',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Просмотренные товары'),
        ),
    ]
