# Generated by Django 3.0 on 2020-05-16 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200516_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='payed',
            field=models.BooleanField(default=False, verbose_name='Оплата'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='payed',
            field=models.BooleanField(default=False, verbose_name='Оплата'),
        ),
    ]
