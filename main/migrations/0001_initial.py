# Generated by Django 3.0 on 2020-05-15 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_id', models.PositiveIntegerField(verbose_name='Телеграмм ID')),
                ('question', models.TextField(verbose_name='Вопрос')),
                ('answer', models.TextField(blank=True, verbose_name='Ответ')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('tg_id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Телеграмм ID')),
                ('full_name', models.CharField(max_length=150, verbose_name='ФИО')),
                ('date_b', models.TextField(blank=True, verbose_name='Дата рождения')),
                ('country_city', models.TextField(default='Не указано', verbose_name='Страна и город')),
                ('position', models.CharField(max_length=100, verbose_name='Желаемая должность')),
                ('contacts', models.TextField(verbose_name='Контакты')),
                ('money', models.TextField(verbose_name='Желаемая з/п')),
                ('experience', models.TextField(verbose_name='Опыт')),
                ('education', models.TextField(blank=True, verbose_name='Образование')),
                ('skills', models.TextField(verbose_name='Проф. навыки')),
                ('recomendations', models.TextField(blank=True, verbose_name='Рекомендации')),
                ('info', models.TextField(blank=True, verbose_name='Личные качества')),
                ('portfolio_url', models.URLField(blank=True, verbose_name='Портфолио')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('tg_id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Телеграмм ID')),
                ('position', models.TextField(verbose_name='Должность в компании')),
                ('company_name', models.TextField(verbose_name='Название компании')),
                ('what_do', models.TextField(verbose_name='Что делать')),
                ('requirements', models.TextField(verbose_name='Требования')),
                ('conditions', models.TextField(verbose_name='Условия')),
                ('money', models.TextField(verbose_name='З/П')),
                ('contacts', models.TextField(verbose_name='Контакты')),
                ('rubric', models.TextField(verbose_name='Рубрика')),
                ('position2', models.TextField(verbose_name='Должность')),
            ],
        ),
    ]