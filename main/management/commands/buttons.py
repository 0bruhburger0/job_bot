from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Кнопка назад
inline_btn_1 = InlineKeyboardButton('Назад', callback_data='button_back')
back = InlineKeyboardMarkup().add(inline_btn_1)

inline_kb_full = InlineKeyboardMarkup(row_width=1)

# Кнопка для размещения вакансии
inline_btn_2 = InlineKeyboardButton('🕵️‍♂️ Разместить вакансию', callback_data='vacancy')

# Кнопка для связи
inline_btn_4 = InlineKeyboardButton('📞 Связаться с администартором', callback_data='admin')

# Кнопка для размещения резюме
inline_btn_3 = InlineKeyboardButton('📄 Разместить резюме', callback_data='resume')


inline_kb_full.add(inline_btn_3, inline_btn_2, inline_btn_4)

back2 = InlineKeyboardButton('Отмена', callback_data='back2')
back_add = InlineKeyboardMarkup().add(back2)

# Кнопки рубрик
markup = InlineKeyboardMarkup(row_width=1)
inline_btn_5 = InlineKeyboardButton('Тексты', callback_data='Тексты')
inline_btn_6 = InlineKeyboardButton('Дизайн/Арт', callback_data='Дизайн/Арт')
inline_btn_7 = InlineKeyboardButton('Реклама и маркетинг', callback_data='Реклама и маркетинг')
inline_btn_8 = InlineKeyboardButton('Полиграфия', callback_data='Полиграфия')
inline_btn_9 = InlineKeyboardButton('Разработка сайтов', callback_data='Разработка сайтов')
inline_btn_10 = InlineKeyboardButton('Программирование', callback_data='Программирование')
inline_btn_11 = InlineKeyboardButton('Telegram', callback_data='Telegram')
inline_btn_12 = InlineKeyboardButton('Менеджмент', callback_data='Менеджмент')
inline_btn_13 = InlineKeyboardButton('Оптимизация (SEO)', callback_data='Оптимизация (SEO)')
inline_btn_14 = InlineKeyboardButton('Фотография', callback_data='Фотография')
inline_btn_15 = InlineKeyboardButton('Аудио/Видео', callback_data='Аудио/Видео')
inline_btn_16 = InlineKeyboardButton('Переводы', callback_data='Переводы')
inline_btn_17 = InlineKeyboardButton('3D Графика', callback_data='3D Графика')
inline_btn_18 = InlineKeyboardButton('Анимация и флеш', callback_data='Анимация и флеш')
inline_btn_19 = InlineKeyboardButton('Разработка игр', callback_data='Разработка игр')
inline_btn_20 = InlineKeyboardButton('Архитектура/Интерьер', callback_data='Архитектура/Интерьер')
inline_btn_21 = InlineKeyboardButton('Инжиниринг', callback_data='Инжиниринг')
inline_btn_22 = InlineKeyboardButton('Аутсорсинг и консалдинг', callback_data='Аутсорсинг и консалдинг')
inline_btn_23 = InlineKeyboardButton('Обучение и консультации', callback_data='Обучение и консультации')
inline_btn_24 = InlineKeyboardButton('Сети и инфосистемы', callback_data='Сети и инфосистемы')
inline_btn_25 = InlineKeyboardButton('Мобильные приложения', callback_data='Мобильные приложения')


markup.add(inline_btn_5, inline_btn_6, inline_btn_7, inline_btn_8, inline_btn_9, inline_btn_10, inline_btn_11, inline_btn_12,
           inline_btn_13, inline_btn_14, inline_btn_15, inline_btn_16, inline_btn_17, inline_btn_18, inline_btn_19,
           inline_btn_20, inline_btn_21, inline_btn_22, inline_btn_23, inline_btn_24, inline_btn_25)


