# Generated by Django 3.0.4 on 2020-05-03 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20200328_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='products/placeholder.jpg', upload_to='products/images'),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
