# Generated by Django 3.0.4 on 2020-03-28 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0009_auto_20200328_1607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='cart_item',
            new_name='cartitem',
        ),
    ]