# Кнопки для текстов
texts_btn = InlineKeyboardMarkup(row_width=1)
texts_btn_1 = InlineKeyboardButton('Копирайтинг', callback_data='text_Копирайтинг')
texts_btn_2 = InlineKeyboardButton('Редактирование/Корректура', callback_data='text_Редактирование/Корректура')
texts_btn_3 = InlineKeyboardButton('Расшифровка аудио и видео', callback_data='text_Расшифровка аудио и видео')
texts_btn_4 = InlineKeyboardButton('Рерайтинг', callback_data='text_Рерайтинг')
texts_btn_5 = InlineKeyboardButton('Контент-менеджер', callback_data='text_Контент-менеджер')
texts_btn_6 = InlineKeyboardButton('Статьи', callback_data='text_Статьи')
texts_btn_7 = InlineKeyboardButton('Сканирование и распознование', callback_data='text_Сканирование и распознование')
texts_btn_8 = InlineKeyboardButton('Рефераты/Курсовые/Дипломы', callback_data='text_Рефераты/Курсовые/Дипломы')
texts_btn_9 = InlineKeyboardButton('Постинг', callback_data='text_Постинг')
texts_btn_10 = InlineKeyboardButton('Стихи/Поэмы/Эссе', callback_data='text_Стихи/Поэмы/Эссе')
texts_btn_11 = InlineKeyboardButton('Тексты/Речи/Рапорты', callback_data='text_Тексты/Речи/Рапорты')
texts_btn_12 = InlineKeyboardButton('Тексты на иностарнных языках', callback_data='text_Тексты на иностарнных языках')
texts_btn_13 = InlineKeyboardButton('Создание субтитров', callback_data='text_Создание субтитров')
texts_btn_14 = InlineKeyboardButton('Сценарии', callback_data='text_Сценарии')
texts_btn_15 = InlineKeyboardButton('Слоганы/Нейминг', callback_data='text_Слоганы/Нейминг')
texts_btn_16 = InlineKeyboardButton('Новости/Пресс-релизы', callback_data='text_Новости/Пресс-релизы')
texts_btn_17 = InlineKeyboardButton('Резюме', callback_data='text_Резюме')
texts_btn_18 = InlineKeyboardButton('ТЗ/Help/Мануал', callback_data='text_ТЗ/Help/Мануал')
back_rubric = InlineKeyboardButton('⬅️ Назад', callback_data='back_rubric')

texts_btn.add(
    texts_btn_1,
    texts_btn_2,
    texts_btn_3,
    texts_btn_4,
    texts_btn_5,
    texts_btn_6,
    texts_btn_7,
    texts_btn_8,
    texts_btn_9,
    texts_btn_10,
    texts_btn_11,
    texts_btn_12,
    texts_btn_13,
    texts_btn_14,
    texts_btn_15,
    texts_btn_16,
    texts_btn_17,
    texts_btn_18,
    back_rubric
)


design = InlineKeyboardMarkup(row_width=1)
design_sites = InlineKeyboardButton('Дизайн сайтов', callback_data='design Дизайн сайтов')
logo = InlineKeyboardButton('Логотипы', callback_data='design_Логотипы')
draw = InlineKeyboardButton('Рисунки и иллюстрации', callback_data='design Рисунки и иллюстрации')
poligraph_design = InlineKeyboardButton('Полиграфический дизайн', callback_data='design_Полиграфический дизайн')
interier = InlineKeyboardButton('Интерьеры', callback_data='design_Интерьеры')
banner = InlineKeyboardButton('Баннеры', callback_data='design_Баннеры')
vector = InlineKeyboardButton('Векторная графика', callback_data='design_Векторная графика')
firm_style = InlineKeyboardButton('Фирменный стиль', callback_data='design Фирменный стиль')
hero_2d = InlineKeyboardButton('2D Персонажи', callback_data='design_2D Персонажи')
presents = InlineKeyboardButton('Презентации', callback_data='design_Презентации')
animation_2d = InlineKeyboardButton('2D Анимация', callback_data='design_2D Анимация')
design_pack = InlineKeyboardButton('Дизайн упаковки', callback_data='design_Дизайн упаковки')
lifedraw = InlineKeyboardButton('Живопись', callback_data='design_Живопись')
open_ad = InlineKeyboardButton('Наружная реклама', callback_data='design_Наружная реклама')
landscape = InlineKeyboardButton('Ландшафтный дизайн/Генплан', callback_data='design_Ландшафтный дизайн/Генплан')
hand_made = InlineKeyboardButton('Хенд-мейд', callback_data='design_Хенд-мейд')
illistr_3d = InlineKeyboardButton('3D Иллюстрации', callback_data='design_3D Иллюстрации')
icons = InlineKeyboardButton('Иконки', callback_data='design_Иконки')
design_apps = InlineKeyboardButton('Дизайн интерфейсов приложений', callback_data='design_Дизайн интерфейсов приложений')
interface = InlineKeyboardButton('Интерфейсы', callback_data='design_Интерфейсы')
hero_3d = InlineKeyboardButton('3D Персонажи', callback_data='design_3D Персонажи')
clo_design = InlineKeyboardButton('Трикотажный и текстильный дизайн', callback_data='design_Трикотажный и текстильный дизайн')
concept_art = InlineKeyboardButton('Концепт-арт', callback_data='design_Концепт-арт')
prom_design = InlineKeyboardButton('Промышленный дизайн', callback_data='design_Промышленный дизайн')
pixel_art = InlineKeyboardButton('Пиксел-арт', callback_data='design_Пиксел-арт')
tehnic_design = InlineKeyboardButton('Технический дизайнер', callback_data='design_Технический дизайнер')
comics = InlineKeyboardButton('Комиксы', callback_data='design_Комиксы')
graffiti = InlineKeyboardButton('Граффити', callback_data='design_Граффити')
inograph = InlineKeyboardButton('Инографика', callback_data='design_Инографика')
design_stands = InlineKeyboardButton('Дизайн выставочных стендов', callback_data='design_Дизайн выставочных стендов')
cart_graph = InlineKeyboardButton('Картография', callback_data='design_Картография')
fonts = InlineKeyboardButton('Разработка шрифтов', callback_data='design_Разработка шрифтов')
design_stitch = InlineKeyboardButton('Дизайнер машинной вышивки', callback_data='design_Дизайнер машинной вышивки')
airograph = InlineKeyboardButton('Аэрография', callback_data='design_Аэрография')

