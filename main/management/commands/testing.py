from main.models import Resume, Vacancy, Questions
import telebot

bot = telebot.TeleBot('1227931750:AAHxjQLO4oV9jdLPtD3gETJvHXEjAnrwZu4')

from asgiref.sync import async_to_sync, sync_to_async


@sync_to_async
def save_resume(tg_id, position, contacts, money, experience, education, skills, info, portfolio_url):
    try:
        print(tg_id, position, contacts, money, experience, education, skills, info, portfolio_url)
        m = Resume(
            tg_id=tg_id,
            position=position,
            contacts=contacts,
            money=money,
            experience=experience,
            education=education,
            skills=skills,
            info=info,
            portfolio_url=portfolio_url
        )
        m.save()
        print('yep')
    except:
        bot.send_message(tg_id, 'Мы не смогли создать резюме. Видимо, у вас уже есть резюме.\nНапишите в поддержку.')


@sync_to_async
def save_vacancy(tg_id, position, company_name, what_do, requirements, conditions, money, contacts):
    try:
        m = Vacancy(
            tg_id=tg_id,
            position=position,
            company_name=company_name,
            what_do=what_do,
            requirements=requirements,
            conditions=conditions,
            money=money,
            contacts=contacts,
        )
        m.save()
        print('yep')
    except:
        bot.send_message(tg_id, 'Мы не смогли создать вакансию. Видимо, у вас уже есть резвакансияюме.\nНапишите в поддержку.')


@sync_to_async
def save_rubric(tg_id, rubric, position2):
    m = Vacancy.objects.filter(tg_id=tg_id)
    m.update(rubric=rubric, position2=position2)
    print('yep')


@sync_to_async
def save_question(tg_id, question):
    m = Questions(
        tg_id=tg_id,
        question=question,
    )
    m.save()
    print('yep')


@sync_to_async
def payed_update(tg_id):
    m = Vacancy.objects.filter(tg_id=tg_id)
    m.update(payed=True)
    v = Resume.object.filter(tg_id=tg_id)
    v.update(payed=True)
    print('yep')
