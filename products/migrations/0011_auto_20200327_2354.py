# Generated by Django 3.0.4 on 2020-03-27 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200327_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='label',
            field=models.CharField(blank=True, choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], max_length=1, null=True),
        ),
    ]