design.add(
    design_sites, logo, draw, poligraph_design, poligraph_design, interier, banner,
    vector, firm_style, hero_2d, presents, animation_2d, design_pack, lifedraw, open_ad, landscape,
    hand_made, illistr_3d, icons, design_apps, interface, hero_3d, clo_design, concept_art, prom_design,
    pixel_art, tehnic_design, comics, graffiti, inograph, design_stands, cart_graph, fonts, design_stitch, airograph, back_rubric
)


# Кнопки для рекламы и маркетинга
ad = InlineKeyboardMarkup(row_width=1)
ad_1 = InlineKeyboardButton('SMM', callback_data='ad SMM')
ad_2 = InlineKeyboardButton('Контекстная реклама', callback_data='ad Контекстная реклама')
ad_3 = InlineKeyboardButton('Сбор и обработка информации', callback_data='ad Сбор и обработка информации')
ad_4 = InlineKeyboardButton('Продажи и генерация лидов', callback_data='ad Продажи и генерация лидов')
ad_5 = InlineKeyboardButton('Креатив', callback_data='ad Креатив')
ad_6 = InlineKeyboardButton('PR-менеджмент', callback_data='ad PR-менеджмент')
ad_7 = InlineKeyboardButton('Рекламные концепции', callback_data='ad Рекламные концепции')
ad_8 = InlineKeyboardButton('Телемаркетинг', callback_data='ad Телемаркетинг')
ad_9 = InlineKeyboardButton('Исследования рынка и опросы', callback_data='ad Исследования рынка и опросы')
ad_10 = InlineKeyboardButton('SMO', callback_data='ad SMO')
ad_11 = InlineKeyboardButton('Исследования', callback_data='ad Исследования')
ad_12 = InlineKeyboardButton('Организация мероприятий', callback_data='ad Организация мероприятий')
ad_13 = InlineKeyboardButton('Медиапланирование', callback_data='ad Медиапланирование')
ad_14 = InlineKeyboardButton('Промо-персонал', callback_data='ad Промо-персонал')

ad.add(
    ad_1,
    ad_2,
    ad_3,
    ad_4,
    ad_5,
    ad_6,
    ad_7,
    ad_8,
    ad_9,
    ad_10,
    ad_11,
    ad_12,
    ad_13,
    ad_14,
    back_rubric
)


# Полиграфия
pg = InlineKeyboardMarkup(row_width=1)
pg_1 = InlineKeyboardButton('Полиграфический дизайн', callback_data='pg Полиграфический дизайн')
pg_2 = InlineKeyboardButton('Дизайн упаковки', callback_data='pg Дизайн упаковки')
pg_3 = InlineKeyboardButton('Полиграфическая верстка', callback_data='pg Полиграфическая верстка')
pg_4 = InlineKeyboardButton('Допечатная подготовка', callback_data='pg Допечатная подготовка')
pg_5 = InlineKeyboardButton('Верстка электронных изданий', callback_data='pg Верстка электронных изданий')
pg_6 = InlineKeyboardButton('Разработка шрифтов', callback_data='pg Разработка шрифтов')

pg.add(
    pg_1,
    pg_2,
    pg_3,
    pg_4,
    pg_5,
    pg_6,
    back_rubric
)


