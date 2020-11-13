import telebot
import telegram
from main.models import Vacancy, Resume, Questions

bot = telebot.TeleBot('1227931750:AAHxjQLO4oV9jdLPtD3gETJvHXEjAnrwZu4')


def send_vacancy(tg_id):
    all_part = Vacancy.objects.filter(tg_id=tg_id).all()
    for a in all_part:
        bot.send_message(chat_id='@test_rb', text=f'<b>Требуется {a.position} в {a.company_name}</b>\n'
                                                       f'<b>Что делать:</b>\n'
                                                       f'{a.what_do}\n\n'
                                                       f'<b>Требования:</b>\n'
                                                       f'{a.requirements}\n\n'
                                                       f'<b>Условия:</b>\n'
                                                       f'{a.conditions}\n\n'
                                                       f'<b>Оплата:</b>\n'
                                                       f'{a.money}\n\n'
                                                       f'<b>Контакты:</b>\n'
                                                       f'{a.contacts}\n\n'
                                                       f'Оставить свою вакансию или резюме тут @removejob_bot\n\n'
                                                       f'{a.rubric}\n'
                                                       f'{a.position2}', parse_mode=telegram.ParseMode.HTML)


def send_resume(tg_id):
    all_part = Resume.objects.filter(tg_id=tg_id).all()
    for r in all_part:
        if r.portfolio_url is not None:
            bot.send_message(chat_id='@test_rb', text=f'#Резюме\n'
                                                      f'<b>{r.position}</b>\n'
                                                      f'<b>Опыт:</b>\n'
                                                      f'{r.experience}\n\n'
                                                      f'<b>Проф. навыки:</b>\n'
                                                      f'{r.skills}\n\n'
                                                      f'<b>Образование:</b>\n'
                                                      f'{r.education}\n\n'
                                                      f'<b>Портфолио:</b>\n'
                                                      f'{r.portfolio_url}\n\n'
                                                      f'<b>Желаемая оплата:</b>\n'
                                                      f'{r.money}\n\n'
                                                      f'<b>О себе:</b>\n'
                                                      f'{r.info}\n\n'
                                                      f'<b>Контакты:</b>\n'
                                                      f'{r.contacts}\n\n'
                                                      f'Оставить свою вакансию или резюме тут @removejob_bot\n\n',
                                                      parse_mode=telegram.ParseMode.HTML)
        else:
            bot.send_message(chat_id='@test_rb', text=f'#Резюме\n'
                                                      f'<b>{r.position}</b>\n'
                                                      f'<b>Опыт:</b>\n'
                                                      f'{r.experience}\n\n'
                                                      f'<b>Проф. навыки:</b>\n'
                                                      f'{r.skills}\n\n'
                                                      f'<b>Образование:</b>\n'
                                                      f'{r.education}\n\n'
                                                      f'<b>Желаемая оплата:</b>\n'
                                                      f'{r.money}\n\n'
                                                      f'<b>О себе:</b>\n'
                                                      f'{r.info}\n\n'
                                                      f'<b>Контакты:</b>\n'
                                                      f'{r.contacts}\n\n'
                                                      f'Оставить свою вакансию или резюме тут @removejob_bot\n\n',
                                                      parse_mode=telegram.ParseMode.HTML)


def send_questions(tg_id, question, answer):
    bot.send_message(tg_id, (f"Твой вопрос: {question}\n\n"
                               f"Ответ: {answer}"))



bot.polling()
