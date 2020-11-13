from django.db import models


class Resume(models.Model):
    tg_id = models.PositiveIntegerField(verbose_name='Телеграмм ID', unique=True, primary_key=True)
    position = models.CharField(verbose_name='Желаемая должность', max_length=100)
    contacts = models.TextField(verbose_name='Контакты')
    money = models.TextField(verbose_name='Желаемая з/п')
    experience = models.TextField(verbose_name='Опыт')
    education = models.TextField(verbose_name='Образование', blank=True)
    skills = models.TextField(verbose_name='Проф. навыки')
    info = models.TextField(verbose_name='Личные качества', blank=True)
    portfolio_url = models.TextField(verbose_name='Портфолио', blank=True)
    status = models.BooleanField(verbose_name='Cтатус', default=False, blank=True)
    payed = models.BooleanField(verbose_name='Оплата', default=False)


class Vacancy(models.Model):
    tg_id = models.PositiveIntegerField(verbose_name='Телеграмм ID', unique=True, primary_key=True)
    position = models.TextField(verbose_name='Должность в компании')
    company_name = models.TextField(verbose_name='Название компании')
    what_do = models.TextField(verbose_name='Что делать')
    requirements = models.TextField(verbose_name='Требования')
    conditions = models.TextField(verbose_name='Условия')
    money = models.TextField(verbose_name='З/П')
    contacts = models.TextField(verbose_name='Контакты')
    rubric = models.TextField(verbose_name='Рубрика')
    position2 = models.TextField(verbose_name='Должность')
    status = models.BooleanField(verbose_name='Cтатус', default=False)
    payed = models.BooleanField(verbose_name='Оплата', default=False)


class Questions(models.Model):
    tg_id = models.PositiveIntegerField(verbose_name='Телеграмм ID')
    question = models.TextField(verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ', blank=True)

