# Generated by Django 3.0 on 2020-05-15 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200515_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='country_city',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='date_b',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='full_name',
        ),
    ]