import telebot
from telebot import apihelper
from telebot import types
import logging
import markup as m

# main variables

TOKEN = "926612370:AAFYeXQwUk8vFDdWNI7_2Yp4k03_RN8dO6M"
apihelper.proxy = {'https': 'socks5://226990439:NhiwhtKM@grsst.s5.opennetwork.cc:999'}
bot = telebot.TeleBot(TOKEN)
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, ' '.join(['Привет,', message.from_user.first_name]))
    bot.send_message(message.chat.id,
                     'Я ваш персональный помощник кальянного кейтеринга TEPLO \nМы доставляем и обслуживаем кальяны '
                     'на ваши мерепреятия по Москве и МО.')
    bot.send_message(message.chat.id,
                     '! Отвечая здесь, вы Даете согласие на обработку персональных данных: *ссылка на наш сайт* ')
    msg = bot.send_message(message.chat.id, 'Чтобы продолжить, подтвердите, что вам уже исполнилось 18 лет',
                           reply_markup=m.age_markup)
    bot.register_next_step_handler(msg, askAge)


def askAge(message):
    chat_id = message.chat.id
    text = message.text
    if text.lower() == 'да':
        msg = bot.send_message(chat_id, 'Отлично! Что хотите узнать?', reply_markup=m.choose_markup)
        bot.register_next_step_handler(msg, choose_question)
    elif text.lower() == 'нет':
        msg = bot.send_message(chat_id, 'Ты слишком мал')
    else:
        msg = bot.send_message(chat_id, 'Выберите вариант да или нет', reply_markup=m.age_markup)
        bot.register_next_step_handler(msg, askAge)  # askSource
        return


@bot.message_handler(commands=['menu'])
def choose_question(message):
    chat_id = message.chat.id
    text = message.text
    if text == '1) Сколько мне нужно кальянов?':
        mes = """Очень правильно, что вы решили уточнить у нас кол-во кальянов, ведь мы отработали уже на сотне мероприятий и смогли выявить идеальную формулу, по которой легко определить точное кол-во кальянов. 
Дело в том, что на мероприятии, как правило, хорошо относятся к кальяну - ровно половина людей, но активных курильщиков - около 50-70% от тех, кто не против "подымить". 
Введите кол-во людей и наш бот выдаст вам точное кол-во кальянов, необходимых на ваше мероприятие. 
Вы всегда можете расчитывать на полученную цифру добавляя или уменьшая на 1-2 кальяна. """
        msg = bot.send_message(chat_id, mes)
        bot.register_next_step_handler(msg, choose_count_people)
    elif text == '2) Сколько будет стоить?':
        mes = 'Напишите, какое количество кальянов необходимо на мероприятии:'
        msg = bot.send_message(chat_id, mes)
        bot.register_next_step_handler(msg, count_hookah)
    elif text == '3) FAQ: Частые вопросы':
        msg = bot.send_message(chat_id, 'Илья скоро придумает')
    else:
        msg = bot.send_message(chat_id, 'Выберите вариант ответа ниже', reply_markup=m.choose_markup)
        bot.register_next_step_handler(msg, choose_question)
        return


@bot.message_handler(commands=['count_hookahs'])
def choose_count_people(message):
    chat_id = message.chat.id
    text = message.text
    if text == '/count_hookahs':
        mes = """Очень правильно, что вы решили уточнить у нас кол-во кальянов, ведь мы отработали уже на сотне мероприятий и смогли выявить идеальную формулу, по которой легко определить точное кол-во кальянов. 
        Дело в том, что на мероприятии, как правило, хорошо относятся к кальяну - ровно половина людей, но активных курильщиков - около 50-70% от тех, кто не против "подымить". 
        Введите кол-во людей и наш бот выдаст вам точное кол-во кальянов, необходимых на ваше мероприятие. 
        Вы всегда можете расчитывать на полученную цифру добавляя или уменьшая на 1-2 кальяна. """
        msg = bot.send_message(chat_id, mes)
        bot.register_next_step_handler(msg, choose_count_people)
        return
    if not text.isdigit():
        msg = bot.send_message(chat_id, 'Количество людей должно быть числом. Введите корректно.')
        bot.register_next_step_handler(msg, choose_count_people)
        return
    if int(text) < 1 or int(text) > 150:
        msg = bot.send_message(chat_id, 'Количество людей должно быть >0 и <150. Введите корректно.')
        bot.register_next_step_handler(msg, choose_count_people)
        return
    import math
    max_count = math.ceil(int(text) / 7) + 1
    min_count = math.floor(int(text) / 7) - 1
    mes = '{}-{} кальянов'.format(min_count, max_count)
    msg = bot.send_message(chat_id, mes)


