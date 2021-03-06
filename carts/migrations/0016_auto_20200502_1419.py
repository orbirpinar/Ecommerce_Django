# Generated by Django 3.0.4 on 2020-05-02 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0009_add_subregion'),
        ('carts', '0015_adress_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.City'),
        ),
        migrations.AlterField(
            model_name='adress',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.Customer'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.Customer'),
        ),
    ]
