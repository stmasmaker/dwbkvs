import telebot

from telebot import types

from database import SQL
db = SQL('localhost', 'domaildo_usrbbd6', 'e5svFRqYtG8SdB^P=)', 'domaildo_boottrg06')






# Возвращаемся в меню
back_menu_btn = types.KeyboardButton('📋В меню')

menu_back = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu_back.add(back_menu_btn)




# Меню на главной странице
menu = types.ReplyKeyboardMarkup(resize_keyboard=True)

profile_btn = types.KeyboardButton('📃Профиль')
create_check_btn = types.KeyboardButton('💸Создать чек')
guess_course_btn = types.KeyboardButton('📈Угадай курс')
promo_btn = types.KeyboardButton('📜Промокод')
games_btn = types.KeyboardButton('🕹Игры')

menu.add(profile_btn, create_check_btn, guess_course_btn, promo_btn, games_btn)



# Профиль
profile_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)

deposit_btn = types.KeyboardButton('💵Депозит')
withdraw_btn = types.KeyboardButton('💴Вывод')
bot_statictic_btn = types.KeyboardButton('📑Статистика бота')
tickets_btn = types.KeyboardButton('🎫Билеты')
referals_btn = types.KeyboardButton('👨‍💼Реф. система')

profile_menu.add(deposit_btn, withdraw_btn, bot_statictic_btn, back_menu_btn, tickets_btn, referals_btn)


# Купить рекламу
buy_ad = types.InlineKeyboardMarkup()

buy_ad_btn = types.InlineKeyboardButton('Купить рекламу в боте', url='t.me/Check_adm')

buy_ad.add(buy_ad_btn)

# Вернуться в профиль
profile_back = types.ReplyKeyboardMarkup(resize_keyboard=True)

profile_back_btn = types.KeyboardButton('🔙Вернуться')

profile_back.add(profile_back_btn)



# Промокод

promo_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

ins_promo = types.KeyboardButton('✏️Ввести промокод')
crt_promo = types.KeyboardButton('📝Создать промокод')

promo_menu.add(ins_promo, crt_promo, back_menu_btn)


# Выбор при создании промокода
promo_type = types.InlineKeyboardMarkup()

generate_promo = types.InlineKeyboardButton('Сгенерировать', callback_data='Генерация промокода')
self_promo = types.InlineKeyboardButton('Ввести', callback_data='Ввод промокода')
otmena_btn = types.InlineKeyboardButton('Отменить', callback_data='Отмена')

promo_type.add(generate_promo, self_promo, otmena_btn)


# Кнопка отмены
otmena = types.InlineKeyboardMarkup()
otmena.add(otmena_btn)


# Клавиатура для выбора игры
games_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

rooms_btn = types.KeyboardButton('🚪Комнаты')
dice_btn = types.KeyboardButton('🎲Дайс')

games_markup.add(rooms_btn, dice_btn, back_menu_btn)


# Кнопка для дайса
dice_inl_markup = types.InlineKeyboardMarkup()
dice_inl_btn = types.InlineKeyboardButton('🎲', callback_data='dice')
dice_inl_markup.add(dice_inl_btn)



# Клавиатура для игр с комнатами

# def rooms():
#     games = types.InlineKeyboardMarkup(row_width=1)

#     r1 = '1'
#     for i in db.check_len_room('1'):
#         r1 = i
        
    
#     r1 = str(db.check_len_room('1'))
#     r2 = str(db.check_len_room('2'))
#     r3 = str(db.check_len_room('3'))
#     r4 = str(db.check_len_room('4'))
#     r5 = str(db.check_len_room('5'))
#     r6 = str(db.check_len_room('6'))

#     room1 = types.InlineKeyboardButton('1 комната - 1р - ' + r1 + '/5', callback_data='Комната1')
#     room2 = types.InlineKeyboardButton('2 комната - 3р - ' + r2 + '/5', callback_data='Комната2')
#     room3 = types.InlineKeyboardButton('3 комната - 10р - ' + r3 + '/5', callback_data='Комната3')
#     room4 = types.InlineKeyboardButton('4 комната - 30р - ' + r4 + '/5', callback_data='Комната4')
#     room5 = types.InlineKeyboardButton('5 комната - 100р - ' + r5 + '/5', callback_data='Комната5')
#     room6 = types.InlineKeyboardButton('6 комната - 300р - ' + r6 + '/5', callback_data='Комната6')

#     games.add(room1, room2, room3, room4, room5, room6)
#     return games


# Кнопки отмен для игровых комнат

otmena_room1 = types.InlineKeyboardMarkup()
otmena_room_btn1 = types.InlineKeyboardButton('Отмена', callback_data='Отмена игры1')
otmena_room1.add(otmena_room_btn1)

otmena_room2 = types.InlineKeyboardMarkup()
otmena_room_btn2 = types.InlineKeyboardButton('Отмена', callback_data='Отмена игры2')
otmena_room2.add(otmena_room_btn2)

otmena_room3 = types.InlineKeyboardMarkup()
otmena_room_btn3 = types.InlineKeyboardButton('Отмена', callback_data='Отмена игры3')
otmena_room3.add(otmena_room_btn3)

otmena_room4 = types.InlineKeyboardMarkup()
otmena_room_btn4 = types.InlineKeyboardButton('Отмена', callback_data='Отмена игры4')
otmena_room4.add(otmena_room_btn4)