sites = InlineKeyboardMarkup(row_width=1)
sites_1 = InlineKeyboardButton('Веб-программирование', callback_data='site Веб-программирование')
sites_2 = InlineKeyboardButton('Копирайтинг', callback_data='site Копирайтинг')
sites_3 = InlineKeyboardButton('Дизайн сайтов', callback_data='site Дизайн сайтов')
sites_4 = InlineKeyboardButton('Верстка', callback_data='site Верстка')
sites_5 = InlineKeyboardButton('Сайт «под ключ»', callback_data='site Сайт «под ключ»')
sites_6 = InlineKeyboardButton('Контент-менеджер', callback_data='site Контент-менеджер')
sites_7 = InlineKeyboardButton('Менеджер проектов', callback_data='site Менеджер проектов')
sites_8 = InlineKeyboardButton('Интернет-магазины', callback_data='site Интернет-магазины')
sites_9 = InlineKeyboardButton('QA (тестирование)', callback_data='site QA (тестирование)')
sites_10 = InlineKeyboardButton('Системы администирования (CMS)', callback_data='site Системы администирования (CMS)')
sites_11 = InlineKeyboardButton('Доработка сайтов', callback_data='site Доработка сайтов')
sites_12 = InlineKeyboardButton('Проектирование', callback_data='site Проектирование')
sites_13 = InlineKeyboardButton('Юзабилити-анализ', callback_data='site Юзабилити-анализ')
sites_14 = InlineKeyboardButton('Флеш-сайты', callback_data='site Флеш-сайты')
sites_15 = InlineKeyboardButton('Wap/PDA-сайты', callback_data='site Wap/PDA-сайты')

sites.add(
    sites_1,
    sites_2,
    sites_3,
    sites_4,
    sites_5,
    sites_6,
    sites_7,
    sites_8,
    sites_9,
    sites_10,
    sites_11,
    sites_12,
    sites_13,
    sites_14,
    sites_15,
    back_rubric
)


# Кнопки для программирования
program = InlineKeyboardMarkup(row_width=1)
program_1 = InlineKeyboardButton('Веб-программирование', callback_data='program Веб-программирование')
program_2 = InlineKeyboardButton('Прикладное программирование', callback_data='program Прикладное программирование')
program_3 = InlineKeyboardButton('1С-программирование', callback_data='program 1С-программирование')
program_4 = InlineKeyboardButton('QA (тестирование)', callback_data='program QA (тестирование)')
program_5 = InlineKeyboardButton('Базы данных', callback_data='program Базы данных')
program_6 = InlineKeyboardButton('Системный администратор', callback_data='program Системный администратор')
program_7 = InlineKeyboardButton('Разработка игр', callback_data='program Разработка игр')
program_8 = InlineKeyboardButton('Системное программирование', callback_data='program Системное программирование')
program_9 = InlineKeyboardButton('Программирование для сотовых', callback_data='program Программирование для сотовых')
program_10 = InlineKeyboardButton('Разработка CRM и EPR', callback_data='program Разработка CRM и EPR')
program_11 = InlineKeyboardButton('Плагины/Сценарии/Утилиты', callback_data='program Плагины/Сценарии/Утилиты')
program_12 = InlineKeyboardButton('Встраиваемые системы', callback_data='program Встраиваемые системы')
program_13 = InlineKeyboardButton('Защита информации', callback_data='program Защита информации')
program_14 = InlineKeyboardButton('Интерактивные приложения', callback_data='program Интерактивные приложения')
program_15 = InlineKeyboardButton('Проектирование', callback_data='program Проектирование')
program_16 = InlineKeyboardButton('Управление проектами разработки', callback_data='program Управление проектами')
program_17 = InlineKeyboardButton('Макросы для игр', callback_data='program Макросы для игр')

program.add(
    program_1,
    program_2,
    program_3,
    program_4,
    program_5,
    program_6,
    program_7,
    program_8,
    program_9,
    program_10,
    program_11,
    program_12,
    program_13,
    program_14,
    program_15,
    program_16,
    program_17,
    back_rubric
)

tg = InlineKeyboardMarkup(row_width=1)
tg_1 = InlineKeyboardButton('Рекламные тексты', callback_data='tg Рекламные тексты')
tg_2 = InlineKeyboardButton('Ведение каналов', callback_data='tg Ведение каналов')
tg_3 = InlineKeyboardButton('Продвижение', callback_data='tg Продвижение')
tg_4 = InlineKeyboardButton('Разработка ботов', callback_data='tg Разработка ботов')
tg_5 = InlineKeyboardButton('Консалтинг', callback_data='tg Консалтинг')
tg_6 = InlineKeyboardButton('Разработка стикеров', callback_data='tg Разработка стикеров')

