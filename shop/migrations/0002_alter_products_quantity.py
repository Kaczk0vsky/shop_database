# Generated by Django 3.2.16 on 2023-01-22 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
