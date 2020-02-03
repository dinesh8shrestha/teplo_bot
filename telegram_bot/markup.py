from telebot import types

age_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
age_markup_btn1 = types.KeyboardButton('Да')
age_markup_btn2 = types.KeyboardButton('Нет')
age_markup.add(age_markup_btn1, age_markup_btn2)

choose_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
choose_markup_btn1 = types.KeyboardButton('1) Сколько мне нужно кальянов?')
choose_markup_btn2 = types.KeyboardButton('2) Сколько будет стоить?')
choose_markup_btn3 = types.KeyboardButton('3) FAQ: Частые вопросы')
choose_markup.add(choose_markup_btn1, choose_markup_btn2, choose_markup_btn3)

choose_markup_cup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
choose_markup_cup1 = types.KeyboardButton('на классической')
choose_markup_cup2 = types.KeyboardButton('на фруктовой')
choose_markup_cup3 = types.KeyboardButton('микс 50/50')
choose_markup_cup.add(choose_markup_cup1, choose_markup_cup2, choose_markup_cup3)

remove_markup = types.ReplyKeyboardRemove(selective=False)