from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types.message import ContentTypes
from .config import TOKEN, PAYMENTS_PROVIDER_TOKEN
import telegram
from . import buttons
import logging
from main.models import Resume
from asgiref.sync import async_to_sync, sync_to_async
from . import testing


import aiogram.utils.markdown as md
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode

storage = MemoryStorage()
dp = Bot(token=TOKEN)
bot = Dispatcher(dp, storage=storage)
PAYMENTS_PROVIDER_TOKEN = PAYMENTS_PROVIDER_TOKEN


class FormQuestion(StatesGroup):
    tg_id = State()
    question = State()


class FormRub(StatesGroup):
    tg_id = State()
    rubric = State()
    position2 = State()


class Form(StatesGroup):
    position = State()
    company_name = State()
    what_do = State()
    requirements = State()
    conditions = State()
    money = State()
    contacts = State()
    tg_id = State()


class FormResume(StatesGroup):
    position = State()
    contacts = State()
    money = State()
    experience = State()
    education = State()
    skills = State()
    info = State()
    portfolio_url = State()
    tg_id = State()


# Setup prices
prices_resume = [
    types.LabeledPrice(label='Размещение резюме', amount=200000),
]
prices_vacancy = [
    types.LabeledPrice(label='Размещение Вакансии', amount=100000),
]


@bot.callback_query_handler(lambda c: c.data == 'admin')
async def process_callback_admin(callback_query: types.CallbackQuery):
    await FormQuestion.tg_id.set()
    await dp.answer_callback_query(callback_query.id)
    await dp.edit_message_text(chat_id=callback_query.from_user.id,
                               message_id=callback_query.message.message_id,
                               text='Хорошо, напишите интересующий вас вопрос, и наш модератор обязательно ответит на него! '
                                    'Учитывайте, что я не умею обрабатывать ваши скриншоты, поэтому не отправляйте мне их.\n\n'
                                    '/start - для отмены',
                               parse_mode=telegram.ParseMode.HTML)
    # await dp.send_message(callback_query.from_user.id,
    #                       'Хорошо, напишите интересующий вас вопрос, и наш модератор обязательно ответит на него! '
    #                       'Учитывайте, что я не умею обрабатывать ваши скриншоты, поэтому не отправляйте мне их.',
    #                       reply_markup=buttons.back_add)


@bot.message_handler(state=FormQuestion.tg_id)
async def process_quest(message: types.Message, state: FSMContext):
    if message.text == '/start':
        await dp.send_message(message.from_user.id,
                              'Hello! Как дела?\nЯ бот, который поможет'
                              ' <b>найти сотрудника</b> или <b>устроиться на работу</b>.',
                              parse_mode=telegram.ParseMode.HTML,
                              reply_markup=buttons.inline_kb_full)
    else:
        async with state.proxy() as data:
            data['tg_id'] = message.chat.id
        await FormQuestion.next()
        async with state.proxy() as data:
            data['question'] = message.text

        await testing.save_question(data['tg_id'], data['question'])
        await state.finish()

        await dp.send_message(message.from_user.id,
                              "Окей, ваш вопрос был отправлен в поддержку.",
                              reply_markup=buttons.inline_kb_full)


@bot.message_handler(commands=['start'])
async def send_start(callback_query: types.CallbackQuery):
    await dp.send_message(callback_query.from_user.id,
                          'Hello! Как дела?\nЯ бот, который поможет'
                          ' <b>найти сотрудника</b> или <b>устроиться на работу</b>.',
                          parse_mode=telegram.ParseMode.HTML,
                          reply_markup=buttons.inline_kb_full)


@bot.callback_query_handler(lambda c: c.data == 'vacancy')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await dp.answer_callback_query(callback_query.id)
    await dp.send_message(callback_query.from_user.id,
                          'Хорошо, но вначале необходимо, '
                          'чтобы Вы заполнили некоторые данные. '
                          'Старайтесь писать кратко и выкладывать основную суть предложения. '
                          'Если пост выйдет слишком длинным, то мы его укоротим самостоятельно.')
    await Form.position.set()
    await dp.send_message(callback_query.from_user.id,
                          '<b>Укажите название должности. Рекомендуем сделать максимально коротким и понятным (1-4 слова)</b>\n'
                          'Пример: Программист, Маркетолог, Аналитик, Помощник руководителя.',
                          parse_mode=telegram.ParseMode.HTML)


@bot.message_handler(state='*', commands='cancel')
@bot.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    # Cancel state and inform user about it
    await state.finish()
    # And remove keyboard (just in case)
    await dp.send_message('Cancelled.', reply_markup=types.ReplyKeyboardRemove())


