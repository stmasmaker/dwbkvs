import telebot
from telebot import types
from config import bot
from multiprocessing import *
from buttons import menu, profile_menu, profile_back, menu_back, promo_menu, buy_ad, promo_type, otmena, otmena_room1, otmena_room2, otmena_room3, otmena_room4, otmena_room5, otmena_room6, admin_markup, check_set, promo_set, qiwi_set, withdraw_keyboard, qiwi_or_payeer, qiwi_or_payeer_with, withdraw_keyboard_payeer, tickets_markup, accept, channels_markup, return_adm_markup, games_markup, dice_inl_markup,send_or_canc
from clases import check_ref, generate_check, generate_promo, isfloat
import schedule
import time
import datetime
from time import sleep
import requests
import json
# from win_room import check_win
import random
import pymysql
from database import SQL
from light_qiwi import Qiwi, Provider, OperationType, PaymentStatus
import datetime
from datetime import timedelta
import pytz

tz_moscow = pytz.timezone("Europe/Moscow")
one_day = timedelta(-1)
api = Qiwi('31c7352ad0b221d2b30a4bf6e127b5c0', '79602844595')
# 509766197, 
admin = [509766197]
payeer = 'P1020141813'
db = SQL('localhost', 'domaildo_usrbbd6', 'e5svFRqYtG8SdB^P=)', 'domaildo_boottrg06')

def btc_course():
    url = 'https://blockchain.info/ticker'

    r =requests.get(url)

    r_json = r.json()
    btc_course = (r_json['USD']['last'])

    b = []
    for i in db.btc_course():
        map(float, i)
        b.append(float(i[0]))

    b.remove(min(b, key=lambda x:abs(x-btc_course)))
    b.remove(min(b, key=lambda x:abs(x-btc_course)))
    a = min(b, key=lambda x:abs(x-btc_course))
    print(a)
    btc_work(int(a))
    db.date_next()
schedule.every(3).days.at("18:00").do(btc_course)
def one_days():
    db.plus_day()
schedule.every().day.at("00:00").do(one_days)
def check_win(room):

    a = []
    for i in db.list_players(room):
        a.append(int(i[0]))
    result = random.choice(a)
    return result








def tickets_top():
    a = []
    b = db.check_top_ticket()
    for i in db.ticket_win():
        a.append(int(i[0]))
        
    
    for win in range(b):
        if len(a) == b:

            db.add_balance_ticket(int(a[0]), '1')
            ticket_win_send(int(a[0]))
            a.pop(0)
        elif len(a) == b-1:

            db.add_balance_ticket(int(a[0]), '2')
            ticket_win_send(int(a[0]))
            a.pop(0)

        elif len(a) == b-2:

            db.add_balance_ticket(int(a[0]), '3')
            ticket_win_send(int(a[0]))
            a.pop(0)
        elif len(a) == b-3:

            db.add_balance_ticket(int(a[0]), '4')
            ticket_win_send(int(a[0]))
            a.pop(0)
        elif len(a) == b-4:

            db.add_balance_ticket(int(a[0]), '5')
            ticket_win_send(int(a[0]))
            a.pop(0)
    db.zero_tickets()     
schedule.every(10).days.at("12:00").do(tickets_top)



def jack_win():
    a = []
    for i in db.select_jack_quant():
        a.append(int(i[0]))
    a.sort(reverse=True)
    db.jack_win(str(a[0]))
    jackpot_win_send(str(a[0]))
schedule.every().sunday.at("13:00").do(jack_win)







class ScheduleWork():
    def try_work():
        while True:
            schedule.run_pending()
            time.sleep(1)

    def start_process():
        p1 = Process(target=ScheduleWork.try_work, args=())
        p1.start()




def rooms():
    games = types.InlineKeyboardMarkup(row_width=1)

    r1 = str(db.check_len_room('1'))
    r2 = str(db.check_len_room('2'))
    r3 = str(db.check_len_room('3'))
    r4 = str(db.check_len_room('4'))
    #r5 = str(db.check_len_room('5'))
    #r6 = str(db.check_len_room('6'))

    room1 = types.InlineKeyboardButton('1 комната - 1р - ' + r1 + '/5', callback_data='Комната1')
    room2 = types.InlineKeyboardButton('2 комната - 3р - ' + r2 + '/5', callback_data='Комната2')
    room3 = types.InlineKeyboardButton('3 комната - 10р - ' + r3 + '/5', callback_data='Комната3')
    room4 = types.InlineKeyboardButton('4 комната - 30р - ' + r4 + '/5', callback_data='Комната4')
    #room5 = types.InlineKeyboardButton('5 комната - 100р - ' + r5 + '/5', callback_data='Комната5')
    #room6 = types.InlineKeyboardButton('6 комната - 300р - ' + r6 + '/5', callback_data='Комната6')

    games.add(room1, room2, room3, room4)
    return games






@bot.message_handler(commands=['start'])
def new_user(message):
    check_member = db.check_channels()
    check_member_list = []
    for i in check_member:
        check_member_list.append(i[0])

        
    
    if (not db.check_user(message.from_user.id)):
        db.add_user(message.from_user.id, message.from_user.username)
        a = check_ref(message.text)
        if a == '1':
                    
                    

            bot.send_message(message.from_user.id, '😁Привет, подпишись на эти каналы, чтобы продолжить: '+
                                                       '👇👇👇👇👇', reply_markup=accept)
            for channel in check_member_list:
                bot.send_message(message.from_user.id, 't.me/'+channel.split('@')[1])
        elif len(a) == 2:
            db.add_ref(a[1], message.from_user.id)
            
            bot.send_message(message.from_user.id, '😁Привет, подпишись на эти каналы, чтобы продолжить: '+
                                                       '👇👇👇👇👇', reply_markup=accept)
            for channel in check_member_list:
                bot.send_message(message.from_user.id, 't.me/'+channel.split('@')[1])
        elif len(a) == 3:
            db.add_ref(a[1],message.from_user.id)
            db.add_for_check(a[1])
            b = db.check_add(message.from_user.id, a[2],a[1])
            if b == 'not valid':
                bot.send_message(message.from_user.id, 'Увы, но чек недействителен 😔')
                
                bot.send_message(message.from_user.id, '😁Привет, подпишись на эти каналы, чтобы продолжить: '+
                                                       '👇👇👇👇👇', reply_markup=accept)
                for channel in check_member_list:
                    bot.send_message(message.from_user.id, 't.me/'+channel.split('@')[1])
            elif b == 'usernot':
                bot.send_message(message.from_user.id, 'Вы не можете активировать свой-же чек😏')
                
                bot.send_message(message.from_user.id, '😁Привет, подпишись на эти каналы, чтобы продолжить: '+
                                                       '👇👇👇👇👇', reply_markup=accept)
                for channel in check_member_list:
                    bot.send_message(message.from_user.id, 't.me/'+channel.split('@')[1])
            elif b == 'time not end':
                bot.send_message(message.from_user.id, 'Вы можете активировать чек только 1 раз в час🤨')
                
                bot.send_message(message.from_user.id, '😁Привет, подпишись на эти каналы, чтобы продолжить: '+
                                                       '👇👇👇👇👇', reply_markup=accept)
                for channel in check_member_list:
                    bot.send_message(message.from_user.id, 't.me/'+channel.split('@')[1])
            elif a == 'failed':
                bot.send_message(message.from_user.id, '😔 Произошла ошибка, попробуйте чуть позже ')
            else:
                bot.send_message(message.from_user.id, 'Вы активировали чек на сумму: '+ b +' RUB 🤑')

                if db.check_crt(a[2]) != 'failed':    
                    bot.send_message(db.check_crt(a[2]), '@'+ message.from_user.username + ' активировал ваш чек!')
                        
                    bot.send_message(message.from_user.id, '😁Привет, подпишись на эти каналы, чтобы продолжить: '+
                                                        '👇👇👇👇👇', reply_markup=accept)
                    for channel in check_member_list:
                        bot.send_message(message.from_user.id, 't.me/'+channel.split('@')[1])
                elif db.check_crt(a[2]) == 'failed':
                    bot.send_message(message.from_user.id, '😁Привет, подпишись на эти каналы, чтобы продолжить: '+
                                                        '👇👇👇👇👇', reply_markup=accept)
                    for channel in check_member_list:
                        bot.send_message(message.from_user.id, 't.me/'+channel.split('@')[1])
        
    elif (db.check_user(message.from_user.id) == True):
        if db.check_subs(message.from_user.id) == 'ok':
            a = check_ref(message.text)
            if len(a) == 1:
                bot.send_message(message.from_user.id,'С возвращением!😊', reply_markup=menu)
            elif len(a) == 2:
                if db.check_ref(message.from_user.id) != None:
                    bot.send_message(message.from_user.id,'С возвращением!😊', reply_markup=menu)
                elif db.check_ref(message.from_user.id) == None:
                    bot.send_message(message.from_user.id,'С возвращением!😊', reply_markup=menu)
            elif len(a) == 3:
                b = db.check_add(message.from_user.id, a[2], a[1])
                if b == 'not valid':
                    bot.send_message(message.from_user.id, 'Увы, но чек недействителен 😔', reply_markup=menu)
                elif b == 'usernot':
                    bot.send_message(message.from_user.id, 'Вы не можете активировать свой-же чек😏', reply_markup=menu)
                elif b == 'time not end':
                    bot.send_message(message.from_user.id, 'Вы можете активировать чек только 1 раз в час🤨', reply_markup=menu)
                else:
                    if db.check_crt(a[2]) != 'failed':
                        bot.send_message(message.from_user.id, 'Вы активировали чек на сумму: '+ b +' RUB 🤑', reply_markup=menu)
                        bot.send_message(db.check_crt(a[2]), '@'+ message.from_user.username + ' активировал ваш чек!')
                    elif db.check_crt(a[2]) == 'failed':
                        bot.send_message(message.from_user.id, 'Чек недействителен', reply_markup=menu)
            elif a == 'failed':
                bot.send_message(message.from_user.id, '😔 Произошла ошибка, попробуйте чуть позже')
        elif db.check_subs(message.from_user.id) == 'no':
            bot.send_message(message.from_user.id, 'Вы не подписаны на каналы!', reply_markup=accept)
            for channel in check_member_list:
                bot.send_message(message.from_user.id,'t.me/'+channel.split('@')[1])

    



@bot.message_handler(commands=['admin'])
def admins(message):
    if message.from_user.id in admin:
        bot.send_message(message.from_user.id, 'Вы вошли в админ панель', reply_markup=admin_markup)
    else:
        bot.send_message(message.from_user.id, 'Вы не администратор!😑')