tg.add(
    tg_1,
    tg_2,
    tg_3,
    tg_4,
    tg_5,
    tg_6,
    back_rubric
)

# Кнопка для Менеджмент
manage = InlineKeyboardMarkup(row_width=1)
manage_1 = InlineKeyboardButton('Менеджер проектов', callback_data='manage Менеджер проектов')
manage_2 = InlineKeyboardButton('Менеджер по продажам', callback_data='manage Менеджер по продажам')
manage_3 = InlineKeyboardButton('Менеджер по персоналу', callback_data='manage Менеджер по персоналу')
manage_4 = InlineKeyboardButton('Управление репутацией онлайн', callback_data='manage Управление репутацией онлайн')
manage_5 = InlineKeyboardButton('Арт-директор', callback_data='manage Арт-директор')

manage.add(
    manage_1,
    manage_2,
    manage_3,
    manage_4,
    manage_5,
    back_rubric
)


# Кнопка для Оптимизация (SEO)
seo = InlineKeyboardMarkup(row_width=1)
seo_1 = InlineKeyboardButton('Контекстная реклама', callback_data='seo Контекстная реклама')
seo_2 = InlineKeyboardButton('Поисковые системы', callback_data='seo Поисковые системы')
seo_3 = InlineKeyboardButton('Контент', callback_data='seo Контент')
seo_4 = InlineKeyboardButton('SMO', callback_data='seo SMO')
seo_5 = InlineKeyboardButton('SEM', callback_data='seo SEM')
seo_6 = InlineKeyboardButton('Продажа ссылок', callback_data='seo Продажа ссылок')

seo.add(
    seo_1,
    seo_2,
    seo_3,
    seo_4,
    seo_5,
    seo_6,
    back_rubric
)

# Кнопки для Фотография
photo = InlineKeyboardMarkup(row_width=1)
photo_1 = InlineKeyboardButton('Ретуширование/коллажи', callback_data='photo Ретуширование/коллажи')
photo_2 = InlineKeyboardButton('Рекламная/Постановочная', callback_data='photo Рекламная/Постановочная')
photo_3 = InlineKeyboardButton('Художественная/Арт', callback_data='photo Художественная/Арт')
photo_4 = InlineKeyboardButton('Мероприятия/Репортажи', callback_data='photo Мероприятия/Репортажи')
photo_5 = InlineKeyboardButton('Модели', callback_data='photo Модели')
photo_6 = InlineKeyboardButton('Свадебная фотосъемка', callback_data='photo Свадебная фотосъемка')
photo_7 = InlineKeyboardButton('Архитектура/Интерьер', callback_data='photo Архитектура/Интерьер')
photo_8 = InlineKeyboardButton('Промышленная фотосъемка', callback_data='photo Промышленная фотосъемка')

photo.add(
    photo_1,
    photo_2,
    photo_3,
    photo_4,
    photo_5,
    photo_6,
    photo_7,
    photo_8,
    back_rubric
)

# Кнопки для Аудио/Видео
video = InlineKeyboardMarkup(row_width=1)
video_1 = InlineKeyboardButton('Видеомонтаж', callback_data='video Видеомонтаж')
video_2 = InlineKeyboardButton('Музыка/Звуки', callback_data='video Музыка/Звуки')
video_3 = InlineKeyboardButton('Диктор', callback_data='video Диктор')
video_4 = InlineKeyboardButton('Видеодизайн', callback_data='video Видеодизайн')
video_5 = InlineKeyboardButton('Аудиомонтаж', callback_data='video Аудиомонтаж')
video_6 = InlineKeyboardButton('Видеосъемка', callback_data='video Видеосъемка')
video_7 = InlineKeyboardButton('Создание субтитров', callback_data='video Создание субтитров')
video_8 = InlineKeyboardButton('Видеопрезентации', callback_data='video Видеопрезентации')
video_9 = InlineKeyboardButton('Видеоинфографика', callback_data='video Видеоинфографика')
video_10 = InlineKeyboardButton('Режиссура', callback_data='video Режиссура')
video_11 = InlineKeyboardButton('Свадебное видео', callback_data='video Свадебное видео')
video_12 = InlineKeyboardButton('Кастинг', callback_data='video Кастинг')
video_13 = InlineKeyboardButton('Раскадровки', callback_data='video Раскадровки')

video.add(
    video_1,
    video_2,
    video_3,
    video_4,
    video_5,
    video_6,
    video_7,
    video_8,
    video_9,
    video_10,
    video_11,
    video_12,
    video_13,
    back_rubric
)


