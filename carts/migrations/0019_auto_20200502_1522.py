# Generated by Django 3.0.4 on 2020-05-02 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0018_cart_shipping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='carts.Customer'),
        ),
    ]