@bot.message_handler(content_types=['text'])
def general(message):
    check_member = db.check_channels()
    check_member_list = []
    for i in check_member:
        check_member_list.append(i[0])

    # Все, связанное с профилем
    if db.check_subs(message.from_user.id) == 'ok':
        if message.text == '📃Профиль':
            try:
                a = db.check_qiwi_num(message.from_user.id)
                if a != 'not qiwi':
                    bot.send_message(message.from_user.id, '<b>💵Ваш баланс</b>: '+ db.check_balance(message.from_user.id) + ' RUB \n' +
                                                        '<b>💸Доступно для вывода</b>: '+ db.check_balance(message.from_user.id) + ' RUB \n'+
                                                        '<b>🎫Билетов</b>: '+ db.check_ticket(message.from_user.id) + ' \n'+
                                                        # '<b>На выводе</b>: '+ db.check_on_withdraw(message.from_user.id) +' RUB \n' +
                                                        # '<b>Заработано</b>: '+ db.check_earn(message.from_user.id) +' RUB \n '+
                                                        '<b>QIWI кошелек</b>: '+ db.check_qiwi_num(message.from_user.id) + ' \n'+
                                                        '<b>Payeer номер счета</b>:'+ db.check_payeer_num(message.from_user.id), reply_markup=profile_menu, parse_mode='html')
                    bot.send_message(message.from_user.id, 'Если вы хотите изменить свой QIWI кошелек - нажмите на кнопку ниже: ', reply_markup=qiwi_set)
                elif a == 'not qiwi':
                    bot.send_message(message.from_user.id, '<b>💵Ваш баланс</b>: '+ db.check_balance(message.from_user.id) + ' RUB \n' +
                                                        '<b>💸Доступно для вывода</b>: '+ db.check_balance(message.from_user.id) + ' RUB \n'+
                                                        '<b>🎫Билетов</b>: '+ db.check_ticket(message.from_user.id) + ' \n'+
                                                        # '<b>На выводе</b>: '+ db.check_on_withdraw(message.from_user.id) +' RUB \n' +
                                                        # '<b>Заработано</b>: '+ db.check_earn(message.from_user.id) +' RUB \n '+
                                                        '<b>QIWI кошелек</b>: '+ db.check_qiwi_num(message.from_user.id) + ' \n'+
                                                        '<b>Payeer номер счета</b>:'+ db.check_payeer_num(message.from_user.id), reply_markup=profile_menu, parse_mode='html')
                    bot.send_message(message.from_user.id, 'Привяжите QIWI кошелек по кнопке ниже:', reply_markup=qiwi_set)
            except Exception as ex:
                print(ex)
        elif message.text == '👨‍💼Реф. система':
            a = int(db.check_referals(message.from_user.id))*0.5
            bot.send_message(message.from_user.id, '🧸За каждого пользователя, которого вы привели, мы платим по 50 копеек, которые доступны для вывода. \n'+
                                                   ' \n'+
                                                   '👨‍💼Приглашено рефералов: '+ db.check_referals(message.from_user.id) +' Пользователей \n'+
                                                   '💰Получено рублей: '+ str(a) + ' \n'
                                                   ' \n'+
                                                   '🔋Ваш доход ничем не ограничен: создавайте статьи, пишите посты на каналах и зарабатывайте реальные деньги. \n'
                                                   'Ваша ссылка, для приглашения рефералов: http://t.me/promocheck_bot?start=' + db.crt_ref(message.from_user.id), parse_mode='html')
        elif message.text == '💵Депозит':
            try:
                bot.send_message(message.from_user.id, 'Выберите платежную систему:', reply_markup=qiwi_or_payeer)
            except Exception as ex:
                print(ex)
        elif message.text == 'QIWI':
            try:
                bot.send_message(message.from_user.id, '*ВНИМАНИЕ!* Если у вас в профиле QIWI кошелек указан неверно - платеж не будет засчитан! *Проверьте профиль перед депозитом*', parse_mode='Markdown')
                msg = bot.send_message(message.from_user.id, 'Введите сумму депозита:', reply_markup=profile_back)
                bot.register_next_step_handler(msg, dep_create)
            except Exception as ex:
                print(ex)
        elif message.text == 'Payeer':
            try:
                msg = bot.send_message(message.from_user.id,    '💶Минимальная сумма для депозита 10 RUB \n'+
                                                                '💵Введите сумму депозита:', reply_markup=profile_back)
                bot.register_next_step_handler(msg, dep_payeer_crt)
            except Exception as ex:
                print(ex)
        elif message.text == '💴Вывод':
            try:
                bot.send_message(message.from_user.id, 'Выберите платежную систему для вывода: ', reply_markup=qiwi_or_payeer_with)
            except Exception as ex:
                print(ex)
        elif message.text == 'Qiwi':
            try:
                a = db.check_qiwi_num(message.from_user.id)
                if a != 'not qiwi':
                    bot.send_message(message.from_user.id, '💵*Доступная сумма*: '+ db.check_balance(message.from_user.id) +' RUB', parse_mode='Markdown')
                    msg = bot.send_message(message.from_user.id, '💶Минимальная сумма для вывода 10 RUB. Введите, сколько хотите вывести', reply_markup=profile_back)
                    bot.register_next_step_handler(msg, with_oper)
                elif a == 'not qiwi':
                    bot.send_message(message.from_user.id, 'У вас не привязан QIWI кошелек! Привяжите его в профиле', reply_markup=menu)
            except Exception as ex:
                print(ex)
                
        elif message.text == 'Pаyeer':
            try:
                a = db.check_payeer_num(message.from_user.id)
                if a == 'not payeer':
                    bot.send_message(message.from_user.id, 'У вас не привязан Payeer. Привяжите его в профиле!', reply_markup=menu)
                elif a != 'not payeer':
                    bot.send_message(message.from_user.id, '💵*Доступная сумма*: '+ db.check_balance(message.from_user.id) +' RUB', parse_mode='Markdown')
                    msg = bot.send_message(message.from_user.id, '💶Минимальная сумма для вывода составляет 10 RUB. Введите, сколько хотите вывести', reply_markup=profile_back)
                    bot.register_next_step_handler(msg, with_payeer_oper)
            except Exception as ex:
                print(ex)
        elif message.text == '📑Статистика бота':
            try:
                a = int(db.checks_sum())+int(db.promos_sum())
                bot.send_message(message.from_user.id, 'Статистика бота: \n'+
                                                       '⚙️Мы работаем: '+str(db.day_work()) + ' дней \n'+
                                                       ' \n'+
                                                       '👨‍💼Пользователей: '+ str(db.check_users()) +' \n'+
                                                       ' \n'+
                                                       '👫Новых пользователей за сутки: '+ str(db.users_hours()) + '\n'+
                                                       ' \n'+
                                                       '💴Пользователи получили чеки на сумму: '+ db.checks_sum() +' RUB \n'+
                                                       ' \n'+
                                                       '📜Пользователи получили промокоды на сумму: '+ db.promos_sum() + ' RUB \n'+
                                                       ' \n'+
                                                       '💵Общая сумма заработанных денег: '+str(a)+' RUB \n'
                                                    , reply_markup=buy_ad, parse_mode='Markdown')
            except Exception as ex:
                print(ex)
        elif message.text == '🔙Вернуться':
            try:
                
                a = db.check_qiwi_num(message.from_user.id)
                if a != 'not qiwi':
                    bot.send_message(message.from_user.id, '<b>💵Ваш баланс</b>: '+ db.check_balance(message.from_user.id) + ' RUB \n' +
                                                        '<b>💸Доступно для вывода</b>: '+ db.check_balance(message.from_user.id) + ' RUB \n'+
                                                        '<b>🎫Билетов</b>: '+ db.check_ticket(message.from_user.id) + ' \n'+
                                                        # '<b>На выводе</b>: '+ db.check_on_withdraw(message.from_user.id) +' RUB \n' +
                                                        # '<b>Заработано</b>: '+ db.check_earn(message.from_user.id) +' RUB \n '+
                                                        '<b>QIWI кошелек</b>: '+ db.check_qiwi_num(message.from_user.id) + ' \n'+
                                                        '<b>Payeer номер счета</b>:'+ db.check_payeer_num(message.from_user.id), reply_markup=profile_menu, parse_mode='html')
                    bot.send_message(message.from_user.id, 'Если вы хотите изменить свой QIWI кошелек - нажмите на кнопку ниже: ', reply_markup=qiwi_set)
                elif a == 'not qiwi':
                    bot.send_message(message.from_user.id, '<b>💵Ваш баланс</b>: '+ db.check_balance(message.from_user.id) + ' RUB \n' +
                                                        '<b>💸Доступно для вывода</b>: '+ db.check_balance(message.from_user.id) + ' RUB \n'+
                                                        '<b>🎫Билетов</b>: '+ db.check_ticket(message.from_user.id) + ' \n'+
                                                        # '<b>На выводе</b>: '+ db.check_on_withdraw(message.from_user.id) +' RUB \n' +
                                                        # '<b>Заработано</b>: '+ db.check_earn(message.from_user.id) +' RUB \n '+
                                                        '<b>QIWI кошелек</b>: '+ db.check_qiwi_num(message.from_user.id) + ' \n'+
                                                        '<b>Payeer номер счета</b>:'+ db.check_payeer_num(message.from_user.id), reply_markup=profile_menu, parse_mode='html')
                    bot.send_message(message.from_user.id, 'Привяжите QIWI кошелек по кнопке ниже:', reply_markup=qiwi_set)
            except Exception as ex:
                print(ex)
        elif message.text == '📋В меню':
            try:
                bot.send_message(message.from_user.id, 'Вы в меню', reply_markup=menu)
            except Exception as ex:
                print(ex)
        
        if message.text == '🎫Билеты':
            try:

                bot.send_message(message.from_user.id, '🎫*Как получить билеты?*🎫 \n'+
                                                    '*1.* 👨‍💼За *каждого* приведенного пользователя, вы получаете *один* билет \n'+
                                                    '*2.* 💵Пополнить баланс \n'+
                                                    '*3.* 🕹Играя в игры \n'+
                                                    ' \n'+
                                                    '*При пополнении баланса*, в зависимости от суммы пополнения вы получите: \n'+
                                                    '• '+ str(db.ticket_sum_check('1')) +' → '+ str(db.ticket_set_check('1')) +' \n'+
                                                    '• '+ str(db.ticket_sum_check('2')) +' → '+ str(db.ticket_set_check('2')) +' \n'+
                                                    '• '+ str(db.ticket_sum_check('3')) +' → '+ str(db.ticket_set_check('3')) +' \n'+
                                                    '• '+ str(db.ticket_sum_check('4')) +' → '+ str(db.ticket_set_check('4')) +' \n'+
                                                    '• '+ str(db.ticket_sum_check('5')) +' → '+ str(db.ticket_set_check('5')) +' \n'+
                                                    '• '+ str(db.ticket_sum_check('6')) +' → '+ str(db.ticket_set_check('6')) +' \n'+
                                                    '• '+ str(db.ticket_sum_check('7')) +' → '+ str(db.ticket_set_check('7')) +' \n'+
                                                    ' \n'+
                                                    '🎫*Для чего нужны билеты?*🎫 \n '+
                                                    'Каждые 10 дней, те пользователи, кто заработал больше билетов - получают 💸денежное💸 вознаграждение!', reply_markup=profile_back, parse_mode='Markdown')


            except Exception as ex:
                print(ex)

        # Все, свзянное с созданием чека

        
        elif message.text == '💸Создать чек':
            try:
                bot.send_message(message.from_user.id,'👨‍💼Каждый пользователь, кто перейдет по этой ссылке станет вашим рефералом и вы получите за него 0.5 RUB на счёт для вывода. \n'+
                                                    '*ВАЖНО*: с одного чека может быть неограниченное количество рефералов \n'+
                                                    '💈Чек поможет в развитии вашего канала, либо другого ресурса', parse_mode='Markdown')
                bot.send_message(message.from_user.id, '💵*Баланс*: '+ db.check_balance(message.from_user.id) +' RUB \n'+
                                                    '💴*Минимальная сумма для создания чека*: ' + db.check_min_check() + ' RUB \n'+
                                                    '💶*Максимальная сумма для создания чека*: ' + db.check_max_check() + ' RUB', parse_mode='Markdown')
                msg = bot.send_message(message.from_user.id,'Введите сумму чека', reply_markup=menu_back)
                bot.register_next_step_handler(msg, check_message)
            except Exception as ex:
                print(ex)
        
        # Все, связанное с угадыванием курса

        elif message.text == '📈Угадай курс':
            try:
                msg = bot.send_message(message.from_user.id, '📈Здесь вы сможете выиграть деньги, если ваш прогноз на курс биткоина окажется ближе всех! \n'+
                                                             ' \n'+
                                                             '📌За 3 часа до конца розыгрыша, запрещено вводить данные. Каждый может без вложений и знаний заработать реальные деньги. \n'+
                                                             ' \n'+
                                                             'Курс BTC/USD бот берет с blockchain.com \n'+
                                                             '\n'+
                                                             'За первое место вы можете получить: '+str(db.check_btc('1'))+ ' RUB \n'+
                                                             'За второе место вы можете получить: '+str(db.check_btc('2'))+ ' RUB \n'+
                                                             'За третье место вы можете получить: '+str(db.check_btc('3'))+ ' RUB \n'+
                                                             '💲 Введите, сколько будет стоить биткоин (в долларах) '+str(db.check_date_btc('1'))+'.' +str(db.check_date_btc('2'))+ ' в 18:00', parse_mode='Markdown', reply_markup=menu_back)
                bot.register_next_step_handler(msg, btc)

            except Exception as ex:
                print(ex)
        
        


        # Все, связанное с промокодом

        elif message.text == '📜Промокод':
            try:
                bot.send_message(message.from_user.id,  '👨‍💼Каждый пользователь, который введет ваш промокод, станет вашим рефералом, даже если он уже не действителен и вы получите за него 0.5 RUB на счёт для вывода. \n'+
                                                       'ВАЖНО: с одного промокода может быть неограниченное количество рефералов \n'+
                                                       '📢 Например у вас есть ютуб канал, вы можете создать промокод и спрятать его на протяжении всего видео. Тем самым, пользователи будут смотреть ваше видео и искать промокод. \n'+
                                                       ' \n'
                                                        'Выберите, что вам нужно: создать или ввести промокод', reply_markup=promo_menu)
            except Exception as ex:
                print(ex)
        elif message.text == '📝Создать промокод':
            try:
                bot.send_message(message.from_user.id, 'Сгенерировать - получится промо код из 6 символов, автоматически (например f5j7fn) \n'+
                                                       ' \n'
                                                       'Создать - вы можете создать слово или фразу и добавить ее на видео, либо личный сайт',reply_markup=promo_type, parse_mode='Markdown')
            except Exception as ex:
                print(ex)
        elif message.text == '✏️Ввести промокод':
            try:
                msg = bot.send_message(message.from_user.id, 'Введите промокод:', reply_markup=promo_menu)
                bot.register_next_step_handler(msg, ins_promo)
            except Exception as ex:
                print(ex)



        # Все свзянанное с играми
        elif message.text == '🕹Игры':
            try:

                bot.send_message(message.from_user.id, 'Выберите игру, в которую вы хотите сыграть', reply_markup=games_markup)

            except Exception as ex:
                print(ex)

        elif message.text == '🚪Комнаты':
            try:
                bot.send_message(message.from_user.id, '👨‍💼В этом разделе моно играть в 4-ех комнатах с реальными людьми! \n'+
                                                    'В каждой комнате по 5 игроков. Как только комната заполняется, бот выбирает победителя!🤑'+
                                                    ' \n'+
                                                    '*Внимание* Если вы войдете в комнату, то сможете выйти только через 3 часа!', parse_mode='Markdown', reply_markup=rooms())
            except Exception as ex:
                print(ex)
        
        elif message.text == '🎲Дайс':
            try:

                bot.send_message(message.from_user.id, '🎲*Дайс - здесь вы можете испытать свою удачу!* \n'+
                                                       ' \n'+
                                                       'После того, как вы введете сумму ставки и нажмете на кнопку - бот *начислит* или спишет с вашего баланса указанное количество RUB с вероятностью 50% \n'+
                                                       '📢 например, ваша ставка 100р и с вероятностью 50% вы получите 200р, либо с вероятностью 50% выиграет бот. \n'+
                                                       ' \n'+
                                                       '🏷За каждую игру от 10р, вы получите дополнительно 1 билет.', parse_mode='Markdown')
                msg = bot.send_message(message.from_user.id, 'Введите ставку от 1 до 200 RUB: ', reply_markup=menu_back)
                bot.register_next_step_handler(msg, dice)
            
            except Exception as ex:
                print(ex)

        
        # Работа с админкой

        elif message.text == 'Вернуться в админку':
            if message.from_user.id in admin:
                bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
            else:
                bot.send_message(message.from_user.id, 'Вы не администратор!')
        elif message.text == 'Изменение чека':
            if message.from_user.id in admin:
                bot.send_message(message.from_user.id, 'Выберите, что вам нужно изменить: ', reply_markup=check_set)
            else:
                bot.send_message(message.from_user.id, 'Вы не администратор!')
        elif message.text == 'Минимальную сумму':
            if message.from_user.id in admin:
                msg = bot.send_message(message.from_user.id, 'Хорошо, введите минимальную сумму, для создания чека: ')
                bot.register_next_step_handler(msg, set_min_check)
            else:
                bot.send_message(message.from_user.id, 'Вы не администратор!')
        elif message.text == 'Максимальную сумму':
            if message.from_user.id in admin:
                msg = bot.send_message(message.from_user.id, 'Хорошо, введите максимальную сумму, для создания чека: ')
                bot.register_next_step_handler(msg, set_max_check)
            else:
                bot.send_message(message.from_user.id, 'Вы не администратор!')
        elif message.text == 'Награда за чек':
            if message.from_user.id in admin:
                msg = bot.send_message(message.from_user.id, 'Хорошо, введите награду за активацию чека: ')
                bot.register_next_step_handler(msg, set_rew_check)
            else:
                bot.send_message(message.from_user.id, 'Вы не администратор!')
        elif message.text == 'Изменение промокода':
            if message.from_user.id in admin:
                bot.send_message(message.from_user.id, 'Выберите, что вам нужно изменить: ', reply_markup=promo_set)
            else:
                bot.send_message(message.from_user.id, 'Вы не администратор!')
        elif message.text == 'Минимальную сумму промокода':
            if message.from_user.id in admin:
                msg = bot.send_message(message.from_user.id, 'Хорошо, введите минимальную сумму, для создания промокода: ')
                bot.register_next_step_handler(msg, set_min_promo)
            else:
                bot.send_message(message.from_user.id, 'Вы не администратор!')
        elif message.text == 'Максимальную сумму промокода':
            if message.from_user.id in admin:
                msg = bot.send_message(message.from_user.id, 'Хорошо, введите максимальную сумму, для создания промокода: ')
                bot.register_next_step_handler(msg, set_max_promo)
            else:
                bot.send_message(message.from_user.id, 'Вы не администратор!')
        elif message.text == 'Награда за промокод':
            if message.from_user.id in admin:
                msg = bot.send_message(message.from_user.id, 'Хорошо, введите награду за активацию промокода: ')
                bot.register_next_step_handler(msg, set_rew_promo)
            else:
                bot.send_message(message.from_user.id, 'Вы не администратор!')
        elif message.text == 'Выигрыш за курс биткоина':
            if message.from_user.id in admin:
                bot.send_message(message.from_user.id, 'Хорошо, на данный момент: \n'+
                                                             'За первое место: '+str(db.check_btc('1'))+ ' RUB \n'+
                                                             'За второе место: '+str(db.check_btc('2'))+ ' RUB \n'+
                                                             'За третье место: '+str(db.check_btc('3'))+ ' RUB \n', reply_markup=return_adm_markup)
                msg = bot.send_message(message.from_user.id, 'Введите место, за которое хотите изменить выигрыш (Пример: "1"): ')
                bot.register_next_step_handler(msg, set_rew_btc)
            else:
                bot.send_message(message.from_user.id, 'Вы не администратор!')
        elif message.text == 'Время валидности промокода':
            if message.from_user.id in admin:
                msg = bot.send_message(message.from_user.id, 'Хорошо, напишите сколько часов будет действителен промокод (1 - один час, 4 - четыре часа и т.д.): ')
                bot.register_next_step_handler(msg, set_time_promo)
            else:
                bot.send_message(message.from_user.id, 'Вы не администратор!')
        elif message.text == 'Изменение билетов':
            if message.from_user.id in admin:
                bot.send_message(message.from_user.id, 'Выберите, что вы хотите изменить в системе билетов', reply_markup=tickets_markup)
            else:
                bot.send_message(message.from_user.id, 'Вы не администратор!')
        elif message.text == 'Призовые места':
            if message.from_user.id in admin:

                msg = bot.send_message(message.from_user.id, 'На данный момент ' + str(db.check_top_ticket()) + ' призовых мест. Введите, сколько установить призовых мест: ')
                bot.register_next_step_handler(msg, change_top_ticket)

            else:
                bot.send_message(message.from_user.id, 'Вы не администратор!')
        elif message.text == 'Выигрыш за билеты':
            if message.from_user.id in admin:

                bot.send_message(message.from_user.id, 'На данный момент: \n'+
                                                    '*За 1 место*: '+str(db.check_win_ticket('1'))+' RUB \n'+
                                                    '*За 2 место*: '+str(db.check_win_ticket('2'))+' RUB \n'+
                                                    '*За 3 место*: '+str(db.check_win_ticket('3'))+' RUB \n'+
                                                    '*За 4 место*: '+str(db.check_win_ticket('4'))+' RUB \n'+
                                                    '*За 5 место*: '+str(db.check_win_ticket('5'))+' RUB \n', parse_mode='Markdown')
                msg = bot.send_message(message.from_user.id, 'Введите номер места, которого хотите изменить выигрыш:')
                bot.register_next_step_handler(msg, change_win_ticket)

            else:
                bot.send_message(message.from_user.id, 'Вы не администратор!')
        elif message.text == 'Билеты за депозит':
            if message.from_user.id in admin:

                bot.send_message(message.from_user.id, 'На данный момент: \n'+
                                                    '*1.* '+ str(db.ticket_sum_check('1')) +' → '+ str(db.ticket_set_check('1')) +' \n'+
                                                    '*2.* '+ str(db.ticket_sum_check('2')) +' → '+ str(db.ticket_set_check('2')) +' \n'+
                                                    '*3.* '+ str(db.ticket_sum_check('3')) +' → '+ str(db.ticket_set_check('3')) +' \n'+
                                                    '*4.* '+ str(db.ticket_sum_check('4')) +' → '+ str(db.ticket_set_check('4')) +' \n'+
                                                    '*5.* '+ str(db.ticket_sum_check('5')) +' → '+ str(db.ticket_set_check('5')) +' \n'+
                                                    '*6.* '+ str(db.ticket_sum_check('6')) +' → '+ str(db.ticket_set_check('6')) +' \n'+
                                                    '*7.* '+ str(db.ticket_sum_check('7')) +' → '+ str(db.ticket_set_check('7')) +' \n', parse_mode='Markdown')
                msg = bot.send_message(message.from_user.id, 'Введите номер, чьи настройки зотите изменить: ')
                bot.register_next_step_handler(msg, change_dep_ticket)

            else:
                bot.send_message(message.from_user.id, 'Вы не администратор!')
        elif message.text == 'Билеты за игры':
            if message.from_user.id in admin:

                bot.send_message(message.from_user.id, 'На данный момент: \n'+
                                                    'За комнату № 1 пользователь получит: '+str(db.check_set_room_tick('1'))+' билетов \n'+
                                                    'За комнату № 2 пользователь получит: '+str(db.check_set_room_tick('2'))+' билетов \n'+
                                                    'За комнату № 3 пользователь получит: '+str(db.check_set_room_tick('3'))+' билетов \n'+
                                                    'За комнату № 4 пользователь получит: '+str(db.check_set_room_tick('4'))+' билетов \n'+
                                                    'За комнату № 5 пользователь получит: '+str(db.check_set_room_tick('5'))+' билетов \n'+
                                                    'За комнату № 6 пользователь получит: '+str(db.check_set_room_tick('6'))+' билетов \n')
                msg = bot.send_message(message.from_user.id, 'Напишите номер комнаты, где хотите изменить количество билетов за выигрыш: ')
                bot.register_next_step_handler(msg, room_ticket)

            else:
                bot.send_message(message.from_user.id, 'Вы не администратор!')
        elif message.text == 'Забанить пользователя':
            if message.from_user.id in admin:

                msg = bot.send_message(message.from_user.id, 'Введите username пользователя, которого нужно забанить. *БЕЗ* @', parse_mode='Markdown')
                bot.register_next_step_handler(msg, ban_user)

            else:
                bot.send_message(message.from_user.id, 'Вы не администратор!')
        elif message.text == 'Разбанить пользователя':
            if message.from_user.id in admin:

                msg = bot.send_message(message.from_user.id, 'Введите username пользователя, которого нужно разбанить. *БЕЗ* @', parse_mode='Markdown')
                bot.register_next_step_handler(msg, unban_user)

            else:
                bot.send_message(message.from_user.id, 'Вы не администратор!')
        elif message.text == 'Каналы для подписки':
            if message.from_user.id in admin:

                bot.send_message(message.from_user.id, 'На данный момент: ' )
                for i in db.check_channels():
                    b = 1
                    bot.send_message(message.from_user.id, str(b)+'. '+str(i[0]))
                bot.send_message(message.from_user.id, 'Это все каналы', reply_markup=channels_markup)

            else:
                bot.send_message(message.from_user.id, 'Вы не администратор!')

        elif message.text == 'Удалить канал':
            if message.from_user.id in admin:

                msg = bot.send_message(message.from_user.id, 'Введите канал, который нужно удалить (Пример: "@channelname")')
                bot.register_next_step_handler(msg, channel_del)

            else:
                bot.send_message(message.from_user.id, 'Вы не администратор!')
        elif message.text == 'Добавить канал':
            if message.from_user.id in admin:

                msg = bot.send_message(message.from_user.id, 'Введите канал, который нужно добавить (Пример: "@channelname")')
                bot.register_next_step_handler(msg, channel_add)

            else:
                bot.send_message(message.from_user.id, 'Вы не администратор!')
        elif message.text == 'Изменить баланс пользователю':
            if message.from_user.id in admin:
                
                msg = bot.send_message(message.from_user.id, 'Введите id пользователя: ', return_adm_markup)
                bot.register_next_step_handler(msg, change_balance)
                
            else:
                bot.send_message(message.from_user.id, 'Вы не администратор!')
        elif message.text == 'Рассылка сообщения':
            if message.from_user.id in admin:

                msg = bot.send_message(message.from_user.id, 'Введите сообщение, которое хотите отправить всем пользователям бота: ', reply_markup=return_adm_markup)
                bot.register_next_step_handler(msg, send_msgs)

            else:
                bot.send_message(message.from_user.id, 'Вы не администратор!')
    elif db.check_subs(message.from_user.id) == 'no':
            bot.send_message(message.from_user.id, 'Вы не подписаны на каналы!', reply_markup=accept)
            for channel in check_member_list:
                bot.send_message(message.from_user.id,'t.me/'+channel.split('@')[1])




