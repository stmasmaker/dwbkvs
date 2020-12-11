from config import bot
from database import SQL
import random


db = SQL('localhost', 'domaildo_usrbbd6', 'e5svFRqYtG8SdB^P=)', 'domaildo_boottrg06')




def check_win(room):

    a = []
    for i in db.list_players(room):
        a.append(int(i[0]))
    result = random.choice(a)
    return result