# Кнопки для Переводы
tl = InlineKeyboardMarkup(row_width=1)
tl_1 = InlineKeyboardButton('Перевод текстов общей тематики', callback_data='tl Перевод текстов общей тематики')
tl_2 = InlineKeyboardButton('Технический перевод', callback_data='tl Технический перевод')
tl_3 = InlineKeyboardButton('Художественный перевод', callback_data='tl Художественный перевод')
tl_4 = InlineKeyboardButton('Локализация ПО, сайтов и игр', callback_data='tl Локализация ПО, сайтов и игр')
tl_5 = InlineKeyboardButton('Деловая переписка', callback_data='tl Деловая переписка')
tl_6 = InlineKeyboardButton('Редактирование переводов', callback_data='tl Редактирование переводов')
tl_7 = InlineKeyboardButton('Устный перевод', callback_data='tl Устный перевод')

tl.add(
    tl_1,
    tl_2,
    tl_3,
    tl_4,
    tl_5,
    tl_6,
    tl_7,
    back_rubric
)


# Кнопки для 3D Графика
gr3d = InlineKeyboardMarkup(row_width=1)
gr3d_1 = InlineKeyboardButton('3D Моделирование', callback_data='gr3d 3D Моделирование')
gr3d_2 = InlineKeyboardButton('Интерьеры', callback_data='gr3d Интерьеры')
gr3d_3 = InlineKeyboardButton('Видеодизайн', callback_data='gr3d Видеодизайн')
gr3d_4 = InlineKeyboardButton('3D Анимация', callback_data='gr3d 3D Анимация')
gr3d_5 = InlineKeyboardButton('Экстерьеры', callback_data='gr3d Экстерьеры')
gr3d_6 = InlineKeyboardButton('3D Иллюстрации', callback_data='gr3d 3D Иллюстрации')
gr3d_7 = InlineKeyboardButton('Предметная визуализация', callback_data='gr3d Предметная визуализация')
gr3d_8 = InlineKeyboardButton('3D Персонажи', callback_data='gr3d 3D Персонажи')


gr3d.add(
    gr3d_1,
    gr3d_2,
    gr3d_3,
    gr3d_4,
    gr3d_5,
    gr3d_6,
    gr3d_7,
    gr3d_8,
    back_rubric
)


# Кнопки для Анимация и флеш
flash = InlineKeyboardMarkup(row_width=1)
flash_1 = InlineKeyboardButton('Баннеры', callback_data='flash Баннеры')
flash_2 = InlineKeyboardButton('Флеш-баннеры', callback_data='flash Флеш-баннеры')
flash_3 = InlineKeyboardButton('Музыка/Звуки', callback_data='flash Музыка/Звуки')
flash_4 = InlineKeyboardButton('2D Персонажи', callback_data='flash 2D Персонажи')
flash_5 = InlineKeyboardButton('2D Анимация', callback_data='flash 2D Анимация')
flash_6 = InlineKeyboardButton('3D Анимация', callback_data='flash 3D Анимация')
flash_7 = InlineKeyboardButton('3D Персонажи', callback_data='flash 3D Персонажи')
flash_8 = InlineKeyboardButton('Гейм-арт', callback_data='flash Гейм-арт')
flash_9 = InlineKeyboardButton('Flash/Flex-программирование', callback_data='flash Flash/Flex-программирование')
flash_10 = InlineKeyboardButton('Флеш-сайты', callback_data='flash Флеш-сайты')
flash_11 = InlineKeyboardButton('2D Флеш-анимация', callback_data='flash 2D Флеш-анимация')
flash_12 = InlineKeyboardButton('Сценарии для анимации', callback_data='flash Сценарии для анимации')
flash_13 = InlineKeyboardButton('Флеш-графика', callback_data='flash Флеш-графика')
flash_14 = InlineKeyboardButton('Виртуаьные туры', callback_data='flash Виртуаьные туры')
flash_15 = InlineKeyboardButton('Раскадровка', callback_data='flash Раскадровка')

flash.add(
    flash_1,
    flash_2,
    flash_3,
    flash_4,
    flash_5,
    flash_6,
    flash_7,
    flash_8,
    flash_9,
    flash_10,
    flash_11,
    flash_12,
    flash_13,
    flash_14,
    flash_15,
    back_rubric
)