def send_msgs(message):
    a = db.add_msg(message.text)
    if message.text == 'Вернуться в админку':
        bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
    else:
        a = db.add_msg(message.text)
        bot.send_message(message.from_user.id, str(a), reply_markup=send_or_canc)


def dice(message):
    
    if message.text.isdigit():
        if (int(message.text) >= 1 or float(message.text) >= 1.0) and (int(message.text) <= 200 or float(message.text) <= 200.0):
            a = db.dice_step1(message.from_user.id, float(message.text))
            if a == 'ok':
                bot.send_message(message.from_user.id, '*Ваша ставка*: '+message.text+' RUB \n'+
                                                    'Нажмите на кнопку ниже, чтобы сыграть', parse_mode='Markdown', reply_markup=dice_inl_markup)
            elif a == 'notmoney':
                bot.send_message(message.from_user.id, 'У вас недостаточно денег. Вы были отправлены в меню', reply_markup=menu)
        else:
            bot.send_message(message.from_user.id, 'Произошла ошибка. Возможно вы ввели неверную сумму ставки. Вы были отправлены в меню', reply_markup=menu)
    

    elif message.text == '📋В меню':
        bot.send_message(message.from_user.id, 'Вы в меню📋', reply_markup=menu)
    else:
        bot.send_message(message.from_user.id, 'Произошла ошибка. Возможно вы ввели число с точкой либо буквы. Вы были отправлены в меню', reply_markup=menu)



