# Generated by Django 4.1.4 on 2022-12-30 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_img',
            field=models.CharField(default='', max_length=255),
        ),
    ]