# Кнопки для Разработка игр
game = InlineKeyboardMarkup(row_width=1)
game_1 = InlineKeyboardButton('Рисунки и иллюстрации', callback_data='game Рисунки и иллюстрации')
game_2 = InlineKeyboardButton('2D Анимация', callback_data='game 2D Анимация')
game_3 = InlineKeyboardButton('3D Моделирование', callback_data='game 3D Моделирование')
game_4 = InlineKeyboardButton('Программирование игр', callback_data='game Программирование игр')
game_5 = InlineKeyboardButton('3D Анимация', callback_data='game 3D Анимация')
game_6 = InlineKeyboardButton('Тестирование игр (QA)', callback_data='game Тестирование игр (QA)')
game_7 = InlineKeyboardButton('Пиксел-арт', callback_data='game Пиксел-арт')
game_8 = InlineKeyboardButton('Озвучивание игр', callback_data='game Озвучивание игр')
game_9 = InlineKeyboardButton('Flash/Flex-программирование', callback_data='game Flash/Flex-программирование')
game_10 = InlineKeyboardButton('Концепт/Эскизы', callback_data='game Концепт/Эскизы')
game_11 = InlineKeyboardButton('Макросы для игр', callback_data='game Макросы для игр')
game_12 = InlineKeyboardButton('Видеоролики', callback_data='game Видеоролики')
game_13 = InlineKeyboardButton('Экономика игр', callback_data='game Экономика игр')

game.add(
    game_1,
    game_2,
    game_3,
    game_4,
    game_5,
    game_6,
    game_7,
    game_8,
    game_9,
    game_10,
    game_11,
    game_12,
    game_13,
    back_rubric
)


# Кнопки для Архитектура/Интерьер
arh = InlineKeyboardMarkup(row_width=1)
arh_1 = InlineKeyboardButton('Интерьеры', callback_data='arh Интерьеры')
arh_2 = InlineKeyboardButton('Архитектура', callback_data='arh Архитектура')
arh_3 = InlineKeyboardButton('Визуализация/3D', callback_data='arh Визуализация/3D')
arh_4 = InlineKeyboardButton('Ландшафтный дизайн/Генплан', callback_data='arh Ландшафтный дизайн/Генплан')
arh_5 = InlineKeyboardButton('Макетирование', callback_data='arh Макетирование')

arh.add(
    arh_1,
    arh_2,
    arh_3,
    arh_4,
    arh_5,
    back_rubric
)


# Кнопки для Инжиниринг
ig = InlineKeyboardMarkup(row_width=1)
ig_1 = InlineKeyboardButton('Чертежи/Схемы', callback_data='ig Чертежи/Схемы')
ig_2 = InlineKeyboardButton('Машиностроение', callback_data='ig Машиностроение')
ig_3 = InlineKeyboardButton('Конструкции', callback_data='ig Конструкции')
ig_4 = InlineKeyboardButton('Слаботочные сети/Автоматизация', callback_data='ig Слаботочные сети/Автоматизация')
ig_5 = InlineKeyboardButton('Электрика', callback_data='ig Электрика')
ig_6 = InlineKeyboardButton('Сметы', callback_data='ig Сметы')
ig_7 = InlineKeyboardButton('Отопление/Вентиляция', callback_data='ig Отопление/Вентиляция')
ig_8 = InlineKeyboardButton('Разборка радиоэлектронных систем', callback_data='ig Разборка радио систем')
ig_9 = InlineKeyboardButton('Водоснабжение/Канализация', callback_data='ig Водоснабжение/Канализация')
ig_10 = InlineKeyboardButton('Технология', callback_data='ig Технология')
ig_11 = InlineKeyboardButton('Газоснабжение', callback_data='ig Газоснабжение')

ig.add(
    ig_1,
    ig_2,
    ig_3,
    ig_4,
    ig_5,
    ig_6,
    ig_7,
    ig_8,
    ig_9,
    ig_10,
    ig_11,
    back_rubric
)