def change_balance1(message):
    a = message.text.split(",")
    if len(a) == 2:
        if a[1].isdigit():
            db.change_balance(a[0], a[1])
            bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)
        else:
            bot.send_message(message.from_user.id, 'Вы ввели некорректную сумму и были отправлены в админ панель!', reply_markup=admin_markup)
    else:
        bot.send_message(message.from_user.id, 'Вы ввели что-то неправильно и были отправлены в админ панель!', reply_markup=admin_markup)

def change_balance(message):
    if message.text == 'Вернуться в админку':
        bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)

        
    
    else:
        a = db.check_userid(message.text)
        if a == 'usernot':
            bot.send_message(message.from_user.id, 'Такого пользователя нет в базе данных!', reply_markup=admin_markup)
        else:
            bot.send_message(message.from_user.id, 'Пользователь был найден! У него '+str(a)+' RUB на балансе!')
            msg = bot.send_message(message.from_user.id, 'Введите ещё раз его id и число на которое изменить ему баланс через запятую! (Пример: 123456789,5000)', reply_markup=return_adm_markup)
            bot.register_next_step_handler(msg, change_balance1)
        

def channel_add(message):
    if message.text == 'Вернуться в админку':
        bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
    else:
        db.add_channel(message.text)
        bot.send_message(message.from_user.id, 'Добавлено!', reply_markup=admin_markup)

def channel_del(message):
    if message.text == 'Вернуться в админку':
        bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
    else:
        db.del_channel(message.text)
        bot.send_message(message.from_user.id, 'Удалено!', reply_markup=admin_markup)



def unban_user(message):
    db.ban_or_unban('2', message.text)
    bot.send_message(message.from_user.id, 'Пользователь разбанен!', reply_markup=admin_markup)


def ban_user(message):
    db.ban_or_unban('1', message.text)
    bot.send_message(message.from_user.id, 'Пользователь забанен!', reply_markup=admin_markup)

def room_ticket1(message):
    try:
        if message.text.isdigit():
            db.ticket_room_change('1', int(message.text))
            bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)
        elif message.text == 'Вернуться в админку':
            bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
        else:
            bot.send_message(message.from_user.id, 'Произошла ошибка, вы были отправлены в админ панель', reply_markup=admin_markup)
    except Exception as ex:
        print(ex)

def room_ticket2(message):
    try:
        if message.text.isdigit():
            db.ticket_room_change('2', int(message.text))
            bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)
        elif message.text == 'Вернуться в админку':
            bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
        else:
            bot.send_message(message.from_user.id, 'Произошла ошибка, вы были отправлены в админ панель', reply_markup=admin_markup)
    except Exception as ex:
        print(ex)

def room_ticket3(message):
    try:
        if message.text.isdigit():
            db.ticket_room_change('3', int(message.text))
            bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)
        elif message.text == 'Вернуться в админку':
            bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
        else:
            bot.send_message(message.from_user.id, 'Произошла ошибка, вы были отправлены в админ панель', reply_markup=admin_markup)
    except Exception as ex:
        print(ex)

def room_ticket4(message):
    try:
        if message.text.isdigit():
            db.ticket_room_change('4', int(message.text))
            bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)
        elif message.text == 'Вернуться в админку':
            bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
        else:
            bot.send_message(message.from_user.id, 'Произошла ошибка, вы были отправлены в админ панель', reply_markup=admin_markup)
    except Exception as ex:
        print(ex)

def room_ticket5(message):
    try:
        if message.text.isdigit():
            db.ticket_room_change('5', int(message.text))
            bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)
        elif message.text == 'Вернуться в админку':
            bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
        else:
            bot.send_message(message.from_user.id, 'Произошла ошибка, вы были отправлены в админ панель', reply_markup=admin_markup)
    except Exception as ex:
        print(ex)

def room_ticket6(message):
    try:
        if message.text.isdigit():
            db.ticket_room_change('6', int(message.text))
            bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)
        elif message.text == 'Вернуться в админку':
            bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
        else:
            bot.send_message(message.from_user.id, 'Произошла ошибка, вы были отправлены в админ панель', reply_markup=admin_markup)
    except Exception as ex:
        print(ex)

def room_ticket(message):
    try:
        if message.text.isdigit():
            if int(message.text) <= 6 and int(message.text) > 0:
                if message.text == '1':
                    msg = bot.send_message(message.from_user.id, 'Введите количество билетов за 1 комнату: ')
                    bot.register_next_step_handler(msg, room_ticket1)
                elif message.text == '2':
                    msg = bot.send_message(message.from_user.id, 'Введите количество билетов за 1 комнату: ')
                    bot.register_next_step_handler(msg, room_ticket2)
                elif message.text == '3':
                    msg = bot.send_message(message.from_user.id, 'Введите количество билетов за 1 комнату: ')
                    bot.register_next_step_handler(msg, room_ticket3)
                elif message.text == '4':
                    msg = bot.send_message(message.from_user.id, 'Введите количество билетов за 1 комнату: ')
                    bot.register_next_step_handler(msg, room_ticket4)
                elif message.text == '5':
                    msg = bot.send_message(message.from_user.id, 'Введите количество билетов за 1 комнату: ')
                    bot.register_next_step_handler(msg, room_ticket5)
                elif message.text == '6':
                    msg = bot.send_message(message.from_user.id, 'Введите количество билетов за 1 комнату: ')
                    bot.register_next_step_handler(msg, room_ticket6)
                elif message.text == 'Вернуться в админку':
                    bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
            elif message.text == 'Вернуться в админку':
                bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
            else:
                bot.send_message(message.from_user.id, 'Вы ввели неверное число и были отправлены в админ панель', reply_markup=admin_markup)
        elif message.text == 'Вернуться в админку':
            bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
        else:
            bot.send_message(message.from_user.id, 'Вы были отправлены в админ панель', reply_markup=admin_markup)
    except Exception as ex:
        print(ex)


def dep_ticket1(message):
    a = message.text.split(",")
    if len(a) == 2:
        db.change_dep_tickets(a[0],a[1],'1')
        bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)
    elif message.text == 'Вернуться в админку':
        bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
    else:
        bot.send_message(message.from_user.id, 'Вы были отправлены в админ панель', reply_markup=admin_markup)

def dep_ticket2(message):
    a = message.text.split(",")
    if len(a) == 2:
        db.change_dep_tickets(a[0],a[1],'2')
        bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)
    elif message.text == 'Вернуться в админку':
        bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
    else:
        bot.send_message(message.from_user.id, 'Вы были отправлены в админ панель', reply_markup=admin_markup)

def dep_ticket3(message):
    a = message.text.split(",")
    if len(a) == 2:
        db.change_dep_tickets(a[0],a[1],'3')
        bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)
    elif message.text == 'Вернуться в админку':
        bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
    else:
        bot.send_message(message.from_user.id, 'Вы были отправлены в админ панель', reply_markup=admin_markup)

def dep_ticket4(message):
    a = message.text.split(",")
    if len(a) == 2:
        db.change_dep_tickets(a[0],a[1],'4')
        bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)
    elif message.text == 'Вернуться в админку':
        bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
    else:
        bot.send_message(message.from_user.id, 'Вы были отправлены в админ панель', reply_markup=admin_markup)

def dep_ticket5(message):
    a = message.text.split(",")
    if len(a) == 2:
        db.change_dep_tickets(a[0],a[1],'5')
        bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)
    elif message.text == 'Вернуться в админку':
        bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
    else:
        bot.send_message(message.from_user.id, 'Вы были отправлены в админ панель', reply_markup=admin_markup)

