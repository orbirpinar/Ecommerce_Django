# Generated by Django 3.0.4 on 2020-05-02 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0017_auto_20200502_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='shipping',
            field=models.BooleanField(default=False),
        ),
    ]
