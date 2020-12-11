from database import SQL
from telebot import types
from buttons import menu, menu_back
import secrets
import string
db = SQL('localhost', 'domaildo_usrbbd6', 'e5svFRqYtG8SdB^P=)', 'domaildo_boottrg06')


def check_ref(text):
    a = text.replace(' ','_').split('_')
    print(a)
    

    if len(a) == 1:
        return '1'
    elif len(a) == 2:
        return a
    elif len(a) == 3:
        return a


def generate_check():
    letters_and_digits = string.ascii_letters + string.digits
    check = ''.join(secrets.choice(
    letters_and_digits) for i in range(32))
    return check


def generate_promo():
    letters_and_digits = string.ascii_letters + string.digits
    check = ''.join(secrets.choice(
    letters_and_digits) for i in range(8))
    return check

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False