def dep_ticket6(message):
    a = message.text.split(",")
    if len(a) == 2:
        db.change_dep_tickets(a[0],a[1],'6')
        bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)
    elif message.text == 'Вернуться в админку':
        bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
    else:
        bot.send_message(message.from_user.id, 'Вы были отправлены в админ панель', reply_markup=admin_markup)

def dep_ticket7(message):
    a = message.text.split(",")
    if len(a) == 2:
        db.change_dep_tickets(a[0],a[1],'7')
        bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)
    elif message.text == 'Вернуться в админку':
        bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
    else:
        bot.send_message(message.from_user.id, 'Вы были отправлены в админ панель', reply_markup=admin_markup)

def change_dep_ticket(message):
    if message.text.isdigit():
        if message.text == '1':
            msg = bot.send_message(message.from_user.id, 'Введите через запятую, сколько билетов за сколько депозита получит пользователь в формате ("БИЛЕТЫ,СУММА"). Пример (1,100):')
            bot.register_next_step_handler(msg, dep_ticket1)
        elif message.text == '2':
            msg = bot.send_message(message.from_user.id, 'Введите через запятую, сколько билетов за сколько депозита получит пользователь в формате ("БИЛЕТЫ,СУММА"). Пример (1,100):')
            bot.register_next_step_handler(msg, dep_ticket2)
        elif message.text == '3':
            msg = bot.send_message(message.from_user.id, 'Введите через запятую, сколько билетов за сколько депозита получит пользователь в формате ("БИЛЕТЫ,СУММА"). Пример (1,100):')
            bot.register_next_step_handler(msg, dep_ticket3)
        elif message.text == '4':
            msg = bot.send_message(message.from_user.id, 'Введите через запятую, сколько билетов за сколько депозита получит пользователь в формате ("БИЛЕТЫ,СУММА"). Пример (1,100):')
            bot.register_next_step_handler(msg, dep_ticket4)
        elif message.text == '5':
            msg = bot.send_message(message.from_user.id, 'Введите через запятую, сколько билетов за сколько депозита получит пользователь в формате ("БИЛЕТЫ,СУММА"). Пример (1,100):')
            bot.register_next_step_handler(msg, dep_ticket5)
        elif message.text == '6':
            msg = bot.send_message(message.from_user.id, 'Введите через запятую, сколько билетов за сколько депозита получит пользователь в формате ("БИЛЕТЫ,СУММА"). Пример (1,100):')
            bot.register_next_step_handler(msg, dep_ticket6)
        elif message.text == '7':
            msg = bot.send_message(message.from_user.id, 'Введите через запятую, сколько билетов за сколько депозита получит пользователь в формате ("БИЛЕТЫ,СУММА"). Пример (1,100):')
            bot.register_next_step_handler(msg, dep_ticket7)
        elif message.text == 'Вернуться в админку':
            bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
    elif message.text == 'Вернуться в админку':
        bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
    else:
        bot.send_message(message.from_user.id, 'Вы были отправлены в админ панель', reply_markup=admin_markup)


def win1(message):
    db.change_win_tickets('1', int(message.text))
    bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)

def win2(message):
    db.change_win_tickets('2', int(message.text))
    bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)

def win3(message):
    db.change_win_tickets('3', int(message.text))
    bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)

def win4(message):
    db.change_win_tickets('4', int(message.text))
    bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)

def win5(message):
    db.change_win_tickets('5', int(message.text))
    bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)

def change_win_ticket(message):
    if message.text.isdigit():
        if message.text == '1':
            msg = bot.send_message(message.from_user.id, 'Введите сумму:')
            bot.register_next_step_handler(msg, win1)
        elif message.text == '2':
            msg = bot.send_message(message.from_user.id, 'Введите сумму:')
            bot.register_next_step_handler(msg, win2)
        elif message.text == '3':
            msg = bot.send_message(message.from_user.id, 'Введите сумму:')
            bot.register_next_step_handler(msg, win3)
        elif message.text == '4':
            msg = bot.send_message(message.from_user.id, 'Введите сумму:')
            bot.register_next_step_handler(msg, win4)
        elif message.text == '5':
            msg = bot.send_message(message.from_user.id, 'Введите сумму:')
            bot.register_next_step_handler(msg, win5)
        elif message.text == 'Вернуться в админку':
            bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
        else:
            bot.send_message(message.from_user.id, 'Вы ввели что-то не так и были отправлены в меню', reply_markup=admin_markup)
    elif message.text == 'Вернуться в админку':
        bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
    else:
        bot.send_message(message.from_user.id, 'Вы ввели что-то не так и были отправлены в меню', reply_markup=admin_markup)

def change_top_ticket(message):
    if message.text.isdigit():
        if int(message.text) <= 5 and int(message.text) > 0:
            bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)
        elif message.text == 'Вернуться в админку':
            bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
        else:
            bot.send_message(message.from_user.id, 'Вы ввели неверное число и были отправлены в админ панель', reply_markup=admin_markup)
    elif message.text == 'Вернуться в админку':
        bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
    else:
        bot.send_message(message.from_user.id, 'Произошла ошибка. Вы ввели не число и были отправлены админ панель', reply_markup=admin_markup)



def with_payeer_oper(message):
    if message.text.isdigit():
        if int(message.text) >= 10:
            balance = db.check_balance(message.from_user.id)
            if message.text <= balance:
                db.balance_with(message.from_user.id, message.text)
                bot.send_message(message.from_user.id, '💸Заявка на вывод создана! Ожидайте зачисление средств в течении 72 часов!💸')
                a = db.check_payeer_num(message.from_user.id)
                for i in admin:
                    bot.send_message(i, 'Создана заявка на вывод средств! \n'+
                                        '*Id пользователя*: '+str(message.from_user.id)+' \n'+
                                        '*Сумма*: '+message.text + ' RUB \n'+
                                        '*Номер счета Payeer*: '+a+ '\n', reply_markup=withdraw_keyboard_payeer, parse_mode='Markdown')
            else:
                bot.send_message(message.from_user.id, 'Произошла ошибка. Возможно вы ввели больше, чем у вас на балансе.', reply_markup=menu)
        else:
            bot.send_message(message.from_user.id, 'Вы ввели меньше 10 RUB и были отправлены в меню', reply_markup=menu)
    else:
        bot.send_message(message.from_user.id, 'Вы ввели не число и были отправлены в меню', reply_markup=menu)




def with_oper(message):
    if message.text.isdigit():
        if int(message.text) >= 10:
            balance = db.check_balance(message.from_user.id)
            if message.text <= balance:
                qiwi_num = db.check_qiwi_num(message.from_user.id)
                bot.send_message(message.from_user.id, '💸Заявка на вывод создана!💸', reply_markup=menu)
                a = db.with_operaion(message.from_user.id, message.text, qiwi_num)
                for i in admin:
                    bot.send_message(i, 'Новая заявка на вывод! \n'+
                                        'Заявка №'+str(a)+' \n'+
                                        '*Пользователь* - @'+ message.from_user.username +' \n'+
                                        '*Сумма* - ' + message.text + ' RUB \n' +
                                        '*Дата* - ' + str(db.time_now()) + ' \n'+
                                        '*Кошелек* - +'+ qiwi_num, reply_markup=withdraw_keyboard, parse_mode='Markdown')
            elif message.text > balance:
                bot.send_message(message.from_user.id, 'Вы не можете вывести больше, чем вам баланс!', reply_markup=menu)
        elif int(message.text) < 10:
            bot.send_message(message.from_user.id, 'Минимальная сумма - 10 RUB. Вы были возвращены в мею', reply_markup=menu)


def payeer_sets(message):
    if message.text == '🔙Вернуться':
        bot.send_message(message.from_user.id, '<b>💵Ваш баланс</b>: '+ db.check_balance(message.from_user.id) + ' RUB \n' +
                                                '<b>💸Доступно для вывода</b>: '+ db.check_balance(message.from_user.id) + ' RUB \n'+
                                                '<b>🎫Билетов</b>: '+ db.check_ticket(message.from_user.id) + ' \n'+
                                                # '<b>На выводе</b>: '+ db.check_on_withdraw(message.from_user.id) +' RUB \n' +
                                                # '<b>Заработано</b>: '+ db.check_earn(message.from_user.id) +' RUB \n '+
                                                '<b>QIWI кошелек</b>: '+ db.check_qiwi_num(message.from_user.id) + ' \n'+
                                                '<b>Payeer номер счета</b>:'+ db.check_payeer_num(message.from_user.id), reply_markup=profile_menu, parse_mode='html')
    else:
        bot.send_message(message.from_user.id, 'Вы успешно привязали номер счета Payeer!')
        db.payeer_set(message.from_user.id, message.text)


def dep_create(message):
    if message.text.isdigit():
        if int(message.text) >= 10:
            a = db.check_qiwi_num(message.from_user.id)
            print(a)
            if a != 'not qiwi':
                db.dep_operation(message.from_user.id, message.text)
                bot.send_message(message.from_user.id, 'Ссылка для оплаты:')
                bot.send_message(message.from_user.id, api.get_pay_url(int(message.text), message.from_user.id, '79602844595'))
            elif a == 'not qiwi':
                bot.send_message(message.from_user.id, 'У вас не привязан QIWI кошелек. Привяжите его в профиле', reply_markup=menu)
        elif int(message.text) < 10:
            bot.send_message(message.from_user.id, 'Вы ввели сумму неверно и были отправлены в меню', reply_markup=menu)
    elif message.text == '🔙Вернуться':
        a = db.check_qiwi_num(message.from_user.id)
        if a != 'not qiwi':
            bot.send_message(message.from_user.id, '<b>💵Ваш баланс</b>: '+ db.check_balance(message.from_user.id) + ' RUB \n' +
                                                    '<b>💸Доступно для вывода</b>: '+ db.check_balance(message.from_user.id) + ' RUB \n'+
                                                    '<b>🎫Билетов</b>: '+ db.check_ticket(message.from_user.id) + ' \n'+
                                                    # '<b>На выводе</b>: '+ db.check_on_withdraw(message.from_user.id) +' RUB \n' +
                                                    # '<b>Заработано</b>: '+ db.check_earn(message.from_user.id) +' RUB \n '+
                                                    '<b>QIWI кошелек</b>: '+ db.check_qiwi_num(message.from_user.id) + ' \n'+
                                                    '<b>Payeer номер счета</b>:'+ db.check_payeer_num(message.from_user.id), reply_markup=profile_menu, parse_mode='html')
            bot.send_message(message.from_user.id, 'Если вы хотите изменить свой QIWI кошелек - нажмите на кнопку ниже: ', reply_markup=qiwi_set)
        elif a == 'not qiwi':
            bot.send_message(message.from_user.id, '<b>💵Ваш баланс</b>: '+ db.check_balance(message.from_user.id) + ' RUB \n' +
                                                    '<b>💸Доступно для вывода</b>: '+ db.check_balance(message.from_user.id) + ' RUB \n'+
                                                    '<b>🎫Билетов</b>: '+ db.check_ticket(message.from_user.id) + ' \n'+
                                                    # '<b>На выводе</b>: '+ db.check_on_withdraw(message.from_user.id) +' RUB \n' +
                                                    # '<b>Заработано</b>: '+ db.check_earn(message.from_user.id) +' RUB \n '+
                                                    '<b>QIWI кошелек</b>: '+ db.check_qiwi_num(message.from_user.id) + ' \n'+
                                                    '<b>Payeer номер счета</b>:'+ db.check_payeer_num(message.from_user.id), reply_markup=profile_menu, parse_mode='html')
            bot.send_message(message.from_user.id, 'Привяжите QIWI кошелек по кнопке ниже:', reply_markup=qiwi_set)
    else:
        bot.send_message(message.from_user.id, 'Вы должны ввести число', reply_markup=menu)