@bot.message_handler(commands=['cost'])
def start_calculating(message):
    chat_id = message.chat.id
    text = message.text
    mes = 'Напишите, какое количество кальянов необходимо на мероприятии:'
    msg = bot.send_message(chat_id, mes)
    bot.register_next_step_handler(msg, count_hookah)


def count_hookah(message):
    chat_id = message.chat.id
    text = message.text
    if not text.isdigit():
        msg = bot.send_message(chat_id, 'Количество кальянов должно быть числом. Введите корректно.')
        bot.register_next_step_handler(msg, count_hookah)
        return
    if int(text) < 1 or int(text) > 30:
        msg = bot.send_message(chat_id, 'Количество кальянов должно быть >0 и <30. Введите корректно.')
        bot.register_next_step_handler(msg, count_hookah)
        return
    count = int(text)
    msg = bot.send_message(chat_id, 'На какой чаше должны быть кальяны?', reply_markup=m.choose_markup_cup)
    bot.register_next_step_handler(msg, choose_cup, count)


def choose_cup(message, count_hookahs):
    chat_id = message.chat.id
    text = message.text
    if text == 'на классической':
        msg = bot.send_message(chat_id, 'на сколько часов арендуете?')
        bot.register_next_step_handler(msg, choose_hour, count_hookahs, 1)
    elif text == 'на фруктовой':
        msg = bot.send_message(chat_id, 'на сколько часов арендуете?')
        bot.register_next_step_handler(msg, choose_hour, count_hookahs, 3)
    elif text == 'микс 50/50':
        msg = bot.send_message(chat_id, 'на сколько часов арендуете?')
        bot.register_next_step_handler(msg, choose_hour, count_hookahs, 2)
    else:
        msg = bot.send_message(chat_id, 'Выберите вариант ответа ниже', reply_markup=m.choose_markup_cup)
        bot.register_next_step_handler(msg, choose_cup, count_hookahs)
        return


def choose_hour(message, count_hookahs, kind_cup):
    chat_id = message.chat.id
    text = message.text
    if not text.isdigit():
        msg = bot.send_message(chat_id, 'Количество часов должно быть числом. Введите корректно.')
        bot.register_next_step_handler(msg, choose_hour, count_hookahs, kind_cup)
        return
    if int(text) < 1 or int(text) > 30:
        msg = bot.send_message(chat_id, 'Количество часов должно быть >0 и <30. Введите корректно.')
        bot.register_next_step_handler(msg, choose_hour, count_hookahs, kind_cup)
        return
    hour = int(text)
    msg = bot.send_message(chat_id, 'Сколько профессиональных мастеров необходимо?')
    bot.register_next_step_handler(msg, count_masters, count_hookahs, kind_cup, hour)


def count_masters(message, count_hookahs, kind_cup, hour):
    chat_id = message.chat.id
    text = message.text
    if not text.isdigit():
        msg = bot.send_message(chat_id, 'Количество мастеров должно быть числом. Введите корректно.')
        bot.register_next_step_handler(msg, choose_hour, count_hookahs, kind_cup)
        return
    if int(text) < 1 or int(text) > 15:
        msg = bot.send_message(chat_id, 'Количество мастеров должно быть >0 и <15. Введите корректно.')
        bot.register_next_step_handler(msg, choose_hour, count_hookahs, kind_cup)
        return
    masters = int(text)
    msg = bot.send_message(chat_id, 'Напишите ориентировочную дату мероприятия')
    bot.register_next_step_handler(msg, choose_date, count_hookahs, kind_cup, hour, masters)


def choose_date(message, count_hookahs, kind_cup, hour, masters):
    chat_id = message.chat.id
    text = message.text
    import sqlite3
    from sqlalchemy import create_engine
    engine = create_engine('sqlite:///data.db', echo=False)
    t = (count_hookahs, hour, kind_cup)
    mes = engine.execute('SELECT * FROM tariff WHERE hookahs=? AND hours=? AND number_cup=?', t).fetchall()[0][3]
    msg = bot.send_message(chat_id, '{} рублей'.format(mes))


bot.polling(none_stop=True)