@bot.message_handler(state=Form.position)
async def process_position(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['position'] = message.text

    await Form.next()
    await dp.send_message(message.from_user.id,
                          "<b>Укажите название компании. (1-3 слова)</b>\n"
                          "Пример: Yandex, Telegram",
                          parse_mode=telegram.ParseMode.HTML)


@bot.message_handler(state=Form.company_name)
async def process_company_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['company_name'] = message.text
    await Form.next()

    await dp.send_message(message.from_user.id,
                          "<b>Что нужно делать? Рекомендуем сделать количество знаков — 120.</b>\n"
                          "Пример:\n"
                          "- Планирование рабочего дня;\n"
                          "- Ведение деловой переписки;\n"
                          "- Заполнение отчётов",
                          parse_mode=telegram.ParseMode.HTML)


@bot.message_handler(state=Form.what_do)
async def process_what_do(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['what_do'] = message.text

    await Form.next()
    await dp.send_message(message.from_user.id,
                          "<b>Укажите самые важные требования к кандидату. Рекомендуем сделать количество знаков — 140</b>\n"
                          "Пример:\n"
                          "- Опыт работы с фреймворком Yii, Yii2 от 3-х лет;\n"
                          "- Знание SQL;\n"
                          "- GIT;\n"
                          "- Умение разобраться в чужом коде\n"
                          "Список должен быть кратким и по делу. Такие качества, как пунктуальность и сдача работы в срок являются универсальными, и указывать их не стоит.",
                          parse_mode=telegram.ParseMode.HTML)


@bot.message_handler(state=Form.requirements)
async def process_requirements(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['requirements'] = message.text

    await Form.next()
    await dp.send_message(message.from_user.id,
                          "<b>Какие условия Вы обещаете кандидату? Заполняйте кратко, не нужно писать про печеньки в офисе и дружный коллектив</b>\n"
                          "Пример:\n"
                          "- График работы 5/2 с 10:00 до 19:00;\n"
                          "- Оплачиваемые тренинги",
                          parse_mode=telegram.ParseMode.HTML)


@bot.message_handler(state=Form.conditions)
async def process_conditions(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['conditions'] = message.text

    await Form.next()
    await dp.send_message(message.from_user.id,
                          "<b>Укажите уровень зарплаты, строго придерживайтесь примеров ниже.</b>\n"
                          "Пример:\n"
                          "50000 рублей в месяц\n"
                          "60000-120000 р/мес\n"
                          "По итогам собеседования",
                          parse_mode=telegram.ParseMode.HTML)


@bot.message_handler(state=Form.money)
async def process_money(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['money'] = message.text

    await Form.next()
    await dp.send_message(message.from_user.id,
                          "<b>Контактная информация. Весь текст, что не касается контактной информации мы будем убирать</b>\n"
                          "Пример:\n"
                          "- Галина Петровна +797977999\n"
                          "- email@email.name\n"
                          "- @username (ник в телеграме)\n",
                          parse_mode=telegram.ParseMode.HTML)


@bot.message_handler(state=Form.contacts)
async def process_contacts(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['contacts'] = message.text

    await Form.next()

    async with state.proxy() as data:
        data['tg_id'] = message.chat.id

    await testing.save_vacancy(data['tg_id'], data['position'], data['company_name'], data['what_do'], data['requirements'],
                               data['conditions'], data['money'], data['contacts'])

    await state.finish()
    await FormRub.tg_id.set()
    await dp.send_message(message.from_user.id,
                          "<b>Выберите из предложенного списка необходимую рубрику. "
                          "Если Вы не нашли подходящую, "
                          "тогда выберите ту, которая подходит больше всего.</b>",
                          parse_mode=telegram.ParseMode.HTML,
                          reply_markup=buttons.markup)


@bot.callback_query_handler(lambda c: c.data == 'Тексты', state=FormRub.tg_id)
async def process_rubric(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['tg_id'] = callback_query.message.chat.id
    await FormRub.next()

    async with state.proxy() as data:
        data['rubric'] = 'Тексты'
    await FormRub.next()

    await dp.edit_message_text(chat_id=callback_query.from_user.id,
                               message_id=callback_query.message.message_id,
                               text="<b>Выберите подходящую должность</b>",
                               parse_mode=telegram.ParseMode.HTML,
                               reply_markup=buttons.texts_btn)


@bot.callback_query_handler(lambda c: c.data and c.data.startswith('text'), state=FormRub.position2)
async def process_position_texts(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['position2'] = callback_query.data[5:]

    await testing.save_rubric(data['tg_id'], data['rubric'], data['position2'])
    await state.finish()

    await dp.send_invoice(callback_query.message.chat.id,
                          title='Размещение вакансии',
                          description='Оплата за размещение вакансии - 1000₽.\n'
                                      'Все средства сразу уходят в рекламу нашего проекта, чтобы ещё больше '
                                      'соискателей узнали о вашем предложении.',
                          provider_token=PAYMENTS_PROVIDER_TOKEN,
                          currency='rub',
                          photo_url='https://centersoveta.ru/wp-content/uploads/2019/03/vosstanovlenie-na-rabote.png',
                          photo_height=1126,  # !=0/None or picture won't be shown
                          photo_width=2000,
                          photo_size=512,
                          is_flexible=False,  # True If you need to set up Shipping Fee
                          prices=prices_vacancy,
                          start_parameter='time-machine-example',
                          payload='its payload')


@bot.callback_query_handler(lambda c: c.data == 'back_rubric')
async def process_rubric_back(callback_query: types.CallbackQuery):
    await dp.answer_callback_query(callback_query.id)
    await dp.edit_message_text(chat_id=callback_query.from_user.id,
                               message_id=callback_query.message.message_id,
                               text="<b>Выберите из предложенного списка необходимую рубрику. "
                               "Если Вы не нашли подходящую, "
                               "тогда выберите ту, которая подходит больше всего.</b>",
                               parse_mode=telegram.ParseMode.HTML,
                               reply_markup=buttons.markup)


@bot.callback_query_handler(lambda c: c.data == 'Дизайн/Арт', state=FormRub.tg_id)
async def process_rubric_design(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['tg_id'] = callback_query.message.chat.id
    await FormRub.next()

    async with state.proxy() as data:
        data['rubric'] = 'Дизайн/Арт'
    await FormRub.next()

    await dp.edit_message_text(chat_id=callback_query.from_user.id,
                               message_id=callback_query.message.message_id,
                               text="<b>Выберите подходящую должность</b>",
                               parse_mode=telegram.ParseMode.HTML,
                               reply_markup=buttons.design)


@bot.callback_query_handler(lambda c: c.data and c.data.startswith('design'), state=FormRub.position2)
async def process_position_design(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['position2'] = callback_query.data[7:]

    await testing.save_rubric(data['tg_id'], data['rubric'], data['position2'])
    await state.finish()

    await dp.send_invoice(callback_query.message.chat.id,
                          title='Размещение вакансии',
                          description='Оплата за размещение вакансии - 1000₽.\n'
                                      'Все средства сразу уходят в рекламу нашего проекта, чтобы ещё больше '
                                      'соискателей узнали о вашем предложении.',
                          provider_token=PAYMENTS_PROVIDER_TOKEN,
                          currency='rub',
                          photo_url='https://centersoveta.ru/wp-content/uploads/2019/03/vosstanovlenie-na-rabote.png',
                          photo_height=1126,  # !=0/None or picture won't be shown
                          photo_width=2000,
                          photo_size=512,
                          is_flexible=False,  # True If you need to set up Shipping Fee
                          prices=prices_vacancy,
                          start_parameter='time-machine-example',
                          payload='its payload')


@bot.callback_query_handler(lambda c: c.data == 'Реклама и маркетинг', state=FormRub.tg_id)
async def process_rubric_ad(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['tg_id'] = callback_query.message.chat.id
    await FormRub.next()

    async with state.proxy() as data:
        data['rubric'] = 'Реклама и маркетинг'
    await FormRub.next()

    await dp.edit_message_text(chat_id=callback_query.from_user.id,
                               message_id=callback_query.message.message_id,
                               text="<b>Выберите подходящую должность</b>",
                               parse_mode=telegram.ParseMode.HTML,
                               reply_markup=buttons.ad)


@bot.callback_query_handler(lambda c: c.data and c.data.startswith('ad'), state=FormRub.position2)
async def process_position_ad(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['position2'] = callback_query.data[3:]

    await testing.save_rubric(data['tg_id'], data['rubric'], data['position2'])
    await state.finish()
    await dp.send_invoice(callback_query.message.chat.id,
                          title='Размещение вакансии',
                          description='Оплата за размещение вакансии - 1000₽.\n'
                                      'Все средства сразу уходят в рекламу нашего проекта, чтобы ещё больше '
                                      'соискателей узнали о вашем предложении.',
                          provider_token=PAYMENTS_PROVIDER_TOKEN,
                          currency='rub',
                          photo_url='https://centersoveta.ru/wp-content/uploads/2019/03/vosstanovlenie-na-rabote.png',
                          photo_height=1126,  # !=0/None or picture won't be shown
                          photo_width=2000,
                          photo_size=512,
                          is_flexible=False,  # True If you need to set up Shipping Fee
                          prices=prices_vacancy,
                          start_parameter='time-machine-example',
                          payload='its payload')


@bot.callback_query_handler(lambda c: c.data == 'Полиграфия', state=FormRub.tg_id)
async def process_rubric_pg(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['tg_id'] = callback_query.message.chat.id
    await FormRub.next()

    async with state.proxy() as data:
        data['rubric'] = 'Полиграфия'
    await FormRub.next()

    await dp.edit_message_text(chat_id=callback_query.from_user.id,
                               message_id=callback_query.message.message_id,
                               text="<b>Выберите подходящую должность</b>",
                               parse_mode=telegram.ParseMode.HTML,
                               reply_markup=buttons.pg)


@bot.callback_query_handler(lambda c: c.data and c.data.startswith('pg'), state=FormRub.position2)
async def process_position_pg(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['position2'] = callback_query.data[3:]

    await testing.save_rubric(data['tg_id'], data['rubric'], data['position2'])
    await state.finish()
    await dp.send_invoice(callback_query.message.chat.id,
                          title='Размещение вакансии',
                          description='Оплата за размещение вакансии - 1000₽.\n'
                                      'Все средства сразу уходят в рекламу нашего проекта, чтобы ещё больше '
                                      'соискателей узнали о вашем предложении.',
                          provider_token=PAYMENTS_PROVIDER_TOKEN,
                          currency='rub',
                          photo_url='https://centersoveta.ru/wp-content/uploads/2019/03/vosstanovlenie-na-rabote.png',
                          photo_height=1126,  # !=0/None or picture won't be shown
                          photo_width=2000,
                          photo_size=512,
                          is_flexible=False,  # True If you need to set up Shipping Fee
                          prices=prices_vacancy,
                          start_parameter='time-machine-example',
                          payload='its payload')


@bot.callback_query_handler(lambda c: c.data == 'Разработка сайтов', state=FormRub.tg_id)
async def process_rubric_s(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['tg_id'] = callback_query.message.chat.id
    await FormRub.next()

    async with state.proxy() as data:
        data['rubric'] = 'Разработка сайтов'
    await FormRub.next()
    await dp.edit_message_text(chat_id=callback_query.from_user.id,
                               message_id=callback_query.message.message_id,
                               text="<b>Выберите подходящую должность</b>",
                               parse_mode=telegram.ParseMode.HTML,
                               reply_markup=buttons.sites)


@bot.callback_query_handler(lambda c: c.data and c.data.startswith('site'), state=FormRub.position2)
async def process_position_site(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['position2'] = callback_query.data[5:]

    await testing.save_rubric(data['tg_id'], data['rubric'], data['position2'])
    await state.finish()
    await dp.send_invoice(callback_query.message.chat.id,
                          title='Размещение вакансии',
                          description='Оплата за размещение вакансии - 1000₽.\n'
                                      'Все средства сразу уходят в рекламу нашего проекта, чтобы ещё больше '
                                      'соискателей узнали о вашем предложении.',
                          provider_token=PAYMENTS_PROVIDER_TOKEN,
                          currency='rub',
                          photo_url='https://centersoveta.ru/wp-content/uploads/2019/03/vosstanovlenie-na-rabote.png',
                          photo_height=1126,  # !=0/None or picture won't be shown
                          photo_width=2000,
                          photo_size=512,
                          is_flexible=False,  # True If you need to set up Shipping Fee
                          prices=prices_vacancy,
                          start_parameter='time-machine-example',
                          payload='its payload')


@bot.callback_query_handler(lambda c: c.data == 'Программирование', state=FormRub.tg_id)
async def process_rubric_prog(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['tg_id'] = callback_query.message.chat.id
    await FormRub.next()

    async with state.proxy() as data:
        data['rubric'] = 'Программирование'
    await FormRub.next()
    await dp.edit_message_text(chat_id=callback_query.from_user.id,
                               message_id=callback_query.message.message_id,
                               text="<b>Выберите подходящую должность</b>",
                               parse_mode=telegram.ParseMode.HTML,
                               reply_markup=buttons.program)


@bot.callback_query_handler(lambda c: c.data and c.data.startswith('program'), state=FormRub.position2)
async def process_position_program(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['position2'] = callback_query.data[8:]

    await testing.save_rubric(data['tg_id'], data['rubric'], data['position2'])
    await state.finish()
    await dp.send_invoice(callback_query.message.chat.id,
                          title='Размещение вакансии',
                          description='Оплата за размещение вакансии - 1000₽.\n'
                                      'Все средства сразу уходят в рекламу нашего проекта, чтобы ещё больше '
                                      'соискателей узнали о вашем предложении.',
                          provider_token=PAYMENTS_PROVIDER_TOKEN,
                          currency='rub',
                          photo_url='https://centersoveta.ru/wp-content/uploads/2019/03/vosstanovlenie-na-rabote.png',
                          photo_height=1126,  # !=0/None or picture won't be shown
                          photo_width=2000,
                          photo_size=512,
                          is_flexible=False,  # True If you need to set up Shipping Fee
                          prices=prices_vacancy,
                          start_parameter='time-machine-example',
                          payload='its payload')


@bot.callback_query_handler(lambda c: c.data == 'Telegram', state=FormRub.tg_id)
async def process_rubric_tg(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['tg_id'] = callback_query.message.chat.id
    await FormRub.next()

    async with state.proxy() as data:
        data['rubric'] = 'Telegram'
    await FormRub.next()
    await dp.edit_message_text(chat_id=callback_query.from_user.id,
                               message_id=callback_query.message.message_id,
                               text="<b>Выберите подходящую должность</b>",
                               parse_mode=telegram.ParseMode.HTML,
                               reply_markup=buttons.tg)


@bot.callback_query_handler(lambda c: c.data and c.data.startswith('tg'), state=FormRub.position2)
async def process_position_tg(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['position2'] = callback_query.data[3:]

    await testing.save_rubric(data['tg_id'], data['rubric'], data['position2'])
    await state.finish()
    await dp.send_invoice(callback_query.message.chat.id,
                          title='Размещение вакансии',
                          description='Оплата за размещение вакансии - 1000₽.\n'
                                      'Все средства сразу уходят в рекламу нашего проекта, чтобы ещё больше '
                                      'соискателей узнали о вашем предложении.',
                          provider_token=PAYMENTS_PROVIDER_TOKEN,
                          currency='rub',
                          photo_url='https://centersoveta.ru/wp-content/uploads/2019/03/vosstanovlenie-na-rabote.png',
                          photo_height=1126,  # !=0/None or picture won't be shown
                          photo_width=2000,
                          photo_size=512,
                          is_flexible=False,  # True If you need to set up Shipping Fee
                          prices=prices_vacancy,
                          start_parameter='time-machine-example',
                          payload='its payload')


@bot.callback_query_handler(lambda c: c.data == 'Менеджмент', state=FormRub.tg_id)
async def process_rubric_mg(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['tg_id'] = callback_query.message.chat.id
    await FormRub.next()

    async with state.proxy() as data:
        data['rubric'] = 'Менеджмент'
    await FormRub.next()
    await dp.edit_message_text(chat_id=callback_query.from_user.id,
                               message_id=callback_query.message.message_id,
                               text="<b>Выберите подходящую должность</b>",
                               parse_mode=telegram.ParseMode.HTML,
                               reply_markup=buttons.manage)


@bot.callback_query_handler(lambda c: c.data and c.data.startswith('manage'), state=FormRub.position2)
async def process_position_manage(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['position2'] = callback_query.data[7:]

    await testing.save_rubric(data['tg_id'], data['rubric'], data['position2'])
    await state.finish()
    await dp.send_invoice(callback_query.message.chat.id,
                          title='Размещение вакансии',
                          description='Оплата за размещение вакансии - 1000₽.\n'
                                      'Все средства сразу уходят в рекламу нашего проекта, чтобы ещё больше '
                                      'соискателей узнали о вашем предложении.',
                          provider_token=PAYMENTS_PROVIDER_TOKEN,
                          currency='rub',
                          photo_url='https://centersoveta.ru/wp-content/uploads/2019/03/vosstanovlenie-na-rabote.png',
                          photo_height=1126,  # !=0/None or picture won't be shown
                          photo_width=2000,
                          photo_size=512,
                          is_flexible=False,  # True If you need to set up Shipping Fee
                          prices=prices_vacancy,
                          start_parameter='time-machine-example',
                          payload='its payload')


@bot.callback_query_handler(lambda c: c.data == 'Оптимизация (SEO)', state=FormRub.tg_id)
async def process_rubric_seo(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['tg_id'] = callback_query.message.chat.id
    await FormRub.next()

    async with state.proxy() as data:
        data['rubric'] = 'Оптимизация (SEO)'
    await FormRub.next()
    await dp.edit_message_text(chat_id=callback_query.from_user.id,
                               message_id=callback_query.message.message_id,
                               text="<b>Выберите подходящую должность</b>",
                               parse_mode=telegram.ParseMode.HTML,
                               reply_markup=buttons.seo)


@bot.callback_query_handler(lambda c: c.data and c.data.startswith('seo'), state=FormRub.position2)
async def process_position_seo(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['position2'] = callback_query.data[4:]

    await testing.save_rubric(data['tg_id'], data['rubric'], data['position2'])
    await state.finish()
    await dp.send_invoice(callback_query.message.chat.id,
                          title='Размещение вакансии',
                          description='Оплата за размещение вакансии - 1000₽.\n'
                                      'Все средства сразу уходят в рекламу нашего проекта, чтобы ещё больше '
                                      'соискателей узнали о вашем предложении.',
                          provider_token=PAYMENTS_PROVIDER_TOKEN,
                          currency='rub',
                          photo_url='https://centersoveta.ru/wp-content/uploads/2019/03/vosstanovlenie-na-rabote.png',
                          photo_height=1126,  # !=0/None or picture won't be shown
                          photo_width=2000,
                          photo_size=512,
                          is_flexible=False,  # True If you need to set up Shipping Fee
                          prices=prices_vacancy,
                          start_parameter='time-machine-example',
                          payload='its payload')


@bot.callback_query_handler(lambda c: c.data == 'Фотография', state=FormRub.tg_id)
async def process_rubric_photo(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['tg_id'] = callback_query.message.chat.id
    await FormRub.next()

    async with state.proxy() as data:
        data['rubric'] = 'Фотография'
    await FormRub.next()
    await dp.edit_message_text(chat_id=callback_query.from_user.id,
                               message_id=callback_query.message.message_id,
                               text="<b>Выберите подходящую должность</b>",
                               parse_mode=telegram.ParseMode.HTML,
                               reply_markup=buttons.photo)


@bot.callback_query_handler(lambda c: c.data and c.data.startswith('photo'), state=FormRub.position2)
async def process_position_photo(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['position2'] = callback_query.data[6:]

    await testing.save_rubric(data['tg_id'], data['rubric'], data['position2'])
    await state.finish()
    await dp.send_invoice(callback_query.message.chat.id,
                          title='Размещение вакансии',
                          description='Оплата за размещение вакансии - 1000₽.\n'
                                      'Все средства сразу уходят в рекламу нашего проекта, чтобы ещё больше '
                                      'соискателей узнали о вашем предложении.',
                          provider_token=PAYMENTS_PROVIDER_TOKEN,
                          currency='rub',
                          photo_url='https://centersoveta.ru/wp-content/uploads/2019/03/vosstanovlenie-na-rabote.png',
                          photo_height=1126,  # !=0/None or picture won't be shown
                          photo_width=2000,
                          photo_size=512,
                          is_flexible=False,  # True If you need to set up Shipping Fee
                          prices=prices_vacancy,
                          start_parameter='time-machine-example',
                          payload='its payload')


@bot.callback_query_handler(lambda c: c.data == 'Аудио/Видео', state=FormRub.tg_id)
async def process_rubric_vd(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['tg_id'] = callback_query.message.chat.id
    await FormRub.next()

    async with state.proxy() as data:
        data['rubric'] = 'Аудио/Видео'
    await FormRub.next()
    await dp.edit_message_text(chat_id=callback_query.from_user.id,
                               message_id=callback_query.message.message_id,
                               text="<b>Выберите подходящую должность</b>",
                               parse_mode=telegram.ParseMode.HTML,
                               reply_markup=buttons.video)


@bot.callback_query_handler(lambda c: c.data and c.data.startswith('video'), state=FormRub.position2)
async def process_position_video(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['position2'] = callback_query.data[6:]

    await testing.save_rubric(data['tg_id'], data['rubric'], data['position2'])
    await state.finish()
    await dp.send_invoice(callback_query.message.chat.id,
                          title='Размещение вакансии',
                          description='Оплата за размещение вакансии - 1000₽.\n'
                                      'Все средства сразу уходят в рекламу нашего проекта, чтобы ещё больше '
                                      'соискателей узнали о вашем предложении.',
                          provider_token=PAYMENTS_PROVIDER_TOKEN,
                          currency='rub',
                          photo_url='https://centersoveta.ru/wp-content/uploads/2019/03/vosstanovlenie-na-rabote.png',
                          photo_height=1126,  # !=0/None or picture won't be shown
                          photo_width=2000,
                          photo_size=512,
                          is_flexible=False,  # True If you need to set up Shipping Fee
                          prices=prices_vacancy,
                          start_parameter='time-machine-example',
                          payload='its payload')


@bot.callback_query_handler(lambda c: c.data == 'Переводы', state=FormRub.tg_id)
async def process_rubric_tr(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['tg_id'] = callback_query.message.chat.id
    await FormRub.next()

    async with state.proxy() as data:
        data['rubric'] = 'Переводы'
    await FormRub.next()
    await dp.edit_message_text(chat_id=callback_query.from_user.id,
                               message_id=callback_query.message.message_id,
                               text="<b>Выберите подходящую должность</b>",
                               parse_mode=telegram.ParseMode.HTML,
                               reply_markup=buttons.tl)


@bot.callback_query_handler(lambda c: c.data and c.data.startswith('tl'), state=FormRub.position2)
async def process_position_tl(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['position2'] = callback_query.data[3:]

    await testing.save_rubric(data['tg_id'], data['rubric'], data['position2'])
    await state.finish()
    await dp.send_invoice(callback_query.message.chat.id,
                          title='Размещение вакансии',
                          description='Оплата за размещение вакансии - 1000₽.\n'
                                      'Все средства сразу уходят в рекламу нашего проекта, чтобы ещё больше '
                                      'соискателей узнали о вашем предложении.',
                          provider_token=PAYMENTS_PROVIDER_TOKEN,
                          currency='rub',
                          photo_url='https://centersoveta.ru/wp-content/uploads/2019/03/vosstanovlenie-na-rabote.png',
                          photo_height=1126,  # !=0/None or picture won't be shown
                          photo_width=2000,
                          photo_size=512,
                          is_flexible=False,  # True If you need to set up Shipping Fee
                          prices=prices_vacancy,
                          start_parameter='time-machine-example',
                          payload='its payload')


@bot.callback_query_handler(lambda c: c.data == '3D Графика', state=FormRub.tg_id)
async def process_rubric_3d(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['tg_id'] = callback_query.message.chat.id
    await FormRub.next()

    async with state.proxy() as data:
        data['rubric'] = '3D Графика'
    await FormRub.next()
    await dp.edit_message_text(chat_id=callback_query.from_user.id,
                               message_id=callback_query.message.message_id,
                               text="<b>Выберите подходящую должность</b>",
                               parse_mode=telegram.ParseMode.HTML,
                               reply_markup=buttons.gr3d)


@bot.callback_query_handler(lambda c: c.data and c.data.startswith('gr3d'), state=FormRub.position2)
async def process_position_gr3d(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['position2'] = callback_query.data[5:]

    await testing.save_rubric(data['tg_id'], data['rubric'], data['position2'])
    await state.finish()
    await dp.send_invoice(callback_query.message.chat.id,
                          title='Размещение вакансии',
                          description='Оплата за размещение вакансии - 1000₽.\n'
                                      'Все средства сразу уходят в рекламу нашего проекта, чтобы ещё больше '
                                      'соискателей узнали о вашем предложении.',
                          provider_token=PAYMENTS_PROVIDER_TOKEN,
                          currency='rub',
                          photo_url='https://centersoveta.ru/wp-content/uploads/2019/03/vosstanovlenie-na-rabote.png',
                          photo_height=1126,  # !=0/None or picture won't be shown
                          photo_width=2000,
                          photo_size=512,
                          is_flexible=False,  # True If you need to set up Shipping Fee
                          prices=prices_vacancy,
                          start_parameter='time-machine-example',
                          payload='its payload')


@bot.callback_query_handler(lambda c: c.data == 'Анимация и флеш', state=FormRub.tg_id)
async def process_rubric_flash(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['tg_id'] = callback_query.message.chat.id
    await FormRub.next()

    async with state.proxy() as data:
        data['rubric'] = 'Анимация и флеш'
    await FormRub.next()
    await dp.edit_message_text(chat_id=callback_query.from_user.id,
                               message_id=callback_query.message.message_id,
                               text="<b>Выберите подходящую должность</b>",
                               parse_mode=telegram.ParseMode.HTML,
                               reply_markup=buttons.flash)


@bot.callback_query_handler(lambda c: c.data and c.data.startswith('flash'), state=FormRub.position2)
async def process_position_flash(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['position2'] = callback_query.data[6:]

    await testing.save_rubric(data['tg_id'], data['rubric'], data['position2'])
    await state.finish()
    await dp.send_invoice(callback_query.message.chat.id,
                          title='Размещение вакансии',
                          description='Оплата за размещение вакансии - 1000₽.\n'
                                      'Все средства сразу уходят в рекламу нашего проекта, чтобы ещё больше '
                                      'соискателей узнали о вашем предложении.',
                          provider_token=PAYMENTS_PROVIDER_TOKEN,
                          currency='rub',
                          photo_url='https://centersoveta.ru/wp-content/uploads/2019/03/vosstanovlenie-na-rabote.png',
                          photo_height=1126,  # !=0/None or picture won't be shown
                          photo_width=2000,
                          photo_size=512,
                          is_flexible=False,  # True If you need to set up Shipping Fee
                          prices=prices_vacancy,
                          start_parameter='time-machine-example',
                          payload='its payload')


@bot.callback_query_handler(lambda c: c.data == 'Разработка игр', state=FormRub.tg_id)
async def process_rubric_gm(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['tg_id'] = callback_query.message.chat.id
    await FormRub.next()

    async with state.proxy() as data:
        data['rubric'] = 'Разработка игр'
    await FormRub.next()
    await dp.edit_message_text(chat_id=callback_query.from_user.id,
                               message_id=callback_query.message.message_id,
                               text="<b>Выберите подходящую должность</b>",
                               parse_mode=telegram.ParseMode.HTML,
                               reply_markup=buttons.game)


@bot.callback_query_handler(lambda c: c.data and c.data.startswith('game'), state=FormRub.position2)
async def process_position_game(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['position2'] = callback_query.data[5:]

    await testing.save_rubric(data['tg_id'], data['rubric'], data['position2'])
    await state.finish()
    await dp.send_invoice(callback_query.message.chat.id,
                          title='Размещение вакансии',
                          description='Оплата за размещение вакансии - 1000₽.\n'
                                      'Все средства сразу уходят в рекламу нашего проекта, чтобы ещё больше '
                                      'соискателей узнали о вашем предложении.',
                          provider_token=PAYMENTS_PROVIDER_TOKEN,
                          currency='rub',
                          photo_url='https://centersoveta.ru/wp-content/uploads/2019/03/vosstanovlenie-na-rabote.png',
                          photo_height=1126,  # !=0/None or picture won't be shown
                          photo_width=2000,
                          photo_size=512,
                          is_flexible=False,  # True If you need to set up Shipping Fee
                          prices=prices_vacancy,
                          start_parameter='time-machine-example',
                          payload='its payload')


@bot.callback_query_handler(lambda c: c.data == 'Архитектура/Интерьер', state=FormRub.tg_id)
async def process_rubric_ah(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['tg_id'] = callback_query.message.chat.id
    await FormRub.next()

    async with state.proxy() as data:
        data['rubric'] = 'Архитектура/Интерьер'
    await FormRub.next()
    await dp.edit_message_text(chat_id=callback_query.from_user.id,
                               message_id=callback_query.message.message_id,
                               text="<b>Выберите подходящую должность</b>",
                               parse_mode=telegram.ParseMode.HTML,
                               reply_markup=buttons.arh)


@bot.callback_query_handler(lambda c: c.data and c.data.startswith('arh'), state=FormRub.position2)
async def process_position_arh(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['position2'] = callback_query.data[4:]

    await testing.save_rubric(data['tg_id'], data['rubric'], data['position2'])
    await state.finish()
    await dp.send_invoice(callback_query.message.chat.id,
                          title='Размещение вакансии',
                          description='Оплата за размещение вакансии - 1000₽.\n'
                                      'Все средства сразу уходят в рекламу нашего проекта, чтобы ещё больше '
                                      'соискателей узнали о вашем предложении.',
                          provider_token=PAYMENTS_PROVIDER_TOKEN,
                          currency='rub',
                          photo_url='https://centersoveta.ru/wp-content/uploads/2019/03/vosstanovlenie-na-rabote.png',
                          photo_height=1126,  # !=0/None or picture won't be shown
                          photo_width=2000,
                          photo_size=512,
                          is_flexible=False,  # True If you need to set up Shipping Fee
                          prices=prices_vacancy,
                          start_parameter='time-machine-example',
                          payload='its payload')


@bot.callback_query_handler(lambda c: c.data == 'Инжиниринг', state=FormRub.tg_id)
async def process_rubric_ig(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['tg_id'] = callback_query.message.chat.id
    await FormRub.next()

    async with state.proxy() as data:
        data['rubric'] = 'Инжиниринг'
    await FormRub.next()
    await dp.edit_message_text(chat_id=callback_query.from_user.id,
                               message_id=callback_query.message.message_id,
                               text="<b>Выберите подходящую должность</b>",
                               parse_mode=telegram.ParseMode.HTML,
                               reply_markup=buttons.ig)


@bot.callback_query_handler(lambda c: c.data and c.data.startswith('ig'), state=FormRub.position2)
async def process_position_ig(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['position2'] = callback_query.data[3:]

    await testing.save_rubric(data['tg_id'], data['rubric'], data['position2'])
    await state.finish()
    await dp.send_invoice(callback_query.message.chat.id,
                          title='Размещение вакансии',
                          description='Оплата за размещение вакансии - 1000₽.\n'
                                      'Все средства сразу уходят в рекламу нашего проекта, чтобы ещё больше '
                                      'соискателей узнали о вашем предложении.',
                          provider_token=PAYMENTS_PROVIDER_TOKEN,
                          currency='rub',
                          photo_url='https://centersoveta.ru/wp-content/uploads/2019/03/vosstanovlenie-na-rabote.png',
                          photo_height=1126,  # !=0/None or picture won't be shown
                          photo_width=2000,
                          photo_size=512,
                          is_flexible=False,  # True If you need to set up Shipping Fee
                          prices=prices_vacancy,
                          start_parameter='time-machine-example',
                          payload='its payload')


@bot.callback_query_handler(lambda c: c.data == 'Аутсорсинг и консалдинг', state=FormRub.tg_id)
async def process_rubric_at(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['tg_id'] = callback_query.message.chat.id
    await FormRub.next()

    async with state.proxy() as data:
        data['rubric'] = 'Аутсорсинг и консалдинг'
    await FormRub.next()
    await dp.edit_message_text(chat_id=callback_query.from_user.id,
                               message_id=callback_query.message.message_id,
                               text="<b>Выберите подходящую должность</b>",
                               parse_mode=telegram.ParseMode.HTML,
                               reply_markup=buttons.source)


@bot.callback_query_handler(lambda c: c.data and c.data.startswith('source'), state=FormRub.position2)
async def process_position_source(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['position2'] = callback_query.data[7:]

    await testing.save_rubric(data['tg_id'], data['rubric'], data['position2'])
    await state.finish()
    await dp.send_invoice(callback_query.message.chat.id,
                          title='Размещение вакансии',
                          description='Оплата за размещение вакансии - 1000₽.\n'
                                      'Все средства сразу уходят в рекламу нашего проекта, чтобы ещё больше '
                                      'соискателей узнали о вашем предложении.',
                          provider_token=PAYMENTS_PROVIDER_TOKEN,
                          currency='rub',
                          photo_url='https://centersoveta.ru/wp-content/uploads/2019/03/vosstanovlenie-na-rabote.png',
                          photo_height=1126,  # !=0/None or picture won't be shown
                          photo_width=2000,
                          photo_size=512,
                          is_flexible=False,  # True If you need to set up Shipping Fee
                          prices=prices_vacancy,
                          start_parameter='time-machine-example',
                          payload='its payload')


@bot.callback_query_handler(lambda c: c.data == 'Обучение и консультации', state=FormRub.tg_id)
async def process_rubric_edu(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['tg_id'] = callback_query.message.chat.id
    await FormRub.next()

    async with state.proxy() as data:
        data['rubric'] = 'Обучение и консультации'
    await FormRub.next()
    await dp.edit_message_text(chat_id=callback_query.from_user.id,
                               message_id=callback_query.message.message_id,
                               text="<b>Выберите подходящую должность</b>",
                               parse_mode=telegram.ParseMode.HTML,
                               reply_markup=buttons.edu)


@bot.callback_query_handler(lambda c: c.data and c.data.startswith('edu'), state=FormRub.position2)
async def process_position_edu(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['position2'] = callback_query.data[4:]

    await testing.save_rubric(data['tg_id'], data['rubric'], data['position2'])
    await state.finish()
    await dp.send_invoice(callback_query.message.chat.id,
                          title='Размещение вакансии',
                          description='Оплата за размещение вакансии - 1000₽.\n'
                                      'Все средства сразу уходят в рекламу нашего проекта, чтобы ещё больше '
                                      'соискателей узнали о вашем предложении.',
                          provider_token=PAYMENTS_PROVIDER_TOKEN,
                          currency='rub',
                          photo_url='https://centersoveta.ru/wp-content/uploads/2019/03/vosstanovlenie-na-rabote.png',
                          photo_height=1126,  # !=0/None or picture won't be shown
                          photo_width=2000,
                          photo_size=512,
                          is_flexible=False,  # True If you need to set up Shipping Fee
                          prices=prices_vacancy,
                          start_parameter='time-machine-example',
                          payload='its payload')


@bot.callback_query_handler(lambda c: c.data == 'Сети и инфосистемы', state=FormRub.tg_id)
async def process_rubric_info(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['tg_id'] = callback_query.message.chat.id
    await FormRub.next()

    async with state.proxy() as data:
        data['rubric'] = 'Сети и инфосистемы'
    await FormRub.next()
    await dp.edit_message_text(chat_id=callback_query.from_user.id,
                               message_id=callback_query.message.message_id,
                               text="<b>Выберите подходящую должность</b>",
                               parse_mode=telegram.ParseMode.HTML,
                               reply_markup=buttons.info)


@bot.callback_query_handler(lambda c: c.data and c.data.startswith('info'), state=FormRub.position2)
async def process_position_info(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['position2'] = callback_query.data[5:]

    await testing.save_rubric(data['tg_id'], data['rubric'], data['position2'])
    await state.finish()
    await dp.send_invoice(callback_query.message.chat.id,
                          title='Размещение вакансии',
                          description='Оплата за размещение вакансии - 1000₽.\n'
                                      'Все средства сразу уходят в рекламу нашего проекта, чтобы ещё больше '
                                      'соискателей узнали о вашем предложении.',
                          provider_token=PAYMENTS_PROVIDER_TOKEN,
                          currency='rub',
                          photo_url='https://centersoveta.ru/wp-content/uploads/2019/03/vosstanovlenie-na-rabote.png',
                          photo_height=1126,  # !=0/None or picture won't be shown
                          photo_width=2000,
                          photo_size=512,
                          is_flexible=False,  # True If you need to set up Shipping Fee
                          prices=prices_vacancy,
                          start_parameter='time-machine-example',
                          payload='its payload')


@bot.callback_query_handler(lambda c: c.data == 'Мобильные приложения', state=FormRub.tg_id)
async def process_rubric_mbo(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['tg_id'] = callback_query.message.chat.id
    await FormRub.next()

    async with state.proxy() as data:
        data['rubric'] = 'Мобильные приложения'
    await FormRub.next()
    await dp.edit_message_text(chat_id=callback_query.from_user.id,
                               message_id=callback_query.message.message_id,
                               text="<b>Выберите подходящую должность</b>",
                               parse_mode=telegram.ParseMode.HTML,
                               reply_markup=buttons.apps)


@bot.callback_query_handler(lambda c: c.data and c.data.startswith('apps'), state=FormRub.position2)
async def process_position_apps(callback_query: types.CallbackQuery, state: FSMContext):
    await dp.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        data['position2'] = callback_query.data[5:]

    await testing.save_rubric(data['tg_id'], data['rubric'], data['position2'])
    await state.finish()
    await dp.send_invoice(callback_query.message.chat.id,
                          title='Размещение вакансии',
                          description='Оплата за размещение вакансии - 1000₽.\n'
                                      'Все средства сразу уходят в рекламу нашего проекта, чтобы ещё больше '
                                      'соискателей узнали о вашем предложении.',
                          provider_token=PAYMENTS_PROVIDER_TOKEN,
                          currency='rub',
                          photo_url='https://centersoveta.ru/wp-content/uploads/2019/03/vosstanovlenie-na-rabote.png',
                          photo_height=1126,  # !=0/None or picture won't be shown
                          photo_width=2000,
                          photo_size=512,
                          is_flexible=False,  # True If you need to set up Shipping Fee
                          prices=prices_vacancy,
                          start_parameter='time-machine-example',
                          payload='its payload')


# Обработка резюме
@bot.callback_query_handler(lambda c: c.data == 'resume')
async def process_callback_resume(callback_query: types.CallbackQuery):
    await dp.answer_callback_query(callback_query.id)
    await dp.send_message(callback_query.from_user.id,
                          'К сожалению, мы генерируем только одну страницу под Ваше резюме, '
                          'поэтому если Вы собирались сделать их несколько, '
                          'то уместите в одном резюме, как можно больше информации.')
    await FormResume.position.set()
    await dp.send_message(callback_query.from_user.id,
                          "<b>Укажите желаемую должность</b>\n"
                          "Чем конкретнее, тем лучше, например: 'Бухгалтер', 'Менеджер по закупкам'",
                          parse_mode=telegram.ParseMode.HTML)


@bot.message_handler(state=FormResume.position)
async def process_position(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['position'] = message.text
    await FormResume.next()

    # m = Resume(
    #     tg_id=tg_id
    # )
    # m.save()

    await dp.send_message(message.from_user.id,
                          "<b>Укажите контактные данные</b>",
                          parse_mode=telegram.ParseMode.HTML)


@bot.message_handler(state=FormResume.contacts)
async def process_contacts(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['contacts'] = message.text

    await FormResume.next()
    await dp.send_message(message.from_user.id,
                          "<b>Сколько желаете зарабатывать?</b>\n"
                          "Укажите сумму, которую вы хотите получать, и аббревиатуру валюты",
                          parse_mode=telegram.ParseMode.HTML)


@bot.message_handler(state=FormResume.money)
async def process_money(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['money'] = message.text

    await FormResume.next()
    await dp.send_message(message.from_user.id,
                          "<b>Опишите опыт работы</b>\n"
                          "Коротко и по сути опишите опыт работы. Начинать стоит с последнего места работы,"
                          " а заканчивать — первым. Если на профессиональном пути вам приходилось работать совсем"
                          " не по той специальности, на которую вы претендуете, эту информацию можно пропустить.\n"
                          "Очень важно лаконично описать, что именно входило в ваши обязанности и "
                          "каких высот вы достигли. Не обязательно использовать сложные конструкции."
                          " Опишите по минимуму, своими словами, что делали, чем занимались, что внедрили и осуществили"
                          " на предыдущей работе. Не забудьте о своих достижениях!",
                          parse_mode=telegram.ParseMode.HTML)


@bot.message_handler(state=FormResume.experience)
async def process_experience(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['experience'] = message.text

    await FormResume.next()
    await dp.send_message(message.from_user.id,
                          "<b>Расскажите про образование</b>\n"
                          "Основное образование указывается либо в обратном хронологическом порядке, "
                          "либо в порядке важности. "
                          "Опишите также и дополнительное образование, если оно пересекается с тем, "
                          "чем вам предстоит заниматься на новой работе.\n"
                          "Пример:\n"
                          "Санкт-Петербургский государственный торгово-экономический институт (2008-2012)",
                          parse_mode=telegram.ParseMode.HTML)


@bot.message_handler(state=FormResume.education)
async def process_education(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['education'] = message.text

    await FormResume.next()
    await dp.send_message(message.from_user.id,
                          "<b>Укажите профессиональные навыки</b>\n"
                          "Пример:\n"
                          "Опыт продаж (4 года в оптовом отделе),\n"
                          "Навыки управления персоналом (коллективы до 30 человек)",
                          parse_mode=telegram.ParseMode.HTML)


@bot.message_handler(state=FormResume.skills)
async def process_skills(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['skills'] = message.text

    await FormResume.next()
    await dp.send_message(message.from_user.id,
                          "<b>Внесите дополнительную информацию</b>\n"
                          "Сюда можно внести прочую информацию, важную для желаемой должности. Не повторяйте те навыки "
                          "о которых вы уже упоминали.\n"
                          "Пример:\n"
                          "Энергичность и коммуникабельность помогают мне проводить эффективные презентации товара;\n"
                          "Усидчива и внимательна, поэтому сохраняю высокую производительность труда.",
                          parse_mode=telegram.ParseMode.HTML)


@bot.message_handler(state=FormResume.info)
async def process_info(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['info'] = message.text

    await FormResume.next()
    await dp.send_message(message.from_user.id,
                          "<b>Ссылка на ваше портфолио</b>\n"
                          "Соберите в одном месте всё ваше портфолио и пришлите ссылку на него.",
                          parse_mode=telegram.ParseMode.HTML)


@bot.message_handler(state=FormResume.portfolio_url)
async def process_portfolio_url(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['portfolio_url'] = message.text
    await FormResume.next()

    async with state.proxy() as data:
        data['tg_id'] = message.chat.id

    await dp.send_invoice(message.chat.id, title='Размещение резюме',
                              description='Оплата за размещение резюме - 2000₽.\n'
                                          'Все средства сразу уходят в рекламу нашего проекта, чтобы ещё больше '
                                          'работодателей узнали о вашем предложении.',
                              provider_token=PAYMENTS_PROVIDER_TOKEN,
                              currency='rub',
                              photo_url='https://centersoveta.ru/wp-content/uploads/2019/03/vosstanovlenie-na-rabote.png',
                              photo_height=1126,  # !=0/None or picture won't be shown
                              photo_width=2000,
                              photo_size=512,
                              is_flexible=False,  # True If you need to set up Shipping Fee
                              prices=prices_resume,
                              start_parameter='time-machine-example',
                              payload='its payload')

    await testing.save_resume(data['tg_id'], data['position'], data['contacts'], data['money'], data['experience'], data['education'], data['skills'],
                              data['info'], data['portfolio_url'])

    await state.finish()


@bot.pre_checkout_query_handler(lambda query: True)
async def checkout(pre_checkout_query: types.PreCheckoutQuery):
    await dp.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                       error_message="Инопланетяне попытались украсть ваш CVV,"
                                                     " но мы успешно защитили вас,"
                                                     " попробуйте оплатить через несколько минут, "
                                                     "нам нужен небольшой отдых.")


@bot.message_handler(content_types=ContentTypes.SUCCESSFUL_PAYMENT)
async def got_payment(message: types.Message):
    await dp.send_message(message.chat.id,
                          'Спасибо за оплату! Эти деньги сразу отправятся на продвижение канала, чтобы '
                          'еще больше работадателей узнали о вашем предложении.',
                          parse_mode='Markdown')
    await testing.payed_update(message.from_user.id)

executor.start_polling(bot, skip_updates=True)
# if __name__ == '__main__':
#     executor.start_polling(bot, skip_updates=True)