def dep_payeer_crt(message):
    if message.text.isdigit():
        if int(message.text) >= 10:
            bot.send_message(message.from_user.id, '*Переведите*: ' + message.text + ' RUB💵 \n'+
                                                   '*На номер счета*: ' + payeer + ' \n'+
                                                   '*С комментарием*: ' + str(message.from_user.id) + ' \n'+
                                                   '💸Ожидайте зачисление баланса в течении 24 часов💸', reply_markup=menu, parse_mode='Markdown')
            for i in admin:
                bot.send_message(i, 'Возможно, скоро поступит новый платеж на Payeer! Не забудьте начислить баланс пользователю, id которого, указан в комментарии о платеже!')
        else:
            bot.send_message(message.from_user.id, 'Вы ввели неверную сумму и были отправлены в меню', reply_markup=menu)
    else:
        bot.send_message(message.from_user.id, 'Вы должны ввести число. Вы были отправлены в меню', reply_markup=menu)

def set_time_promo(message):
    if message.text.isdigit():
        db.set_time_promos(message.text)
        bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)
    elif message.text == 'Вернуться в админку':
        bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
    else:
        bot.send_message(message.from_user.id, 'Вы должны ввести число!', reply_markup=admin_markup)


def set_rew_btc1(message):
    if message.text == 'Вернуться в админку':
        bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
    else:
        db.set_rew_btcs('1', message.text)
        bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)

def set_rew_btc2(message):
    if message.text == 'Вернуться в админку':
        bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
    else:
        db.set_rew_btcs('2', message.text)
        bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)

def set_rew_btc3(message):
    if message.text == 'Вернуться в админку':
        bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
    else:
        db.set_rew_btcs('3', message.text)
        bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)


def set_rew_btc(message):
    if message.text.isdigit():
        if message.text == '1':
            msg = bot.send_message(message.from_user.id, 'Введите сумму:')
            bot.register_next_step_handler(msg, set_rew_btc1)
        elif message.text == '2':
            msg = bot.send_message(message.from_user.id, 'Введите сумму:')
            bot.register_next_step_handler(msg, set_rew_btc2)
        elif message.text == '3':
            msg = bot.send_message(message.from_user.id, 'Введите сумму:')
            bot.register_next_step_handler(msg, set_rew_btc3)
        else:
            bot.send_message(message.from_user.id, 'Вы ввели что-то не так и были отправлены в админ панель', reply_markup=admin_markup)
        
            
    elif message.text == 'Вернуться в админку':
        bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
    else:
        bot.send_message(message.from_user.id, 'Вы должны ввести число!', reply_markup=admin_markup)

def set_rew_promo(message):
    if message.text.isdigit():
        db.set_rew_promos(message.text)
        bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)
    elif message.text == 'Вернуться в админку':
        bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
    else:
        bot.send_message(message.from_user.id, 'Вы должны ввести число!', reply_markup=admin_markup)

def set_max_promo(message):
    if message.text.isdigit():
        db.set_max_promos(message.text)
        bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)
    elif message.text == 'Вернуться в админку':
        bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
    else:
        bot.send_message(message.from_user.id, 'Вы должны ввести число!', reply_markup=admin_markup)



def set_min_promo(message):
    if message.text.isdigit():
        db.set_min_promos(message.text)
        bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)
    elif message.text == 'Вернуться в админку':
        bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
    else:
        bot.send_message(message.from_user.id, 'Вы должны ввести число!', reply_markup=admin_markup)



def set_rew_check(message):
    if message.text.isdigit():
        db.set_rew_checks(message.text)
        bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)
    elif message.text == 'Вернуться в админку':
        bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
    else:
        bot.send_message(message.from_user.id, 'Вы должны ввести число!', reply_markup=admin_markup)


def set_min_check(message):
    if message.text.isdigit():
        db.set_min_checks(message.text)
        bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)
    elif message.text == 'Вернуться в админку':
        bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
    else:
        bot.send_message(message.from_user.id, 'Вы должны ввести число!', reply_markup=admin_markup)

def set_max_check(message):
    if message.text.isdigit():
        db.set_max_checks(message.text)
        bot.send_message(message.from_user.id, 'Изменено!', reply_markup=admin_markup)
    elif message.text == 'Вернуться в админку':
        bot.send_message(message.from_user.id, 'Вы вернулись в админ панель', reply_markup=admin_markup)
    else:
        bot.send_message(message.from_user.id, 'Вы должны ввести число!', reply_markup=admin_markup)



def ins_promo(message):
    a = db.promo_add(message.from_user.id, message.text)
    if a == 'usernot':
        bot.send_message(message.from_user.id, 'Вы не можете активировать свой-же промокод😏', reply_markup=menu)
    elif a == 'time not end':
        bot.send_message(message.from_user.id, 'Вы можете активировать только один промокод в час😔', reply_markup=menu)
    elif a == 'not valid':
        bot.send_message(message.from_user.id, 'Промокод недействителен😔', reply_markup=menu)
    elif a == 'notpromo':
        bot.send_message(message.from_user.id, 'Такого промокода не существует😔', reply_markup=menu)
    elif a == 'failed':
        bot.send_message(message.from_user.id, 'Произошла ошибка, попробуйте чуть позже🤨')
    else:
        db.add_ref(db.check_crt_promo(message.text), message.from_user.id)
        bot.send_message(message.from_user.id, 'Вы активировали промокод на сумму: '+ a +' RUB 💵', reply_markup=menu)
        bot.send_message(db.check_crt_promo(message.text), '@'+ message.from_user.username + ' активировал ваш промокод!')

def check_message(message):
    try:
        if message.text == '📋В меню':
            bot.send_message(message.from_user.id, 'Вы в меню', reply_markup=menu)
        elif message.text.isdigit():
            i = float(db.check_balance(message.from_user.id))
            if (int(message.text) <= i or float(message.text) <= i) and (int(message.text) >= int(db.check_min_check()) or float(message.text) >= float(db.check_min_check())) and (int(message.text) <= int(db.check_max_check()) or float(message.text) <= float(db.check_max_check())):
                a = generate_check()
                bot.send_message(message.from_user.id, '📃Чек создан! \n'+
                                                       '💵<b>Сумма</b>: ' + message.text + ' RUB \n'+
                                                       'Ссылка, для активации чека: http://t.me/promocheck_bot?start=' + db.crt_ref(message.from_user.id) + '_' + a, reply_markup=menu, parse_mode='html')
                db.check_time(message.from_user.id, message.text, a)
            elif i == 'failed':
                bot.send_message(message.from_user.id, 'Произошла ошибка, попробуйте чуть позже')
            else:
                bot.send_message(message.from_user.id, 'Вы ввели неправльно число, вы были отправлены в меню', reply_markup=menu)
        
        else:
            bot.send_message(message.from_user.id, 'Произошла ошибка. Возможно вы ввели число с точкой либо буквы. Вы были отправлены в меню', reply_markup=menu)
    except Exception as ex:
        print(ex)    


def create_gen_promo(message):
    try:
        if message.text.isdigit():
            i = float(db.check_balance(message.from_user.id))
            if (int(message.text) <= i or float(message.text) <= i) and (int(message.text) >= int(db.check_min_promo()) or float(message.text) >= float(db.check_min_promo())) and (int(message.text) <= int(db.check_max_promo()) or float(message.text) <= float(db.check_max_promo())):
                a = generate_promo()
                bot.send_message(message.from_user.id, '📜Промокод создан! \n' +
                                                       '💵*Сумма*: ' + message.text + ' RUB \n' +
                                                       '📃*Промокод*: '+ '"' + a + '"' + ' \n' +
                                                       ' \n'+
                                                       '*Вписывать его без кавычек!*', reply_markup=promo_menu, parse_mode='Markdown')
                db.promo_set_time(a, message.text, message.from_user.id)
            elif i == 'failed':
                bot.send_message(message.from_user.id, 'Произошла ошибка, попробуйте чуть позже')
            elif i < int(message.text) or i < float(message.text):
                bot.send_message(message.from_user.id, 'Произошла ошибка. У вас недостаточно средств, пополните баланс. Вы были отправлены в меню', reply_markup=menu)
            else:
                bot.send_message(message.from_user.id, 'Произошла ошибка. Возможно вы ввели больше, чем указано в максимальной сумме промокода или меньше, чем в минимальной сумме. Вы были отправлены в меню', reply_markup=menu)
        elif message.text == '📋В меню':
            bot.send_message(message.from_user.id, 'Вы в меню', reply_markup=menu)
        
        else:
            bot.send_message(message.from_user.id, 'Произошла ошибка. Возможно вы ввели число с точкой либо буквы. Вы были отправлены в меню', reply_markup=menu)
    except Exception as ex:
        print(ex)

def create_self_promo(message):
    try:
        if message.text == '📋В меню':
            bot.send_message(message.from_user.id, 'Вы в меню', reply_markup=menu)
        else:
            if message.text.isdigit():
                i = float(db.check_balance(message.from_user.id))
                if (int(message.text) <= i or float(message.text) <= i) and (int(message.text) >= int(db.check_min_promo()) or float(message.text) >= float(db.check_min_promo())) and (int(message.text) <= int(db.check_max_promo()) or float(message.text) <= float(db.check_max_promo())):
                    db.promo_step1(message.text, message.from_user.id)

                    msg = bot.send_message(message.from_user.id, '📜Хорошо, а теперь введите промокод:', reply_markup=menu_back)
                    bot.register_next_step_handler(msg, create_self_promo2)
                elif i == 'failed':
                    bot.send_message(message.from_user.id, 'Произошла ошибка, попробуйте чуть позже')
                elif i < int(message.text) or i < float(message.text):
                    bot.send_message(message.from_user.id, 'Произошла ошибка. У вас недостаточно средств, пополните баланс. Вы были отправлены в меню', reply_markup=menu)
                else:
                    bot.send_message(message.from_user.id, 'Произошла ошибка. Возможно вы ввели больше, чем указано в максимальной сумме промокода или меньше, чем в минимальной сумме. Вы были отправлены в меню', reply_markup=menu)
            else:
                bot.send_message(message.from_user.id, 'Произошла ошибка. Возможно вы ввели число с точкой либо буквы. Вы были отправлены в меню', reply_markup=menu)

    except Exception as ex:
        print(ex)


def create_self_promo2(message):
    if message.text == '📋В меню':
        bot.send_message(message.from_user.id, 'Вы вернулись в меню', reply_markup=menu)
    else:
        a = db.promo_check(message.text)
        if a == 'Занято':
            bot.send_message(message.from_user.id, 'Этот промокод занят, попробуйте ещё раз', reply_markup=promo_menu)
        elif a == 'failed':
            bot.send_message(message.from_user.id, 'Произошла ошибка, попробуйте чуть позже')
        else:
            db.promo_step2(message.text, message.from_user.id)
            bot.send_message(message.from_user.id,'Промокод создан! \n'+
                                                '*Сумма*: ' + db.promo_sum_check(message.text, message.from_user.id) + ' RUB \n'+
                                                'Промокод: '+ '"' + message.text + '" \n'+
                                                '*Вписывать его без кавычек!*', reply_markup=promo_menu, parse_mode='Markdown')


def btc(message):
    try:
        if isfloat(message.text) == True:
            a = db.btc_add(message.text, message.from_user.id)
            if a == 'no':
                bot.send_message(message.from_user.id, '📈Вы уже прогнозировали курс биткоина. Вы были отправлены в меню', reply_markup=menu)
            elif a == 'failed':
                bot.send_message(message.from_user.id, 'Произошла ошибка😔, попробуйте чуть позже')
            elif a == 'nottime':
                bot.send_message(message.from_user.id, 'Увы, но слишком поздно. Регистрация заканчивается за 3 часа до итогов', reply_markup=menu)
            else:
                bot.send_message(message.from_user.id, 'Хорошо, ваш прогноз ' + message.text + ' записан!😁')
        elif isfloat(message.text) == False:
            bot.send_message(message.from_user.id, '😔Вы должны ввести число. Вы были отправлены в меню', reply_markup=menu)
        elif message.text == '📋В меню':
            bot.send_message(message.from_user.id, 'Вы в меню', reply_markup=menu)
    except Exception as ex:
        print(ex)