otmena_room5 = types.InlineKeyboardMarkup()
otmena_room_btn5 = types.InlineKeyboardButton('Отмена', callback_data='Отмена игры5')
otmena_room5.add(otmena_room_btn5)

otmena_room6 = types.InlineKeyboardMarkup()
otmena_room_btn6 = types.InlineKeyboardButton('Отмена', callback_data='Отмена игры6')
otmena_room6.add(otmena_room_btn6)



# Кнопка для возвращения в адм панель
return_adm_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
return_adm = types.KeyboardButton('Вернуться в админку')

return_adm_markup.add(return_adm)


# Кнопки для админа
admin_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

admin_btn1 = types.KeyboardButton('Изменение чека')
admin_btn2 = types.KeyboardButton('Изменение промокода')
admin_btn3 = types.KeyboardButton('Выигрыш за курс биткоина')
admin_btn4 = types.KeyboardButton('Изменение билетов')
# admin_btn5 = types.KeyboardButton('Забанить пользователя')
# admin_btn6 = types.KeyboardButton('Разбанить пользователя')
admin_btn7 = types.KeyboardButton('Каналы для подписки')
admin_btn8 = types.KeyboardButton('Изменить баланс пользователю')
admin_btn9 = types.KeyboardButton('Рассылка сообщения')


admin_markup.add(admin_btn1, admin_btn2, admin_btn3, admin_btn4, admin_btn7, admin_btn8, admin_btn9)

# Изменение билетов
tickets_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

top_tickets = types.KeyboardButton('Призовые места')
win_tickets = types.KeyboardButton('Выигрыш за билеты')
dep_tickets = types.KeyboardButton('Билеты за депозит')
room_tickets = types.KeyboardButton('Билеты за игры')
tickets_markup.add(top_tickets, win_tickets, dep_tickets, room_tickets, return_adm)



# Изменение каналов

channels_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

channels_delete = types.KeyboardButton('Удалить канал')
channels_add = types.KeyboardButton('Добавить канал')

channels_markup.add(channels_delete, channels_add, return_adm)

# Изменение чека
check_set = types.ReplyKeyboardMarkup(resize_keyboard=True)

check_set_btn1 = types.KeyboardButton('Минимальную сумму')
check_set_btn2 = types.KeyboardButton('Максимальную сумму')
check_set_btn3 = types.KeyboardButton('Награда за чек')

check_set.add(check_set_btn1, check_set_btn2, check_set_btn3, return_adm)


# Изменение промо
promo_set = types.ReplyKeyboardMarkup(resize_keyboard=True)

promo_set_btn1 = types.KeyboardButton('Минимальную сумму промокода')
promo_set_btn2 = types.KeyboardButton('Максимальную сумму промокода')
promo_set_btn3 = types.KeyboardButton('Награда за промокод')
promo_set_btn4 = types.KeyboardButton('Время валидности промокода')

promo_set.add(promo_set_btn1, promo_set_btn2, promo_set_btn3, promo_set_btn4, return_adm)


# Привязка QIWI

qiwi_set = types.InlineKeyboardMarkup(row_width=1)

qiwi_set_btn = types.InlineKeyboardButton('Привязать / Изменить QIWI', callback_data='Привязка киви')
payeer_set_btn = types.InlineKeyboardButton('Привязать / Изменить Payeer', callback_data='Привязка Payeer')

qiwi_set.add(qiwi_set_btn, payeer_set_btn)


# Кнопки для подтверждения \ отказа вывода qiwi
withdraw_keyboard = types.InlineKeyboardMarkup()

withdraw_accept_btn = types.InlineKeyboardButton('Одобрить', callback_data='Вывод одобрен')
withdraw_decline_btn = types.InlineKeyboardButton('Отказ', callback_data='Вывод отказан')

withdraw_keyboard.add(withdraw_accept_btn, withdraw_decline_btn)




# Кнопки для подтверждения \ отказа вывода payeer
withdraw_keyboard_payeer = types.InlineKeyboardMarkup()

withdraw_accept_payeer_btn = types.InlineKeyboardButton('Отправлено', callback_data='Вывод одобрен pay')
withdraw_decline_payeer_btn = types.InlineKeyboardButton('Отказ', callback_data='Вывод отказан pay')

withdraw_keyboard_payeer.add(withdraw_accept_payeer_btn, withdraw_decline_payeer_btn)



# клавиатура выбора депозита
qiwi_or_payeer = types.ReplyKeyboardMarkup(resize_keyboard=True)

qiwi_btn = types.KeyboardButton('QIWI')
payeer_btn = types.KeyboardButton('Payeer')

qiwi_or_payeer.add(qiwi_btn, payeer_btn, back_menu_btn)

# Клавиатура выбора вывода
qiwi_or_payeer_with = types.ReplyKeyboardMarkup(resize_keyboard=True)

qiwi_with_btn = types.KeyboardButton('Qiwi')
payeer_with_btn = types.KeyboardButton('Pаyeer')

qiwi_or_payeer_with.add(qiwi_with_btn, payeer_with_btn, back_menu_btn)



# Кнопка для подтверждения подписок

accept = types.InlineKeyboardMarkup()
accept_btn = types.InlineKeyboardButton('Проверить подписки', callback_data='Проверка')
accept.add(accept_btn)


# Кнопки для отправки либо отмены рассылки

send_or_canc = types.InlineKeyboardMarkup()

send_btn = types.InlineKeyboardButton('Отправить', callback_data='send')
canc_btn = types.InlineKeyboardButton('Отменить', callback_data='canc')

send_or_canc.add(send_btn, canc_btn)