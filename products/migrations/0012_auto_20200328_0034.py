# Generated by Django 3.0.4 on 2020-03-27 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20200327_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('S', 'Shirt'), ('SW', 'Sport wear'), ('OW', 'Outwear')], default='S', max_length=2),
        ),
        migrations.DeleteModel(
            name='OrderProduct',
        ),
    ]