def btc_work(btc_value1):
    a = db.check_win_btc(btc_value1)
    b = db.add_btc_win(a)
    bot.send_message(a, 'Ваш прогноз на курс биткоина оправдался📈 \n'+
                        'Вы заняли 3-е место! \n'
                        'Вам было начислено '+ b + ' RUB на баланс!💵', reply_markup=menu)


def ticket_win_send(user_id):
    bot.send_message(user_id, 'Вы заняли призовое место по количеству билетов! Проверьте ваш баланс!💵')

def jackpot_win_send(quant):
    a = db.select_user_jack(quant)
    bot.send_message(a, 'Вы выиграли в джекпоте! Проверьте ваш баланс 💵')

def qiwi_sets(message):
    if message.text.isdigit():
        db.set_qiwi(message.from_user.id, message.text)
        bot.send_message(message.from_user.id, 'Вы успешно привязали ваш QIWI кошелек!', reply_markup=menu)
    elif message.text == '🔙Вернуться':
        a = db.check_qiwi_num(message.from_user.id)
        if a != 'not qiwi':
            bot.send_message(message.from_user.id, '<b>💵Ваш баланс</b>: '+ db.check_balance(message.from_user.id) + ' RUB \n' +
                                                    '<b>💸Доступно для вывода</b>: '+ db.check_balance(message.from_user.id) + ' RUB \n'+
                                                    '<b>🎫Билетов</b>: '+ db.check_ticket(message.from_user.id) + ' \n'+
                                                    # '<b>На выводе</b>: '+ db.check_on_withdraw(message.from_user.id) +' RUB \n' +
                                                    # '<b>Заработано</b>: '+ db.check_earn(message.from_user.id) +' RUB \n '+
                                                    '<b>QIWI кошелек</b>: '+ db.check_qiwi_num(message.from_user.id) + ' \n'+
                                                    '<b>Payeer номер счета</b>:'+ db.check_payeer_num(message.from_user.id), reply_markup=profile_menu, parse_mode='html')
            bot.send_message(message.from_user.id, 'Если вы хотите изменить свой QIWI кошелек - нажмите на кнопку ниже: ', reply_markup=qiwi_set)
        elif a == 'not qiwi':
            bot.send_message(message.from_user.id, '<b>💵Ваш баланс</b>: '+ db.check_balance(message.from_user.id) + ' RUB \n' +
                                                    '<b>💸Доступно для вывода</b>: '+ db.check_balance(message.from_user.id) + ' RUB \n'+
                                                    '<b>🎫Билетов</b>: '+ db.check_ticket(message.from_user.id) + ' \n'+
                                                    # '<b>На выводе</b>: '+ db.check_on_withdraw(message.from_user.id) +' RUB \n' +
                                                    # '<b>Заработано</b>: '+ db.check_earn(message.from_user.id) +' RUB \n '+
                                                    '<b>QIWI кошелек</b>: '+ db.check_qiwi_num(message.from_user.id) + ' \n'+
                                                    '<b>Payeer номер счета</b>:'+ db.check_payeer_num(message.from_user.id), reply_markup=profile_menu, parse_mode='html')
            bot.send_message(message.from_user.id, 'Привяжите QIWI кошелек по кнопке ниже:', reply_markup=qiwi_set)
    else:
        bot.send_message(message.from_user.id, 'Вы неправильно ввели QIWI кошелек и были отправлены в меню', reply_markup=menu)