# Кнопки для Аутсорсинг и консалтинг
source = InlineKeyboardMarkup(row_width=1)
source_1 = InlineKeyboardButton('Переводы/Тексты', callback_data='source Переводы/Тексты')
source_2 = InlineKeyboardButton('Ввод и обработка данных/текста', callback_data='source Ввод и обработка данных')
source_3 = InlineKeyboardButton('Юриспруденция', callback_data='source Юриспруденция')
source_4 = InlineKeyboardButton('Бухгалтерия', callback_data='source Бухгалтерия')
source_5 = InlineKeyboardButton('Реклама/Маркетинг', callback_data='source Реклама/Маркетинг')
source_6 = InlineKeyboardButton('Разработка сайтов', callback_data='source Разработка сайтов')
source_7 = InlineKeyboardButton('Дизайн/Арт', callback_data='source Дизайн/Арт')
source_8 = InlineKeyboardButton('Репетиторы', callback_data='source Репетиторы')
source_9 = InlineKeyboardButton('Программирование', callback_data='source Программирование')
source_10 = InlineKeyboardButton('Обработка заказов', callback_data='source Обработка заказов')
source_11 = InlineKeyboardButton('Бизнес-консультировнаие', callback_data='source Бизнес-консультировнаие')
source_12 = InlineKeyboardButton('Обработка писем', callback_data='source Обработка писем')
source_13 = InlineKeyboardButton('Обслуживание клиентов', callback_data='source Обслуживание клиентов')
source_14 = InlineKeyboardButton('Оптимизация (SEO)', callback_data='source Оптимизация (SEO)')
source_15 = InlineKeyboardButton('Тех. поддержка', callback_data='source Тех. поддержка')
source_16 = InlineKeyboardButton('Виртуальный ассистент', callback_data='source Виртуальный ассистент')
source_17 = InlineKeyboardButton('Финансовый консультант', callback_data='source Финансовый консультант')
source_18 = InlineKeyboardButton('Поддержка по телефону', callback_data='source Поддержка по телефону')
source_19 = InlineKeyboardButton('Кадровый учет и зарплата', callback_data='source Кадровый учет и зарплата')
source_20 = InlineKeyboardButton('Юзабилити', callback_data='source Юзабилити')
source_21 = InlineKeyboardButton('Статистический анализ', callback_data='source Статистический анализ')
source_22 = InlineKeyboardButton('Управление предприятием', callback_data='source Управление предприятием')
source_23 = InlineKeyboardButton('Обработка платежей', callback_data='source Обработка платежей')

source.add(
    source_1,
    source_2,
    source_3,
    source_4,
    source_5,
    source_6,
    source_7,
    source_8,
    source_9,
    source_10,
    source_11,
    source_12,
    source_13,
    source_14,
    source_15,
    source_16,
    source_17,
    source_18,
    source_19,
    source_20,
    source_21,
    source_22,
    source_23,
    back_rubric
)


# Кнопки для Обучение и консультации
edu = InlineKeyboardMarkup(row_width=1)
edu_1 = InlineKeyboardButton('Рефераты/Курсовые/Дипломы', callback_data='edu Рефераты/Курсовые/Дипломы')
edu_2 = InlineKeyboardButton('Репетиторы', callback_data='edu Репетиторы')
edu_3 = InlineKeyboardButton('Психолог', callback_data='edu Психолог')
edu_4 = InlineKeyboardButton('Иностранные языки', callback_data='edu Иностранные языки')
edu_5 = InlineKeyboardButton('Гуманитарные дисциплины', callback_data='edu Гуманитарные дисциплины')
edu_6 = InlineKeyboardButton('Дошкольное образование', callback_data='edu Дошкольное образование')
edu_7 = InlineKeyboardButton('Технические дисциплины', callback_data='edu Технические дисциплины')
edu_8 = InlineKeyboardButton('Путешествия', callback_data='edu Путешествия')
edu_9 = InlineKeyboardButton('Стилист', callback_data='edu Стилист')

edu.add(
    edu_1,
    edu_2,
    edu_3,
    edu_4,
    edu_5,
    edu_6,
    edu_7,
    edu_8,
    edu_9,
    back_rubric
)


# Кнопки для Сети и инфосистемы
info = InlineKeyboardMarkup(row_width=1)
info_1 = InlineKeyboardButton('Сетевое администрирование', callback_data='info Сетевое администрирование')
info_2 = InlineKeyboardButton('Администрирование баз данных', callback_data='info Администрирование баз данных')
info_3 = InlineKeyboardButton('EPR и CRM интеграции', callback_data='info EPR и CRM интеграции')

info.add(
    info_1,
    info_2,
    info_3,
    back_rubric
)


# Кнопки для Мобильные приложения
apps = InlineKeyboardMarkup(row_width=1)
apps_1 = InlineKeyboardButton('Google Android', callback_data='apps Google Android')
apps_2 = InlineKeyboardButton('IOS', callback_data='apps IOS')
apps_3 = InlineKeyboardButton('Дизайн', callback_data='apps Дизайн')
apps_4 = InlineKeyboardButton('Прототипирование', callback_data='apps Прототипирование')
apps_5 = InlineKeyboardButton('Windows Phone', callback_data='apps Windows Phone')

apps.add(
    apps_1,
    apps_2,
    apps_3,
    apps_4,
    apps_5,
    back_rubric
)