@bot.callback_query_handler(func = lambda call: True)
def promo_callback(c):
    try:
        # Обработчик промокодов
        
        if c.data == 'Отмена':
            bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
            bot.send_message(c.from_user.id, 'Вы вернулись назад', reply_markup=promo_menu)
    
        elif c.data == 'Генерация промокода':
            msg = bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='💵*Баланс*: '+ db.check_balance(c.from_user.id) +' RUB \n'+
                                                                                                          '💴*Минимальная сумма для создания промокода*: ' + db.check_min_promo() + ' RUB \n'+
                                                                                                          '💶*Максимальная сумма для создания промокода*: ' + db.check_max_promo() + ' RUB \n'+
                                                                                                          ' \n'+
                                                                                                          'Введите сумму промокода:', parse_mode='Markdown')
            bot.register_next_step_handler(msg, create_gen_promo)
        elif c.data == 'Ввод промокода':
            msg = bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='💵*Баланс*: '+ db.check_balance(c.from_user.id) + ' RUB \n'+
                                                                                                         '💴*Минимальная сумма для создания промокода*: ' + db.check_min_promo() + ' RUB \n'+
                                                                                                         '💶*Максимальная сумма для создания промокода*: ' + db.check_max_promo() + ' RUB \n'+
                                                                                                         ' \n'+
                                                                                                         'Введите сумму промокода:', parse_mode='Markdown')
            bot.register_next_step_handler(msg, create_self_promo)

        # Обработчик игровых комнат

        elif c.data == 'Отмена игры1':
            
            a = db.exit_room('1', c.from_user.id)
            
            if a == 'ok':
                bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
                bot.send_message(c.from_user.id, 'Вы вышли из комнаты.😔 Деньги были возврашены на ваш баланс')
                bot.send_message(c.from_user.id, 'В этом разделе можно играть в 6-ти комнатах с реальными людьми! \n'+
                                                'В каждой комнате по 5 игроков. Как только комната заполняется, бот выбирает победителя!', reply_markup=rooms())

            elif a == 'no':
                bot.send_message(c.from_user.id, 'Произошла ошибка. Попробуйте ещё раз, либо свяжитесь с поддержкой', reply_markup=menu)
            elif a == 'failed':
                bot.send_message(c.from_user.id, 'Произошла ошибка, попробуйте чуть позже')
            elif a == 'nottime':
                bot.send_message(c.from_user.id, '⏱Ещё не прошло 3 часа с момента входа в комнату!')


        elif c.data == 'Отмена игры2':
            
            a = db.exit_room('2', c.from_user.id)
            if a == 'ok':
                bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
                bot.send_message(c.from_user.id, 'Вы вышли с комнаты.😔 Деньги были возврашены на ваш баланс')
                bot.send_message(c.from_user.id, 'В этом разделе можно играть в 6-ти комнатах с реальными людьми! \n'+
                                                'В каждой комнате по 5 игроков. Как только комната заполняется, бот выбирает победителя!', reply_markup=rooms())

            elif a == 'no':
                bot.send_message(c.from_user.id, 'Произошла ошибка. Попробуйте ещё раз, либо свяжитесь с поддержкой', reply_markup=menu)
            elif a == 'failed':
                bot.send_message(c.from_user.id, 'Произошла ошибка, попробуйте чуть позже')
            elif a == 'nottime':
                bot.send_message(c.from_user.id, '⏱Ещё не прошло 3 часа с момента входа в комнату!')

        
        elif c.data == 'Отмена игры3':
            
            a = db.exit_room('3', c.from_user.id)
            if a == 'ok':
                bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
                bot.send_message(c.from_user.id, 'Вы вышли с комнаты.😔 Деньги были возврашены на ваш баланс')
                bot.send_message(c.from_user.id, 'В этом разделе можно играть в 6-ти комнатах с реальными людьми! \n'+
                                                'В каждой комнате по 5 игроков. Как только комната заполняется, бот выбирает победителя!', reply_markup=rooms())

            elif a == 'no':
                bot.send_message(c.from_user.id, 'Произошла ошибка. Попробуйте ещё раз, либо свяжитесь с поддержкой', reply_markup=menu)
            elif a == 'failed':
                bot.send_message(c.from_user.id, 'Произошла ошибка, попробуйте чуть позже')
            elif a == 'nottime':
                bot.send_message(c.from_user.id, '⏱Ещё не прошло 3 часа с момента входа в комнату!')


        elif c.data == 'Отмена игры4':
            
            a = db.exit_room('4', c.from_user.id)
            if a == 'ok':
                bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
                bot.send_message(c.from_user.id, 'Вы вышли с комнаты.😔 Деньги были возврашены на ваш баланс')
                bot.send_message(c.from_user.id, 'В этом разделе можно играть в 6-ти комнатах с реальными людьми! \n'+
                                                'В каждой комнате по 5 игроков. Как только комната заполняется, бот выбирает победителя!', reply_markup=rooms())

            elif a == 'no':
                bot.send_message(c.from_user.id, 'Произошла ошибка. Попробуйте ещё раз, либо свяжитесь с поддержкой', reply_markup=menu)
            elif a == 'failed':
                bot.send_message(c.from_user.id, 'Произошла ошибка, попробуйте чуть позже')
            elif a == 'nottime':
                bot.send_message(c.from_user.id, '⏱Ещё не прошло 3 часа с момента входа в комнату!')


        elif c.data == 'Отмена игры5':
            
            a = db.exit_room('5', c.from_user.id)
            if a == 'ok':
                bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
                bot.send_message(c.from_user.id, 'Вы вышли с комнаты.😔 Деньги были возврашены на ваш баланс')
                bot.send_message(c.from_user.id, 'В этом разделе можно играть в 6-ти комнатах с реальными людьми! \n'+
                                                'В каждой комнате по 5 игроков. Как только комната заполняется, бот выбирает победителя!', reply_markup=rooms())

            elif a == 'no':
                bot.send_message(c.from_user.id, 'Произошла ошибка. Попробуйте ещё раз, либо свяжитесь с поддержкой', reply_markup=menu)
            elif a == 'failed':
                bot.send_message(c.from_user.id, 'Произошла ошибка, попробуйте чуть позже')
            elif a == 'nottime':
                bot.send_message(c.from_user.id, '⏱Ещё не прошло 3 часа с момента входа в комнату!')


        elif c.data == 'Отмена игры6':
            print(c.data)
            
            a = db.exit_room('6', c.from_user.id)
            if a == 'ok':
                bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
                bot.send_message(c.from_user.id, 'Вы вышли с комнаты.😔 Деньги были возврашены на ваш баланс')
                bot.send_message(c.from_user.id, 'В этом разделе можно играть в 6-ти комнатах с реальными людьми! \n'+
                                                 'В каждой комнате по 5 игроков. Как только комната заполняется, бот выбирает победителя!', reply_markup=rooms())

            elif a == 'no':
                bot.send_message(c.from_user.id, 'Произошла ошибка. Попробуйте ещё раз, либо свяжитесь с поддержкой', reply_markup=menu)
            elif a == 'failed':
                bot.send_message(c.from_user.id, 'Произошла ошибка, попробуйте чуть позже')
            elif a == 'nottime':
                bot.send_message(c.from_user.id, '⏱Ещё не прошло 3 часа с момента входа в комнату!')
            
        
        elif c.data == 'Комната1':
            a = db.add_to_room('1', c.from_user.id)
            if a == 'ok':
                bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='Вы были зарегистрированы в комнате №1. Ожидайте результатов!', reply_markup=otmena_room1)
            elif a == 'no':
                bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='Вы уже зарегистрированы в этой комнате и были перемещены в меню с комнатами')
                bot.send_message(c.from_user.id, 'В этом разделе можно играть в 6-ти комнатах с реальными людьми! \n'+
                                                 'В каждой комнате по 5 игроков. Как только комната заполняется, бот выбирает победителя!', reply_markup=rooms())
            elif a == 'no_bal':
                bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='У вас не хватает денег на балансе. Вы были перемещены в меню с комнатами')
                bot.send_message(c.from_user.id, 'В этом разделе можно играть в 6-ти комнатах с реальными людьми! \n'+
                                                 'В каждой комнате по 5 игроков. Как только комната заполняется, бот выбирает победителя!', reply_markup=rooms())
            elif a == 'go':
                a = check_win('1')
                bot.send_message(a, 'Поздравляем, вы выиграли! Вам на баланс было начислены деньги!')
                b = db.check_lose(a, '1')
                db.win_room('1', a)
                db.room_quant(a)
                z = []
                print(b)
                for row in b:
                    z.append(int(row[0]))
                for i in z:
                    db.room_quant(i)
                    bot.send_message(i, 'К сожалению вы проиграли')
                db.del_room('1')
            elif a == 'failed':
                bot.send_message(c.from_user.id, 'Произошла ошибка, попробуйте чуть позже')

                                                
        elif c.data == 'Комната2':
            a = db.add_to_room('2', c.from_user.id)
            if a == 'ok':
                bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='Вы были зарегистрированы в комнате №2. Ожидайте результатов!', reply_markup=otmena_room2)
            elif a == 'no':
                bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='Вы уже зарегистрированы в этой комнате')
            elif a == 'no_bal':
                bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='У вас не хватает денег на балансе. Вы были перемещены в меню с комнатами')
                bot.send_message(c.from_user.id, 'В этом разделе можно играть в 6-ти комнатах с реальными людьми! \n'+
                                                 'В каждой комнате по 5 игроков. Как только комната заполняется, бот выбирает победителя!', reply_markup=rooms())
            elif a == 'go':
                a = check_win('2')
                bot.send_message(a, 'Поздравляем, вы выиграли! Вам на баланс было начислены деньги!')
                b = db.check_lose(a, '2')
                db.win_room('2', a)
                z = []
                print(b)
                db.room_quant(a)
                for row in b:
                    z.append(int(row[0]))
                for i in z:
                    db.room_quant(i)
                    bot.send_message(i, 'К сожалению вы проиграли')
                db.del_room('2')
            elif a == 'failed':
                bot.send_message(c.from_user.id, 'Произошла ошибка, попробуйте чуть позже')

        elif c.data == 'Комната3':
            a = db.add_to_room('3', c.from_user.id)
            if a == 'ok':
                bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='Вы были зарегистрированы в комнате №3. Ожидайте результатов!', reply_markup=otmena_room3)
            elif a == 'no':
                bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='Вы уже зарегистрированы в этой комнате')
            elif a == 'no_bal':
                bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='У вас не хватает денег на балансе. Вы были перемещены в меню с комнатами')
                bot.send_message(c.from_user.id, 'В этом разделе можно играть в 6-ти комнатах с реальными людьми! \n'+
                                                 'В каждой комнате по 5 игроков. Как только комната заполняется, бот выбирает победителя!', reply_markup=rooms())
            elif a == 'go':
                a = check_win('3')
                bot.send_message(a, 'Поздравляем, вы выиграли! Вам на баланс было начислены деньги!')
                b = db.check_lose(a, '3')
                db.win_room('3', a)
                z = []
                print(b)
                db.room_quant(a)
                for row in b:
                    z.append(int(row[0]))
                for i in z:
                    db.room_quant(i)
                    bot.send_message(i, 'К сожалению вы проиграли')
                db.del_room('3')
            elif a == 'failed':
                bot.send_message(c.from_user.id, 'Произошла ошибка, попробуйте чуть позже')


        elif c.data == 'Комната4':
            a = db.add_to_room('4', c.from_user.id)
            if a == 'ok':
                bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='Вы были зарегистрированы в комнате №4. Ожидайте результатов!', reply_markup=otmena_room4)
            elif a == 'no':
                bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='Вы уже зарегистрированы в этой комнате')
            elif a == 'no_bal':
                bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='У вас не хватает денег на балансе. Вы были перемещены в меню с комнатами')
                bot.send_message(c.from_user.id, 'В этом разделе можно играть в 6-ти комнатах с реальными людьми! \n'+
                                                 'В каждой комнате по 5 игроков. Как только комната заполняется, бот выбирает победителя!', reply_markup=rooms())
            elif a == 'go':
                a = check_win('4')
                bot.send_message(a, 'Поздравляем, вы выиграли! Вам на баланс было начислены деньги!')
                b = db.check_lose(a, '4')
                db.win_room('4', a)
                z = []
                print(b)
                db.room_quant(a)
                for row in b:
                    z.append(int(row[0]))
                for i in z:
                    db.room_quant(i)
                    bot.send_message(i, 'К сожалению вы проиграли')
                db.del_room('4')
            elif a == 'failed':
                bot.send_message(c.from_user.id, 'Произошла ошибка, попробуйте чуть позже')

        elif c.data == 'Комната5':
            a = db.add_to_room('5', c.from_user.id)
            if a == 'ok':
                bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='Вы были зарегистрированы в комнате №5. Ожидайте результатов!', reply_markup=otmena_room5)
            elif a == 'no':
                bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='Вы уже зарегистрированы в этой комнате')
            elif a == 'no_bal':
                bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='У вас не хватает денег на балансе. Вы были перемещены в меню с комнатами')
                bot.send_message(c.from_user.id, 'В этом разделе можно играть в 6-ти комнатах с реальными людьми! \n'+
                                                 'В каждой комнате по 5 игроков. Как только комната заполняется, бот выбирает победителя!', reply_markup=rooms())
            elif a == 'go':
                a = check_win('5')
                bot.send_message(a, 'Поздравляем, вы выиграли! Вам на баланс было начислены деньги!')
                b = db.check_lose(a, '5')
                db.win_room('5', a)
                z = []
                print(b)
                db.room_quant(a)
                for row in b:
                    z.append(int(row[0]))
                for i in z:
                    db.room_quant(i)
                    bot.send_message(i, 'К сожалению вы проиграли')
                
            elif a == 'failed':
                bot.send_message(c.from_user.id, 'Произошла ошибка, попробуйте чуть позже')

        elif c.data == 'Комната6':
            a = db.add_to_room('6', c.from_user.id)
            if a == 'ok':
                bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='Вы были зарегистрированы в комнате №6. Ожидайте результатов!', reply_markup=otmena_room6)
            elif a == 'no':
                bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='Вы уже зарегистрированы в этой комнате')
            elif a == 'no_bal':
                bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='У вас не хватает денег на балансе. Вы были перемещены в меню с комнатами')
                bot.send_message(c.from_user.id, 'В этом разделе можно играть в 6-ти комнатах с реальными людьми! \n'+
                                                 'В каждой комнате по 5 игроков. Как только комната заполняется, бот выбирает победителя!', reply_markup=rooms())
            elif a == 'go':
                a = check_win('6')
                bot.send_message(a, 'Поздравляем, вы выиграли! Вам на баланс были начислены деньги!🤑')
                b = db.check_lose(a, '6')
                db.win_room('6', a)
                z = []
                print(b)
                db.room_quant(a)
                for row in b:
                    z.append(int(row[0]))
                for i in z:
                    db.room_quant(i)
                    bot.send_message(i, 'К сожалению вы проиграли😔')
                print(z)
            elif a == 'failed':
                bot.send_message(c.from_user.id, 'Произошла ошибка, попробуйте чуть позже')
        
        elif c.data == 'Привязка киви':
            bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
            msg = bot.send_message(chat_id=c.message.chat.id, text='Введите ваш кошелек без "+"', reply_markup=profile_back)
            bot.register_next_step_handler(msg, qiwi_sets)
        
        elif c.data == 'Привязка Payeer':
            bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
            msg = bot.send_message(chat_id=c.message.chat.id, text='Введите номер счета Payeer (Пример: Р123456789): ', reply_markup=profile_back)
            bot.register_next_step_handler(msg, payeer_sets)

        elif c.data == 'Вывод одобрен':
            a = c.message.text.split()
            b = db.with_accept(a[5].split('№')[1])
            bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
            bot.send_message(c.message.chat.id, 'Заявка одобрена!😁')
            bot.send_message(b, '💸Ваша заявка была одобрена! Ожидайте начисление денег на ваш кошелек!💸')
            bot.send_message(c.message.chat.id, api.get_pay_url(int(a[11]), "check promo bot", a[19]))

        elif c.data == 'Вывод отказан':
            a = c.message.text.split()
            b = db.with_decline(a[5].split('№')[1])
            bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
            bot.send_message(c.message.chat.id, 'Заявка отклонена!😔')
            bot.send_message(b, 'Ваша заявка была отклонена! Деньги вернулись на баланс')
        
        elif c.data == 'Вывод одобрен pay':
            a = c.message.text.split()
            bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
            bot.send_message(c.message.chat.id, 'Пользователь получил сообщение о том, что деньги поступили на его счет!')
            bot.send_message(a[7], '💸На ваш счет Payeer поступили средства!💸')
        
        elif c.data == 'Вывод отказан pay':
            a = c.message.text.split()
            bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
            db.balance_add(a[7], a[9])
            bot.send_message(c.message.chat.id, 'Заявка отклонена!😔')
            bot.send_message(a[7], 'Ваша заявка была отклонена! Деньги вернулись на баланс')
        
        elif c.data == 'dice':
            a = db.dice_step2(c.from_user.id)
            result = random.choices(['user', 'bot'], weights=[40, 60])[0]
            bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
            if result == 'user':
                db.balance_add(c.from_user.id, a)
                bot.send_message(c.from_user.id, 'Поздравляем, вы победили! Вам на баланс начислено '+str(a)+' RUB', reply_markup=menu)
                if int(a) >= 10:
                    db.add_ticket(c.from_user.id)
            elif result == 'bot':
                db.balance_with(c.from_user.id, a)
                
                if int(a) >= 10:
                    db.add_ticket(c.from_user.id)
                    bot.send_message(c.from_user.id, 'К сожалению, вы проиграли, но вам начислен 1 билет', reply_markup=menu)
                else:
                    bot.send_message(c.from_user.id, 'К сожалению, вы проиграли', reply_markup=menu)

        elif c.data == 'Проверка':
            
            
            user_id = c.from_user.id
            for j in db.check_channels():
                check_member_list = []
                check_member_list.append(j[0])
                for i in check_member_list:
                    try:
                        print(check_member_list)
                        a = bot.get_chat_member(i, user_id)
                        
                        
                    except Exception:
                        bot.send_message(user_id, 'Вы не подписаны на каналы. Подпишитесь, чтобы продолжить')
                        return
            bot.send_message(c.message.chat.id, 'Добро пожаловать!', reply_markup=menu)
            db.ins_subs(c.from_user.id)

        elif c.data == 'send':
            bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
            usr_id = db.send_msg()
            for i in usr_id:
                bot.send_message(i[0], c.message.text)
            bot.send_message(c.from_user.id, 'Отправлено!', reply_markup=admin_markup)

        elif c.data == 'canc':
            bot.delete_message(chat_id=c.message.chat.id, message_id=c.message.message_id)
            bot.send_message(c.from_user.id, 'Вы были отправлены в админ панель', reply_markup=admin_markup)

                
                    


    except Exception as ex:
        print(ex)



    

@api.bind_check(operation=(OperationType.ALL))
def waiter(payment):
    if payment.type == OperationType.IN:
        time_24 = one_day + datetime.datetime.now(tz_moscow)
        if payment.date > time_24.strftime("%Y-%m-%dT%H:%M%z"):
            if payment.status == PaymentStatus.SUCCESS:
                a = db.ins_dep(str(payment.comment), str(payment.amount), str(payment.transaction_id))



    


if __name__ == '__main__':
    ScheduleWork.start_process()
    api.start_threading()
    try:
        bot.polling(none_stop=True)
    except:
        pass