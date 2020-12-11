import pymysql




class SQL:
    def __init__ (self, host, user, password, dbname):
        self.connection = pymysql.connect(host, user, password, dbname)
        self.cursor = self.connection.cursor()

    def check_user(self, user_id):
        self.cursor.execute('SELECT `user_id` FROM `users` WHERE `user_id`=%s', (user_id))
        result = self.cursor.fetchall()
        self.connection.commit()
        return(bool(len(result)))

    def check_ban_user(self, username):
        self.cursor.execute('SELECT `username` FROM `banlist` WHERE `username`=%s', (username))
        result = self.cursor.fetchall()
        self.connection.commit()
        return(bool(len(result)))

    def add_user(self, user_id, username):
        self.cursor.execute('INSERT INTO `users` (`user_id`, `username`, `time_user`) VALUES (%s, %s, now())', (user_id, username))
        self.connection.commit()
        return

    def add_ref(self, ref_id, user_id):


        self.cursor.execute('SELECT `referal` FROM `users` WHERE `user_id`=%s', (user_id))
        result = self.cursor.fetchall()
        result_row = '0'
        for row in result:
            result_row = row[0]
        print(result_row)
        
        if result_row == None:

            self.cursor.execute('UPDATE `users` SET `referal`=%s WHERE `user_id`=%s', (ref_id, user_id))
            self.cursor.execute('UPDATE `users` SET `referals_quant`=referals_quant+1, `tickets`=tickets+1, `balance`=balance+0.5 WHERE `user_id`=%s', (ref_id))

            self.connection.commit()
            return
        else:
            return

    def check_ref(self, user_id):
        self.cursor.execute('SELECT `referal` FROM `users` WHERE `user_id`=%s', (user_id))
        result = self.cursor.fetchall()
        for row in result:
            self.connection.commit()
            return row[0]


    def crt_ref(self, user_id):
        self.cursor.execute('SELECT `user_id` FROM `users` WHERE `user_id`=%s', (user_id))
        result = self.cursor.fetchall()
        for row in result:
            self.connection.commit()
            return row[0]

    def check_balance(self, user_id):
        self.cursor.execute('SELECT `balance` FROM `users` WHERE `user_id`=%s', (user_id))
        result = self.cursor.fetchall()

        for row in result:
            self.connection.commit()
            return row[0]

    def check_withdraw(self, user_id):
        self.cursor.execute('SELECT `balance` FROM `users` WHERE `user_id`=%s', (user_id))
        result = self.cursor.fetchall()
        for row in result:
            self.connection.commit()
            return row[0]

    def check_on_withdraw(self, user_id):
        self.cursor.execute('SELECT `balance` FROM `users` WHERE `user_id`=%s', (user_id))
        result = self.cursor.fetchall()
        for row in result:
            self.connection.commit()
            return row[0]

    def check_referals(self, user_id):
        self.cursor.execute('SELECT `referals_quant` FROM `users` WHERE `user_id`=%s', (user_id))
        result = self.cursor.fetchall()
        for row in result:
            self.connection.commit()
            return row[0]

    def check_earn(self, user_id):
        self.cursor.execute('SELECT `earned` FROM `users` WHERE `user_id`=%s', (user_id))
        result = self.cursor.fetchall()
        for row in result:
            self.connection.commit()
            return row[0]
    
    def check_users(self):
        self.cursor.execute('SELECT `user_id` FROM `users`')
        result = self.cursor.fetchall()
        self.connection.commit()
        return str(len(result))

    def checks_sum(self):
        self.cursor.execute('SELECT `sum` FROM `check`')
        result = self.cursor.fetchall()
        summ = 0
        for row in result:
            summ = summ + int(row[0])
        self.connection.commit()
        return str(summ)

    def promos_sum(self):
        self.cursor.execute('SELECT `sum` FROM `promo`')
        result = self.cursor.fetchall()
        summ = 0
        for row in result:
            summ = summ + int(row[0])
        self.connection.commit()
        return str(summ)

    def check_sums(self, user_id):
        self.cursor.execute('SELECT `sum` FROM `check` WHERE `crt_usr_id`=%s', (user_id))
        result = self.cursor.fetchall()
        for row in result:
            self.connection.commit()
            return int(row[0])

    def check_time(self, user_id, summ, check_id):
        self.cursor.execute('INSERT INTO `check` (`crt_usr_id`, `sum`, `time_now`, `time_check`, `valid`, `check_id`) VALUES (%s, %s, curtime(), (curtime() + INTERVAL 1 hour), "1", %s)', (user_id, summ, check_id))
        self.cursor.execute('UPDATE `users` SET `balance`=balance-%s WHERE `user_id`=%s', (summ, user_id))
        self.connection.commit()
        return
    


    def check_add(self, user_id, check_id, create_id):
        self.cursor.execute('SELECT `valid` FROM `check` WHERE `check_id`=%s', (check_id))
        result = self.cursor.fetchall()
        b = '0'
        for row in result:
            b = row[0]
        if b == 1:
            self.cursor.execute('SELECT `last_check` FROM `users` WHERE `user_id`=%s', (user_id))
            result = self.cursor.fetchall()
            i = '0'
            for row in result:
                i = row[0]
            self.cursor.execute('SELECT now()')
            time = self.cursor.fetchall()
            a = '0'
            for row in time:
                a = row[0]
            self.cursor.execute('SELECT `set_check_money` FROM `admin_set`')
            money_withdraw1 = self.cursor.fetchall()
            money_withdraw = '0'
            for row in money_withdraw1:
                money_withdraw = int(row[0])
            
            if bool(i) == False:
                
                self.cursor.execute('SELECT `user_id` FROM `users` WHERE `user_id`=%s', (user_id))
                result1 = self.cursor.fetchall()
                result1_row = '0'
                for row in result1:
                    result1_row = row[0]
                self.cursor.execute('SELECT `crt_usr_id` FROM `check` WHERE `crt_usr_id`=%s', (create_id))
                result2 = self.cursor.fetchall()
                result2_row = '0'
                for row in result2:
                    result2_row = row[0]
                
                if result1_row != result2_row:

                    self.cursor.execute('SELECT `sum` FROM `check` WHERE `check_id`=%s', (check_id))
                    result = self.cursor.fetchall()
                    a = '0'
                    for row in result:
                        a = row[0]
                    self.cursor.execute('UPDATE `users` SET `balance`=balance+%s, `last_check`=(now() + INTERVAL 1 hour) WHERE `user_id`=%s', (a, user_id))
                    self.cursor.execute('UPDATE `users` SET `balance`=balance+0.5 WHERE `user_id`=%s', ( create_id))
                    self.cursor.execute('UPDATE `check` SET `valid`=0 WHERE `check_id`=%s', (check_id))
                    self.connection.commit()

                    return a
                elif result1_row == result2_row:
                    self.connection.commit()
                    return 'usernot'
            elif bool(i) == True:
                
                c = i<a
                print(c)
                if c == False:
                    self.connection.commit()
                    return 'time not end'
                elif c == True:
                    self.cursor.execute('SELECT `user_id` FROM `users` WHERE `user_id`=%s', (user_id))
                    result1 = self.cursor.fetchall()
                    result1_row = '0'
                    for row in result1:
                        result1_row = row[0]
                    self.cursor.execute('SELECT `crt_usr_id` FROM `check` WHERE `crt_usr_id`=%s', (create_id))
                    result2 = self.cursor.fetchall()
                    result2_row = '0'
                    for row in result2:
                        result2_row = row[0]
                    
                    if result1_row != result2_row:

                        self.cursor.execute('SELECT `sum` FROM `check` WHERE `check_id`=%s', (check_id))
                        result = self.cursor.fetchall()
                        a = '0'
                        for row in result:
                            a = row[0]
                        self.cursor.execute('UPDATE `users` SET `balance`=balance+%s, `last_check`=(now() + INTERVAL 1 hour) WHERE `user_id`=%s', (a, user_id))
                        self.cursor.execute('UPDATE `users` SET `balance`=balance+0.5 WHERE `user_id`=%s', (create_id))
                        self.cursor.execute('UPDATE `check` SET `valid`=0 WHERE `check_id`=%s', (check_id))
                        self.connection.commit()

                        return a
                    
                    elif result1_row == result2_row:
                        self.connection.commit()
                        return 'usernot'
        
        elif b == 0:
            self.connection.commit()
            return 'not valid'


    def check_crt(self, check_id):
        self.cursor.execute('SELECT `crt_usr_id` FROM `check` WHERE `check_id`=%s', (check_id))
        result = self.cursor.fetchall()
        a = '0'
        for row in result:
            a = row[0]
        print(a)
        if a == '0':
            return 'failed'
        elif a != '0':
            return a



    def check_money_check(self):
        self.cursor.execute('SELECT `set_check_money` FROM `admin_set`')
        result = self.cursor.fetchall()
        for row in result:
            self.connection.commit()
            return row[0]

    def check_promo_check(self):
        self.cursor.execute('SELECT `set_promo_money` FROM `admin_set`')
        result = self.cursor.fetchall()
        for row in result:
            self.connection.commit()
            return row[0]

    def check_min_check(self):
        self.cursor.execute('SELECT `set_min_check` FROM `admin_set`')
        result = self.cursor.fetchall()
        for row in result:
            self.connection.commit()
            return row[0]

    def check_max_check(self):
        self.cursor.execute('SELECT `set_max_check` FROM `admin_set`')
        result = self.cursor.fetchall()
        for row in result:
            self.connection.commit()
            return row[0]

    def check_min_promo(self):
        self.cursor.execute('SELECT `set_min_promo` FROM `admin_set`')
        result = self.cursor.fetchall()
        for row in result:
            self.connection.commit()
            return row[0]

    def check_max_promo(self):
        self.cursor.execute('SELECT `set_max_promo` FROM `admin_set`')
        result = self.cursor.fetchall()
        for row in result:
            self.connection.commit()
            return row[0]

    def check_promo_time(self):
        self.cursor.execute('SELECT `set_promo_hours` FROM `admin_set`')
        result = self.cursor.fetchall()
        for row in result:
            self.connection.commit()
            return row[0]

    def promo_set_time(self, promo_name, summ, create_id):
        self.cursor.execute('SELECT `set_promo_hours` FROM `admin_set`')
        result = self.cursor.fetchall()
        time = '0'
        for row in result:
            time = row[0]
        self.cursor.execute('UPDATE `users` SET `balance`=balance-%s WHERE `user_id`=%s',(summ, create_id))
        self.cursor.execute('INSERT INTO `promo` (`name_promo`, `sum`, `crt_usr_id`, `date_end`) VALUES (%s, %s, %s, (now() + INTERVAL %s hour))', (promo_name, summ, create_id, time))
        self.connection.commit()
        return

    def promo_step1(self, summ, create_id):
            self.cursor.execute('DELETE FROM `crt_promo` WHERE `crt_usr_id`=%s', (create_id))
            self.cursor.execute('INSERT INTO `crt_promo` (`sum`, `crt_usr_id`) VALUES (%s,%s)', (summ, create_id))
            self.connection.commit()
            return

    def promo_check(self, promo_name):
        self.cursor.execute('SELECT `name_promo` FROM `promo`')
        result = self.cursor.fetchall()
        for row in result:
            if row[0] == promo_name:
                self.connection.commit()
                return 'Занято'
        self.cursor.execute('UPDATE `crt_promo` SET `promo_name`=%s ', (promo_name))
        self.connection.commit()

    def promo_step2(self, promo_name, create_id):
        self.cursor.execute('SELECT `set_promo_hours` FROM `admin_set`')
        result = self.cursor.fetchall()
        time = '0'
        for row in result:
            time = row[0]
        self.cursor.execute('SELECT `sum` FROM `crt_promo` WHERE `crt_usr_id`=%s', (create_id))
        result1 = self.cursor.fetchall()
        result1_row = '0'
        for row in result1:
            result1_row = row[0]
        self.cursor.execute('INSERT INTO `promo` (`name_promo`, `sum`, `crt_usr_id`, `date_end`) VALUES (%s, %s, %s, (now() + INTERVAL %s hour))', (promo_name, result1_row, create_id, time))
        self.cursor.execute('UPDATE `users` SET `balance`=balance-%s WHERE `user_id`=%s', (result1_row, create_id))
        self.connection.commit()
        return

    # Проверяем сумму промокода
    def promo_sum_check(self, promo_name, create_id):
        self.cursor.execute('SELECT `sum` FROM `promo` WHERE `name_promo`=%s AND `crt_usr_id`=%s', (promo_name, create_id))
        result = self.cursor.fetchall()
        for row in result:
            self.connection.commit()
            return row[0]


    def promo_add(self, user_id, promo_name):
        

        self.cursor.execute('SELECT `valid` FROM `promo` WHERE `name_promo`=%s', (promo_name))
        result = self.cursor.fetchall()
        b = '0'
        for row in result:
            b = row[0]
        if b == '0':
            return 'notpromo'
        elif b != '0':

            self.cursor.execute('SELECT `crt_usr_id` FROM `promo` WHERE `name_promo`=%s', (promo_name))
            create_id1 = self.cursor.fetchall()
            create_id = '0'
            for row in create_id1:
                create_id = row[0]
            if b == 1:
                self.cursor.execute('SELECT `last_promo` FROM `users` WHERE `user_id`=%s',(user_id))
                result = self.cursor.fetchall()
                i = '0'
                for row in result:
                    i = row[0]
                self.cursor.execute('SELECT now()')
                time = self.cursor.fetchall()
                a = '0'
                for row in time:
                    a = row[0]
                self.cursor.execute('SELECT `set_promo_money` FROM `admin_set`')
                money_withdraw1 = self.cursor.fetchall()
                money_withdraw = '0'
                for row in money_withdraw1:
                    money_withdraw = int(row[0])
                
                if bool(i) == False:


                    self.cursor.execute('SELECT `user_id` FROM `users` WHERE `user_id`=%s',(user_id))
                    result1 = self.cursor.fetchall()
                    result1_row = '0'
                    for row in result1:
                        result1_row = row[0]
                    self.cursor.execute('SELECT `crt_usr_id` FROM `promo` WHERE `crt_usr_id`=%s',(create_id))
                    result2 = self.cursor.fetchall()
                    result2_row = '0'
                    for row in result2:
                        result2_row = row[0]
                        
                    if result1_row != result2_row:

                        self.cursor.execute('SELECT `sum` FROM `promo` WHERE `name_promo`=%s', (promo_name))
                        result = self.cursor.fetchall()
                        a = '0'
                        for row in result:
                            a = row[0]
                        self.cursor.execute('UPDATE `users` SET `balance`=balance+%s, `last_promo`=(now() + INTERVAL 1 hour) WHERE `user_id`=%s',(a, user_id))
                        self.cursor.execute('UPDATE `users` SET `balance`=balance+0.5 WHERE `user_id`=%s',(money_withdraw, create_id))
                        self.cursor.execute('UPDATE `promo` SET `valid`=0 WHERE `name_promo`=%s',(promo_name))
                        self.connection.commit()


                        return a
                    elif result1_row == result2_row:
                        return 'usernot'
                elif bool(i) == True:
                    c = i<a
                    if c == False:
                        return 'time not end'
                    if c == True:
                        self.cursor.execute('SELECT `user_id` FROM `users` WHERE `user_id`=%s',(user_id))
                        result1 = self.cursor.fetchall()
                        result1_row = '0'
                        for row in result1:
                            result1_row = row[0]
                        self.cursor.execute('SELECT `crt_usr_id` FROM `promo` WHERE `crt_usr_id`=%s',(create_id,))
                        result2 = self.cursor.fetchall()
                        result2_row = '0'
                        for row in result2:
                            result2_row = row[0]
                                
                                
                        if result1_row != result2_row:

                            self.cursor.execute('SELECT `sum` FROM `promo` WHERE `name_promo`=%s', (promo_name))
                            result = self.cursor.fetchall()
                            a = '0'
                            for row in result:
                                a = row[0]
                            self.cursor.execute('UPDATE `users` SET `balance`=balance+%s, `last_promo`=(now() + INTERVAL 1 hour) WHERE `user_id`=%s',(a, user_id))
                            self.cursor.execute('UPDATE `users` SET `balance`=balance+0.5 WHERE `user_id`=%s',(money_withdraw, create_id))
                            self.cursor.execute('UPDATE `promo` SET `valid`=0 WHERE `name_promo`=%s',(promo_name))
                            self.connection.commit()
                            return a
                        elif result1_row == result2_row:
                            return 'usernot'
            

            elif b == 0:
                
                self.cursor.execute('UPDATE `users` SET `balance`=balance+0.5 WHERE `user_id`=%s',(money_withdraw, create_id))
                self.connection.commit()
                return 'not valid'

    def check_crt_promo(self, promo_name):
            self.cursor.execute('SELECT `crt_usr_id` FROM `promo` WHERE `name_promo`=%s', (promo_name))
            result = self.cursor.fetchall()
            for row in result:
                return row[0]
    
    def btc_add(self, btc_value, user_id):
        self.cursor.execute('SELECT `btc_course` FROM `users` WHERE `user_id`=%s', (user_id))
        check = self.cursor.fetchall()
        check_result = '0'
        for row in check:
            check_result = row[0]

        self.cursor.execute('SELECT `date_next` FROM `btc_time` WHERE `date_next` > (now()+interval 3 hour)')
        times = self.cursor.fetchall()
        if len(times) == 1:
                
                
            if check_result == 0.0:
                self.cursor.execute('UPDATE `users` SET `btc_course`=%s WHERE `user_id`=%s', (btc_value, user_id))
                result = self.cursor.fetchall()
                res = '0'
                for row in result:
                    res = row[0]
                self.connection.commit()
                return res
            elif check_result != 0.0:
                print(check)
                print(check_result)
                return 'no'
        elif len(times) == 0:
            return 'nottime'
    
    def btc_course(self):
        self.cursor.execute('SELECT `btc_course` FROM `users`')
        result = self.cursor.fetchall()
        return result

    def check_win_btc(self, btc_value):
        self.cursor.execute('SELECT `user_id` FROM `users` WHERE `btc_course`=%s',(btc_value))
        result = self.cursor.fetchall()
        result_row = 0
        for row in result:
            result_row = row[0]
        self.cursor.execute('UPDATE `users` SET `btc_course`=0')
        self.connection.commit()
        return int(result_row)

    def add_btc_win(self, user_id):
            self.cursor.execute('SELECT `set_btc_win3` FROM `admin_set`')
            result = self.cursor.fetchall()
            result_row = 0
            for row in result:
                result_row = row[0]
            self.cursor.execute('UPDATE `users` SET `balance`=balance+%s WHERE `user_id`=%s', (result_row, user_id))
            self.connection.commit()
            return str(result_row)

    def check_len_room(self, room):
            if room == '1':
                self.cursor.execute('SELECT `user_id` FROM `room_1`')
                result = self.cursor.fetchall()
                if len(result) == None:
                    return '0'
                elif len(result) != None:
                    return str(len(result))
            elif room == '2':
                self.cursor.execute('SELECT `user_id` FROM `room_2`')
                result = self.cursor.fetchall()
                if len(result) == None:
                    return '0'
                elif len(result) != None:
                    return len(result)
            elif room == '3':
                self.cursor.execute('SELECT `user_id` FROM `room_3`')
                result = self.cursor.fetchall()
                if len(result) == None:
                    return '0'
                elif len(result) != None:
                    return len(result)
            elif room == '4':
                self.cursor.execute('SELECT `user_id` FROM `room_4`')
                result = self.cursor.fetchall()
                if len(result) == None:
                    return '0'
                elif len(result) != None:
                    return len(result)
            elif room == '5':
                self.cursor.execute('SELECT `user_id` FROM `room_5`')
                result = self.cursor.fetchall()
                if len(result) == None:
                    return '0'
                elif len(result) != None:
                    return len(result)
            elif room == '6':
                self.cursor.execute('SELECT `user_id` FROM `room_6`')
                result = self.cursor.fetchall()
                if len(result) == None:
                    return '0'
                elif len(result) != None:
                    return len(result)
    

    def add_to_room(self, room, user_id):
        if room == '1':
            self.cursor.execute('SELECT `balance` FROM `users` WHERE `user_id`=%s', (user_id))
            balance = self.cursor.fetchall()
            balance_row = '0'
            for row in balance:
               balance_row = float(row[0])
            if balance_row >= 1.0:
                self.cursor.execute('SELECT `user_id` FROM `room_1`')
                result = self.cursor.fetchall()
                if len(result) == 0 or len(result) != 5:
                    self.cursor.execute('SELECT `user_id` FROM `room_1` WHERE `user_id`=%s', (user_id))
                    result1 = self.cursor.fetchall()
                    if len(result1) == 0:
                        self.cursor.execute('INSERT INTO `room_1` (user_id, time_exit) VALUES (%s, (now()+INTERVAL 3 hour))', (user_id))
                        self.cursor.execute('SELECT `user_id` FROM `room_1`')
                        result2 = self.cursor.fetchall()
                        if len(result2) != 2:
                            self.cursor.execute('UPDATE `users` SET `balance`=balance-1 WHERE `user_id`=%s', (user_id))
                            self.connection.commit()
                            return 'ok'
                        elif len(result2) == 2:
                            self.connection.commit()
                            return 'go'
                    elif len(result1) != 0:
                        print(len(result1))
                        return 'no'
                elif len(result) == 5:
                    self.connection.commit()
                    return 'go'
            elif balance_row < 1.0:
               return 'no_bal'
                
        elif room == '2':
            self.cursor.execute('SELECT `balance` FROM `users` WHERE `user_id`=%s', (user_id))
            balance = self.cursor.fetchall()
            balance_row = '0'
            for row in balance:
                balance_row = float(row[0])
            if balance_row >= 3.0:
                self.cursor.execute('SELECT `user_id` FROM `room_2`')
                result = self.cursor.fetchall()
                if len(result) == 0 or len(result) != 5:
                    self.cursor.execute('SELECT `user_id` FROM `room_2` WHERE `user_id`=%s', (user_id))
                    result1 = self.cursor.fetchall()
                    if len(result1) == 0:
                        self.cursor.execute('INSERT INTO `room_2` (user_id, time_exit) VALUES (%s, (now()+INTERVAL 3 hour))', (user_id))
                        self.cursor.execute('SELECT `user_id` FROM `room_2`')
                        result2 = self.cursor.fetchall()
                        if len(result2) != 2:
                            self.cursor.execute('UPDATE `users` SET `balance`=balance-3 WHERE `user_id`=%s', (user_id))
                            self.connection.commit()
                            return 'ok'
                        elif len(result2) == 2:
                            self.connection.commit()
                            return 'go'
                    elif len(result1) != 0:
                        print(len(result1))
                        return 'no'
                elif len(result) == 5:
                    return 'go'
            elif balance_row < 3.0:
                return 'no_bal'
                
        elif room == '3':
            self.cursor.execute('SELECT `balance` FROM `users` WHERE `user_id`=%s', (user_id))
            balance = self.cursor.fetchall()
            balance_row = '0'
            for row in balance:
                balance_row = float(row[0])
            if balance_row >= 10.0:
                self.cursor.execute('SELECT `user_id` FROM `room_3`')
                result = self.cursor.fetchall()
                if len(result) == 0 or len(result) != 5:
                    self.cursor.execute('SELECT `user_id` FROM `room_3` WHERE `user_id`=%s', (user_id))
                    result1 = self.cursor.fetchall()
                    if len(result1) == 0:
                        self.cursor.execute('INSERT INTO `room_3` (user_id, time_exit) VALUES (%s, (now()+INTERVAL 3 hour))', (user_id))
                        self.cursor.execute('SELECT `user_id` FROM `room_3`')
                        result2 = self.cursor.fetchall()
                        if len(result2) != 2:
                            self.cursor.execute('UPDATE `users` SET `balance`=balance-10 WHERE `user_id`=%s', (user_id))
                            self.connection.commit()
                            return 'ok'
                        elif len(result2) == 2:
                            self.connection.commit()
                            return 'go'
                    elif len(result1) != 0:
                        print(len(result1))
                        return 'no'
                elif len(result) == 5:
                    return 'go'
            elif balance_row < 10.0:
                return 'no_bal'

        elif room == '4':
            self.cursor.execute('SELECT `balance` FROM `users` WHERE `user_id`=%s', (user_id))
            balance = self.cursor.fetchall()
            balance_row = '0'
            for row in balance:
                balance_row = float(row[0])
            if balance_row >= 30.0:
                self.cursor.execute('SELECT `user_id` FROM `room_4`')
                result = self.cursor.fetchall()
                if len(result) == 0 or len(result) != 5:
                    self.cursor.execute('SELECT `user_id` FROM `room_4` WHERE `user_id`=%s', (user_id))
                    result1 = self.cursor.fetchall()
                    if len(result1) == 0:
                        self.cursor.execute('INSERT INTO `room_4` (user_id, time_exit) VALUES (%s, (now()+INTERVAL 3 hour))', (user_id))
                        self.cursor.execute('SELECT `user_id` FROM `room_4`')
                        result2 = self.cursor.fetchall()
                        if len(result2) != 2:
                            self.cursor.execute('UPDATE `users` SET `balance`=balance-30 WHERE `user_id`=%s', (user_id))
                            self.connection.commit()
                            return 'ok'
                        elif len(result2) == 2:
                            self.connection.commit()
                            return 'go'
                    elif len(result1) != 0:
                        print(len(result1))
                        return 'no'
                elif len(result) == 5:
                    return 'go'
            elif balance_row < 30.0:
                return 'no_bal'
                
        elif room == '5':
            self.cursor.execute('SELECT `balance` FROM `users` WHERE `user_id`=%s', (user_id))
            balance = self.cursor.fetchall()
            balance_row = '0'
            for row in balance:
                balance_row = int(row[0])
            if balance_row >= 100:
                self.cursor.execute('SELECT `user_id` FROM `room_5`')
                result = self.cursor.fetchall()
                if len(result) == 0 or len(result) != 5:
                    self.cursor.execute('SELECT `user_id` FROM `room_5` WHERE `user_id`=%s', (user_id))
                    result1 = self.cursor.fetchall()
                    if len(result1) == 0:
                        self.cursor.execute('INSERT INTO `room_5` (user_id, time_exit) VALUES (%s, (now()+INTERVAL 3 hour))', (user_id))
                        self.cursor.execute('SELECT `user_id` FROM `room_5`')
                        result2 = self.cursor.fetchall()
                        if len(result2) != 5:
                            self.cursor.execute('UPDATE `users` SET `balance`=balance-100 WHERE `user_id`=%s', (user_id))
                            self.connection.commit()
                            return 'ok'
                        elif len(result2) == 5:
                            self.connection.commit()
                            return 'go'
                    elif len(result1) != 0:
                        print(len(result1))
                        return 'no'
                elif len(result) == 5:
                    return 'go'
            elif balance_row < 100:
                return 'no_bal'
                
        elif room == '6':
            self.cursor.execute('SELECT `balance` FROM `users` WHERE `user_id`=%s', (user_id))
            balance = self.cursor.fetchall()
            balance_row = '0'
            for row in balance:
                balance_row = int(row[0])
            if balance_row >= 300:
                self.cursor.execute('SELECT `user_id` FROM `room_6`')
                result = self.cursor.fetchall()
                print(len(result))
                if len(result) == 5 or len(result) != 5:
                    self.cursor.execute('SELECT `user_id` FROM `room_6` WHERE `user_id`=%s', (user_id))
                    result1 = self.cursor.fetchall()
                    if len(result1) == 0:
                        self.cursor.execute('INSERT INTO `room_6` (user_id, time_exit) VALUES (%s, (now()+INTERVAL 3 hour))', (user_id))
                        self.cursor.execute('SELECT `user_id` FROM `room_6`')
                        result2 = self.cursor.fetchall()
                        if len(result2) != 5:
                            self.cursor.execute('UPDATE `users` SET `balance`=balance-300 WHERE `user_id`=%s', (user_id))
                            self.connection.commit()
                            return 'ok'
                        elif len(result2) == 5:
                            self.connection.commit()
                            return 'go'
                    elif len(result1) != 0:
                        print(len(result1))
                        return 'no'
                elif len(result) == 5:
                    return 'go'
            elif balance_row < 300:
                return 'no_bal'

    def exit_room(self, room, user_id):
        if room == '1':

            self.cursor.execute('SELECT `user_id` FROM `room_1` WHERE `time_exit` <= now() AND `user_id`=%s', (user_id))
            lens = self.cursor.fetchall()
            print(len(lens))
            if len(lens) == 1:



                self.cursor.execute('DELETE FROM `room_1` WHERE `user_id`=%s',(user_id))        
                self.cursor.execute('SELECT `user_id` FROM `room_1` WHERE `user_id`=%s',(user_id))
                result = self.cursor.fetchall()
                
                if len(result) == 0:
                    print(len(result))
                    self.cursor.execute('UPDATE `users` SET `balance`=balance+1 WHERE `user_id`=%s', (user_id))
                    self.connection.commit()
                    return 'ok'
                elif len(result) != 0:
                    print(len(result))
                    self.connection.commit()
                    return 'no'
            elif len(lens) == 0:
                return 'nottime'

        elif room == '2':
            self.cursor.execute('SELECT `user_id` FROM `room_2` WHERE `time_exit` <= now() AND `user_id`=%s', (user_id))
            lens = self.cursor.fetchall()
            if len(lens) == 1:

            
                self.cursor.execute('DELETE FROM `room_2` WHERE `user_id`=%s',(user_id))
                self.cursor.execute('SELECT `user_id` FROM `room_2` WHERE `user_id`=%s',(user_id))
                self.connection.commit()

                if len(result) == 0:
                    self.cursor.execute('UPDATE `users` SET `balance`=balance+3 WHERE `user_id`=%s', (user_id))
                    self.connection.commit()
                    return 'ok'
                elif len(result) != 0:
                    self.connection.commit()
                    return 'no'
            elif len(lens) == 0:
                return 'nottime'
                
        elif room == '3':
            self.cursor.execute('SELECT `user_id` FROM `room_3` WHERE `time_exit` <= now() AND `user_id`=%s', (user_id))
            lens = self.cursor.fetchall()
            if len(lens) == 1:
            
                    
                self.cursor.execute('DELETE FROM `room_3` WHERE `user_id`=%s',(user_id))
                self.cursor.execute('SELECT `user_id` FROM `room_3` WHERE `user_id`=%s',(user_id))
                result = self.cursor.fetchall()
                
                if len(result) == 0:
                    self.cursor.execute('UPDATE `users` SET `balance`=balance+10 WHERE `user_id`=%s', (user_id))
                    self.connection.commit()
                    return 'ok'
                elif len(result) != 0:
                    self.connection.commit()
                    return 'no'
            elif len(lens) == 0:
                return 'nottime'
                
        elif room == '4':
            self.cursor.execute('SELECT `user_id` FROM `room_4` WHERE `time_exit` <= now() AND `user_id`=%s', (user_id))
            lens = self.cursor.fetchall()
            if len(lens) == 1:


                    
                self.cursor.execute('DELETE FROM `room_4` WHERE `user_id`=?',(user_id,))        
                self.cursor.execute('SELECT `user_id` FROM `room_4` WHERE `user_id`=%s',(user_id))
                result = self.cursor.fetchall()
                
                if len(result) == 0:
                    self.cursor.execute('UPDATE `users` SET `balance`=balance+30 WHERE `user_id`=%s', (user_id))
                    self.connection.commit()
                    return 'ok'
                elif len(result) != 0:
                    self.connection.commit()
                    return 'no'

            elif len(lens) == 0:
                return 'nottime'

        elif room == '5':
                    
            self.cursor.execute('DELETE FROM `room_5` WHERE `user_id`=%s',(user_id))        
            self.cursor.execute('SELECT `user_id` FROM `room_5` WHERE `user_id`=%s',(user_id))
            result = self.cursor.fetchall()
            if len(result) == 0:
                self.cursor.execute('UPDATE `users` SET `balance`=balance+100 WHERE `user_id`=%s', (user_id))
                self.connection.commit()
                return 'ok'
            elif len(result) != 0:
                return 'no'
                
        elif room == '6':
                    
            self.cursor.execute('DELETE FROM `room_6` WHERE `user_id`=%s',(user_id))        
            self.cursor.execute('SELECT `user_id` FROM `room_6` WHERE `user_id`=?',(user_id))
            result = self.cursor.fetchall()
            if len(result) == 0:
                self.cursor.execute('UPDATE `users` SET `balance`=balance+300 WHERE `user_id`=%s', (user_id))
                self.connection.commit()
                return 'ok'
            elif len(result) != 0:
                self.connection.commit()
                return 'no'

    def list_players(self, room):
        if room == '1':
            self.cursor.execute('SELECT `user_id` FROM `room_1`')
            result = self.cursor.fetchall()
            return result
        elif room == '2':
            self.cursor.execute('SELECT `user_id` FROM `room_2`')
            result = self.cursor.fetchall()
            return result
        elif room == '3':
            self.cursor.execute('SELECT `user_id` FROM `room_3`')
            result = self.cursor.fetchall()
            return result
        elif room == '4':
            self.cursor.execute('SELECT `user_id` FROM `room_4`')
            result = self.cursor.fetchall()
            return result
        elif room == '5':
            self.cursor.execute('SELECT `user_id` FROM `room_5`')
            result = self.cursor.fetchall()
            return result
        elif room == '6':
            self.cursor.execute('SELECT `user_id` FROM `room_6`')
            result = self.cursor.fetchall()
            return result

    def del_room(self, step):
        if step == '1':
            self.cursor.execute('DELETE FROM `room_1`')
            self.connection.commit()
            return
        elif step == '2':
            self.cursor.execute('DELETE FROM `room_2`')
            self.connection.commit()
            return
        elif step == '3':
            self.cursor.execute('DELETE FROM `room_3`')
            self.connection.commit()
            return
        elif step == '4':
            self.cursor.execute('DELETE FROM `room_4`')
            self.connection.commit()
            return



    def check_lose(self, user_id, room):
        if room == '1':
            self.cursor.execute('SELECT `user_id` FROM `room_1` WHERE `user_id` NOT IN (%s)', (user_id))
            result = self.cursor.fetchall()
            return result
        elif room == '2':
            self.cursor.execute('SELECT `user_id` FROM `room_2` WHERE `user_id` NOT IN (%s)', (user_id))
            result = self.cursor.fetchall()
            return result
        elif room == '3':
            self.cursor.execute('SELECT `user_id` FROM `room_3` WHERE `user_id` NOT IN (%s)', (user_id))
            result = self.cursor.fetchall()
            return result
        elif room == '4':
            self.cursor.execute('SELECT `user_id` FROM `room_4` WHERE `user_id` NOT IN (%s)', (user_id))
            result = self.cursor.fetchall()
            return result
        elif room == '5':
            self.cursor.execute('SELECT `user_id` FROM `room_5` WHERE `user_id` NOT IN (%s)', (user_id))
            result = self.cursor.fetchall()
            return result
        elif room == '6':
            self.cursor.execute('SELECT `user_id` FROM `room_6` WHERE `user_id` NOT IN (%s)', (user_id))
            result = self.cursor.fetchall()
            return result



    def win_room(self, room, user_id):
        if room == '1':
            self.cursor.execute('SELECT `ticket_many` FROM `set_tickets_win` WHERE `room`=1')
            result = self.cursor.fetchall()
            result_row = 0
            for row in result:
                result_row = row[0]


            self.cursor.execute('UPDATE `users` SET `balance`=balance+4.5, `tickets`=tickets+%s WHERE `user_id`=%s',(result_row, user_id))
            self.cursor.execute('UPDATE `jackpot` SET `jackpot_sum`=jackpot_sum+0.25')
            self.connection.commit()
            return
        elif room == '2':
            self.cursor.execute('SELECT `ticket_many` FROM `set_tickets_win` WHERE `room`=2')
            result = self.cursor.fetchall()
            result_row = 0
            for row in result:
                result_row = row[0]



            self.cursor.execute('UPDATE `users` SET `balance`=balance+13.5, `tickets`=tickets+%s WHERE `user_id`=%s',(result_row, user_id))
            self.cursor.execute('UPDATE `jackpot` SET `jackpot_sum`=jackpot_sum+0.75')
            self.connection.commit()
            return
        elif room == '3':
            self.cursor.execute('SELECT `ticket_many` FROM `set_tickets_win` WHERE `room`=3')
            result = self.cursor.fetchall()
            result_row = 0
            for row in result:
                result_row = row[0]



            self.cursor.execute('UPDATE `users` SET `balance`=balance+45, `tickets`=tickets+%s WHERE `user_id`=%s',(result_row, user_id))
            self.cursor.execute('UPDATE `jackpot` SET `jackpot_sum`=jackpot_sum+2.5')
            self.connection.commit()
            return
        elif room == '4':
            self.cursor.execute('SELECT `ticket_many` FROM `set_tickets_win` WHERE `room`=4')
            result = self.cursor.fetchall()
            result_row = 0
            for row in result:
                result_row = row[0]



            self.cursor.execute('UPDATE `users` SET `balance`=balance+135, `tickets`=tickets+%s WHERE `user_id`=%s',(result_row, user_id))
            self.cursor.execute('UPDATE `jackpot` SET `jackpot_sum`=jackpot_sum+7.5')
            self.connection.commit()
            return
        elif room == '5':
            self.cursor.execute('SELECT `ticket_many` FROM `set_tickets_win` WHERE `room`=5')
            result = self.cursor.fetchall()
            result_row = 0
            for row in result:
                result_row = row[0]



            self.cursor.execute('UPDATE `users` SET `balance`=balance+450, `tickets`=tickets+%s WHERE `user_id`=%s',(result_row, user_id))
            self.cursor.execute('UPDATE `jackpot` SET `jackpot_sum`=jackpot_sum+25')
            self.connection.commit()
        elif room == '6':
            self.cursor.execute('SELECT `ticket_many` FROM `set_tickets_win` WHERE `room`=6')
            result = self.cursor.fetchall()
            result_row = 0
            for row in result:
                result_row = row[0]



            self.cursor.execute('UPDATE `users` SET `balance`=balance+1350 WHERE, `tickets`=tickets+%s WHERE `user_id`=%s',(result_row, user_id))
            self.cursor.execute('UPDATE `jackpot` SET `jackpot_sum`=jackpot_sum+75')
            self.connection.commit()
            return


    def room_quant(self, user_id):
        self.cursor.execute('UPDATE `users` SET `room_game_quant`=room_game_quant+1 WHERE `user_id`=%s', (user_id))
        self.connection.commit()
        return

    def select_jack_quant(self):
        self.cursor.execute('SELECT `room_game_quant` FROM `users`')
        result = self.cursor.fetchall()
        return result


    def jack_win(self, quant):
        self.cursor.execute('SELECT `user_id` FROM `users` WHERE `room_game_quant`=%s', (quant))
        result = self.cursor.fetchall()
        result_row = '0'
        for row in result:
            result_row = row[0]

        self.cursor.execute('SELECT `jackpot_sum` FROM `jackpot`')
        result1 = self.cursor.fetchall()
        result1_row = '0'
        for row in result1:
            result1_row = row[0]
        self.cursor.execute('UPDATE `users` SET `balance`=balance+%s WHERE `user_id`=%s', (result1_row, result_row))
        self.cursor.execute('UPDATE `jackpot` SET `jackpot_sum`=0')
        self.connection.commit()
        return


    def select_user_jack(self, quant):
        self.cursor.execute('SELECT `user_id` FROM `users` WHERE `room_game_quant`=%s', (quant))
        result = self.cursor.fetchall()
        self.cursor.execute('UPDATE `users` SET `room_game_quant`=0')
        for row in result:
            self.connection.commit()
            return row[0]

    def set_min_checks(self, summ):
        self.cursor.execute('UPDATE `admin_set` SET `set_min_check`=%s', (summ))
        self.connection.commit()
        return

    def set_max_checks(self, summ):
        self.cursor.execute('UPDATE `admin_set` SET `set_max_check`=%s', (summ))
        self.connection.commit()
        return

    def set_rew_checks(self, summ):
        self.cursor.execute('UPDATE `admin_set` SET `set_check_money`=%s', (summ))
        self.connection.commit()
        return

    def set_min_promos(self, summ):
        self.cursor.execute('UPDATE `admin_set` SET `set_min_promo`=%s', (summ))
        self.connection.commit()
        return

    def set_max_promos(self, summ):
        self.cursor.execute('UPDATE `admin_set` SET `set_max_promo`=%s', (summ))
        self.connection.commit()
        return

    def set_rew_promos(self, summ):
        self.cursor.execute('UPDATE `admin_set` SET `set_promo_money`=%s', (summ))
        self.connection.commit()
        return

    def set_rew_btcs(self, step, summ):
        if step == '1':
            self.cursor.execute('UPDATE `admin_set` SET `set_btc_win1`=%s', (summ))
            self.connection.commit()
            return
        elif step == '2':
            self.cursor.execute('UPDATE `admin_set` SET `set_btc_win2`=%s', (summ))
            self.connection.commit()
            return
        elif step == '3':
            self.cursor.execute('UPDATE `admin_set` SET `set_btc_win3`=%s', (summ))
            self.connection.commit()
            return

    def check_btc(self, step):
        if step == '1':
            self.cursor.execute('SELECT `set_btc_win1` FROM `admin_set`')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]
        elif step == '2':
            self.cursor.execute('SELECT `set_btc_win2` FROM `admin_set`')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]
        elif step == '3':
            self.cursor.execute('SELECT `set_btc_win3` FROM `admin_set`')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]



    def set_time_promos(self, summ):
        self.cursor.execute('UPDATE `admin_set` SET `set_promo_hours`=%s', (summ))
        self.connection.commit()
        return


    def check_qiwi_num(self, user_id):
        self.cursor.execute('SELECT `qiwi` FROM `users` WHERE `user_id`=%s', (user_id))
        result = self.cursor.fetchall()
        result_row = '0'
        for row in result:
            result_row = row[0]
        if result_row == '0':
            return 'not qiwi'
        elif result_row != '0':
            return result_row

    def set_qiwi(self, user_id, qiwi):
        self.cursor.execute('UPDATE `users` SET `qiwi`=%s WHERE `user_id`=%s', (qiwi, user_id))
        self.connection.commit()
        return


    def dep_operation(self, user_id, amount):

        self.cursor.execute('DELETE FROM `dep_operations` WHERE `time_create` < (now() - INTERVAL 10 minute) AND `user_id`=%s AND `result`!="success"', (user_id))

        self.cursor.execute('INSERT INTO `dep_operations` (`user_id`, `amount`, `comment`, `result`, `time_create`) VALUES (%s, %s, %s, "waiting", now())', (user_id, amount, user_id))
        self.connection.commit()
        return


    def ins_dep(self, user_id, amount, transaction):
        self.cursor.execute('SELECT `transaction` FROM `dep_operations` WHERE `user_id`=%s AND `amount`=%s AND `transaction` IS NULL', (user_id, amount))
        result = self.cursor.fetchall()
        result_row = '0'
        for row in result:
            result_row = row[0]
            
        if result_row == None:


            self.cursor.execute('UPDATE `users` SET `balance`=balance+%s WHERE `user_id`=%s', (amount, user_id))
            self.connection.commit()
            self.cursor.execute('UPDATE `dep_operations` SET `transaction`=%s, `result`="success" WHERE `transaction` IS NULL AND `result`="waiting" AND `user_id`=%s LIMIT 1', (transaction, user_id))
            self.connection.commit()
            self.cursor.execute('DELETE FROM `dep_operations` WHERE `result`="waiting" AND `user_id`=%s',(user_id))
            self.connection.commit()

            self.cursor.execute('SELECT max(`ticket_sum`) FROM `admin_ticket_set` WHERE `ticket_sum` <=%s', (amount))
            summ = self.cursor.fetchall()
            summ_res = 0
            for row in summ:
                summ_res = row[0]
            if summ_res == None:
                return
            elif summ_res != None:
                self.cursor.execute('SELECT `ticket_many` FROM `admin_ticket_set` WHERE `ticket_sum`=%s', (summ_res))
                ticket_many = self.cursor.fetchall()
                ticket = 0
                for row in ticket_many:
                    ticket = row[0]
                self.cursor.execute('UPDATE `users` SET `tickets`=tickets+%s WHERE `user_id`=%s', (ticket, user_id))
                self.connection.commit()

                return 'success'
        elif result_row != None:
            return

    def with_operaion(self, user_id, amount, qiwi):
        self.cursor.execute('INSERT INTO `withdraw_operations` (`user_id`, `amount`, `qiwi_num`, `date_crt`, `result`) VALUES (%s, %s, %s, now(), "waiting")', (user_id, amount, qiwi))
        self.connection.commit()
        self.cursor.execute('UPDATE `users` SET `balance`=balance-%s WHERE `user_id`=%s', (amount, user_id))
        self.connection.commit()
        self.cursor.execute('SELECT `id` FROM `withdraw_operations` WHERE `date_crt` = (SELECT MAX(`date_crt`) FROM `withdraw_operations` WHERE `user_id`=%s) ', (user_id))
        result = self.cursor.fetchall()
        result_row = '0'
        for row in result:
            result_row = row[0]
        return result_row

    def time_now(self):
        self.cursor.execute('SELECT now()')
        result = self.cursor.fetchall()
        for row in result:
            return row[0]


    def with_accept(self, id):
        self.cursor.execute('UPDATE `withdraw_operations` SET `result`="success" WHERE `id`=%s', (id))
        self.connection.commit()
        self.cursor.execute('SELECT `user_id` FROM `withdraw_operations` WHERE `id`=%s', (id))
        result = self.cursor.fetchall()
        for row in result:
            return row[0]
    
    def with_decline(self, id):
        self.cursor.execute('UPDATE `withdraw_operations` SET `result`="decline" WHERE `id`=%s', (id))
        self.connection.commit()
        self.cursor.execute('SELECT `user_id`, `amount` FROM `withdraw_operations` WHERE `id`=%s', (id))
        result = self.cursor.fetchall()
        result_user_id = '0'
        result_amount = '0'
        for row in result:
            result_user_id = row[0]
            result_amount = row[1]
        
        self.cursor.execute('UPDATE `users` SET `balance`=balance+%s WHERE `user_id`=%s', (result_amount, result_user_id))
        self.connection.commit()
        return result_user_id
            


    def check_payeer_num(self, user_id):
        self.cursor.execute('SELECT `payeer` FROM `users` WHERE `user_id`=%s', (user_id))
        result = self.cursor.fetchall()
        result_row = '0'
        for row in result:
            result_row = row[0]
        if result_row == '0':
            return 'not payeer'
        elif result_row != '0':
            return result_row
    

    def payeer_set(self, user_id, number):
        self.cursor.execute('UPDATE `users` SET `payeer`=%s WHERE `user_id`=%s', (number, user_id))
        self.connection.commit()
        return

    def balance_add(self, user_id, amount):
        self.cursor.execute('UPDATE `users` SET `balance`=balance+%s WHERE `user_id`=%s', (amount, user_id))
        self.connection.commit()
        return

    def balance_with(self, user_id, amount):
        self.cursor.execute('UPDATE `users` SET `balance`=balance-%s WHERE `user_id`=%s', (amount, user_id))
        self.connection.commit()
        return

    def ticket_set_check(self, num_ticket):
        if num_ticket == '1':
            self.cursor.execute('SELECT `ticket_many` FROM `admin_ticket_set` WHERE `id`=1')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]
        elif num_ticket == '2':
            self.cursor.execute('SELECT `ticket_many` FROM `admin_ticket_set` WHERE `id`=2')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]
        elif num_ticket == '3':
            self.cursor.execute('SELECT `ticket_many` FROM `admin_ticket_set` WHERE `id`=3')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]
        elif num_ticket == '4':
            self.cursor.execute('SELECT `ticket_many` FROM `admin_ticket_set` WHERE `id`=4')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]
        elif num_ticket == '5':
            self.cursor.execute('SELECT `ticket_many` FROM `admin_ticket_set` WHERE `id`=5')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]
        elif num_ticket == '6':
            self.cursor.execute('SELECT `ticket_many` FROM `admin_ticket_set` WHERE `id`=6')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]
        elif num_ticket == '7':
            self.cursor.execute('SELECT `ticket_many` FROM `admin_ticket_set` WHERE `id`=7')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]
    
    def ticket_sum_check(self, num_ticket):
        if num_ticket == '1':
            self.cursor.execute('SELECT `ticket_sum` FROM `admin_ticket_set` WHERE `id`=1')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]
        elif num_ticket == '2':
            self.cursor.execute('SELECT `ticket_sum` FROM `admin_ticket_set` WHERE `id`=2')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]
        elif num_ticket == '3':
            self.cursor.execute('SELECT `ticket_sum` FROM `admin_ticket_set` WHERE `id`=3')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]
        elif num_ticket == '4':
            self.cursor.execute('SELECT `ticket_sum` FROM `admin_ticket_set` WHERE `id`=4')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]
        elif num_ticket == '5':
            self.cursor.execute('SELECT `ticket_sum` FROM `admin_ticket_set` WHERE `id`=5')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]
        elif num_ticket == '6':
            self.cursor.execute('SELECT `ticket_sum` FROM `admin_ticket_set` WHERE `id`=6')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]
        elif num_ticket == '7':
            self.cursor.execute('SELECT `ticket_sum` FROM `admin_ticket_set` WHERE `id`=7')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]

    def check_ticket(self, user_id):
        self.cursor.execute('SELECT `tickets` FROM `users` WHERE `user_id`=%s', (user_id))
        result = self.cursor.fetchall()
        for row in result:
            return row[0]


    def ticket_win(self):
        self.cursor.execute('SELECT `top_tickets` FROM `admin_set`')
        result = self.cursor.fetchall()
        result_row = 0
        
        for row in result:
            result_row = int(row[0])
        self.cursor.execute('SELECT `user_id` FROM `users` ORDER BY `tickets` DESC limit %s', (result_row))
        result1 = self.cursor.fetchall()
        return result1

    def check_top_ticket(self):
        self.cursor.execute('SELECT `top_tickets` FROM `admin_set`')
        result = self.cursor.fetchall()
        for row in result:
            return row[0]
        

    def add_balance_ticket(self, user_id, step):
        if step == '1':
            self.cursor.execute('SELECT `win_1` FROM `admin_set`')
            result = self.cursor.fetchall()
            result_row = 0
            for row in result:
                result_row = row[0]
            self.cursor.execute('UPDATE `users` SET `balance`=balance+%s WHERE `user_id`=%s', (result_row, user_id))
            self.connection.commit()
            return
        elif step == '2':
            self.cursor.execute('SELECT `win_2` FROM `admin_set`')
            result = self.cursor.fetchall()
            result_row = 0
            for row in result:
                result_row = row[0]
            self.cursor.execute('UPDATE `users` SET `balance`=balance+%s WHERE `user_id`=%s', (result_row, user_id))
            self.connection.commit()
            return
        elif step == '3':
            self.cursor.execute('SELECT `win_3` FROM `admin_set`')
            result = self.cursor.fetchall()
            result_row = 0
            for row in result:
                result_row = row[0]
            self.cursor.execute('UPDATE `users` SET `balance`=balance+%s WHERE `user_id`=%s', (result_row, user_id))
            self.connection.commit()
            return
        elif step == '4':
            self.cursor.execute('SELECT `win_4` FROM `admin_set`')
            result = self.cursor.fetchall()
            result_row = 0
            for row in result:
                result_row = row[0]
            self.cursor.execute('UPDATE `users` SET `balance`=balance+%s WHERE `user_id`=%s', (result_row, user_id))
            self.connection.commit()
            return
        elif step == '5':
            self.cursor.execute('SELECT `win_5` FROM `admin_set`')
            result = self.cursor.fetchall()
            result_row = 0
            for row in result:
                result_row = row[0]
            self.cursor.execute('UPDATE `users` SET `balance`=balance+%s WHERE `user_id`=%s', (result_row, user_id))
            self.connection.commit()
            return
        
    def zero_tickets(self):
        self.cursor.execute('UPDATE `users` SET `tickets`=0')
        self.connection.commit()
        return
    

    def check_win_ticket(self, step):
        if step == '1':
            self.cursor.execute('SELECT `win_1` FROM `admin_set`')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]
        elif step == '2':
            self.cursor.execute('SELECT `win_2` FROM `admin_set`')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]
        elif step == '3':
            self.cursor.execute('SELECT `win_3` FROM `admin_set`')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]
        elif step == '4':
            self.cursor.execute('SELECT `win_4` FROM `admin_set`')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]
        elif step == '5':
            self.cursor.execute('SELECT `win_5` FROM `admin_set`')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]

    def change_top_tickets(self, amount):
        self.cursor.execute('UPDATE `admin_set` SET `top_tickets`=%s', (amount))
        self.connection.commit()
        return


    def change_win_tickets(self, step, amount):
        if step == '1':
            self.cursor.execute('UPDATE `admin_set` SET `win_1`=%s', (amount))
            self.connection.commit()
            return
        elif step == '2':
            self.cursor.execute('UPDATE `admin_set` SET `win_2`=%s', (amount))
            self.connection.commit()
            return
        elif step == '3':
            self.cursor.execute('UPDATE `admin_set` SET `win_3`=%s', (amount))
            self.connection.commit()
            return
        elif step == '4':
            self.cursor.execute('UPDATE `admin_set` SET `win_4`=%s', (amount))
            self.connection.commit()
            return
        elif step == '5':
            self.cursor.execute('UPDATE `admin_set` SET `win_5`=%s', (amount))
            self.connection.commit()
            return

    def change_dep_tickets(self, many, summ, step):
        if step == '1':
            self.cursor.execute('UPDATE `admin_ticket_set` SET `ticket_many`=%s, `ticket_sum`=%s WHERE `id`=1', (many, summ))
            self.connection.commit()
            return
        elif step == '2':
            self.cursor.execute('UPDATE `admin_ticket_set` SET `ticket_many`=%s, `ticket_sum`=%s WHERE `id`=2', (many, summ))
            self.connection.commit()
            return
        elif step == '3':
            self.cursor.execute('UPDATE `admin_ticket_set` SET `ticket_many`=%s, `ticket_sum`=%s WHERE `id`=3', (many, summ))
            self.connection.commit()
            return
        elif step == '4':
            self.cursor.execute('UPDATE `admin_ticket_set` SET `ticket_many`=%s, `ticket_sum`=%s WHERE `id`=4', (many, summ))
            self.connection.commit()
            return
        elif step == '5':
            self.cursor.execute('UPDATE `admin_ticket_set` SET `ticket_many`=%s, `ticket_sum`=%s WHERE `id`=5', (many, summ))
            self.connection.commit()
            return
        elif step == '6':
            self.cursor.execute('UPDATE `admin_ticket_set` SET `ticket_many`=%s, `ticket_sum`=%s WHERE `id`=6', (many, summ))
            self.connection.commit()
            return
        elif step == '7':
            self.cursor.execute('UPDATE `admin_ticket_set` SET `ticket_many`=%s, `ticket_sum`=%s WHERE `id`=7', (many, summ))
            self.connection.commit()
            return

    def check_set_room_tick(self, step):
        if step == '1':
            self.cursor.execute('SELECT `ticket_many` FROM `set_tickets_win` WHERE `room`=1')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]
        elif step == '2':
            self.cursor.execute('SELECT `ticket_many` FROM `set_tickets_win` WHERE `room`=2')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]
        elif step == '3':
            self.cursor.execute('SELECT `ticket_many` FROM `set_tickets_win` WHERE `room`=3')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]
        elif step == '4':
            self.cursor.execute('SELECT `ticket_many` FROM `set_tickets_win` WHERE `room`=4')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]
        elif step == '5':
            self.cursor.execute('SELECT `ticket_many` FROM `set_tickets_win` WHERE `room`=5')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]
        elif step == '6':
            self.cursor.execute('SELECT `ticket_many` FROM `set_tickets_win` WHERE `room`=6')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]

    def ticket_room_change(self, step, amount):
        if step == '1':
            self.cursor.execute('UPDATE `set_tickets_win` SET `ticket_many`=%s WHERE `room`=1', (amount))
            self.connection.commit()
            return
        elif step == '2':
            self.cursor.execute('UPDATE `set_tickets_win` SET `ticket_many`=%s WHERE `room`=2', (amount))
            self.connection.commit()
            return
        elif step == '3':
            self.cursor.execute('UPDATE `set_tickets_win` SET `ticket_many`=%s WHERE `room`=3', (amount))
            self.connection.commit()
            return
        elif step == '4':
            self.cursor.execute('UPDATE `set_tickets_win` SET `ticket_many`=%s WHERE `room`=4', (amount))
            self.connection.commit()
            return
        elif step == '5':
            self.cursor.execute('UPDATE `set_tickets_win` SET `ticket_many`=%s WHERE `room`=5', (amount))
            self.connection.commit()
            return
        elif step == '6':
            self.cursor.execute('UPDATE `set_tickets_win` SET `ticket_many`=%s WHERE `room`=6', (amount))
            self.connection.commit()
            return


    def ban_or_unban(self, step, username):
        if step == '1':
            self.cursor.execute('INSERT INTO `banlist` (`username`) VALUES (%s)', (username))
            self.connection.commit()
            return
        elif step == '2':
            self.cursor.execute('DELETE FROM `banlist` WHERE `username`=%s', (username))
            self.connection.commit()
            return

    def check_channels(self):
        self.cursor.execute('SELECT `channel_name` FROM `channels`')
        result = self.cursor.fetchall()
        print(result)
        return result

    def del_channel(self, name):
        self.cursor.execute('DELETE FROM `channels` WHERE `channel_name`=%s', (name))
        self.connection.commit()
        return

    def add_channel(self, name):
        self.cursor.execute('INSERT INTO `channels` (`channel_name`) VALUES (%s)', (name))
        self.connection.commit()

    def day_work(self):
        self.cursor.execute('SELECT `days` FROM `admin_set`')
        result = self.cursor.fetchall()
        for row in result:
            return row[0]

    def plus_day(self):
        self.cursor.execute('UPDATE `admin_set` SET `days`=days+1')
        self.connection.commit()
        return

    def users_hours(self):
        self.cursor.execute('SELECT * FROM `users` WHERE `time_user` >= (now()- INTERVAL 24 hour)')
        result = self.cursor.fetchall()
        return len(result)
    
    
    def check_userid(self, user_id):
        self.cursor.execute('SELECT `balance` FROM `users` WHERE `user_id`=%s', (user_id))
        result = self.cursor.fetchall()
        result_row = '0'
        for row in result:
            result_row = row[0]

        if result_row == None:
            return 'usernot'
        elif result_row != None:
            return result_row

    def change_balance(self, user_id, amount):
        self.cursor.execute('UPDATE `users` SET `balance`=%s WHERE `user_id`=%s', (amount, user_id))
        self.connection.commit()
        return

    def check_ref_money(self):
        self.cursor.execute('SELECT `referal_money` FROM `admin_set`')
        money_ref = self.cursor.fetchall()
        for row in money_ref:
            return row[0]
    
    def add_for_promo(self, user_id):
        self.cursor.execute('SELECT `set_promo_money` FROM `admin_set`')
        result = self.cursor.fetchall()
        result_row = '0'
        for row in result:
            result_row = row[0]


        self.cursor.execute('UPDATE `users` SET `balance`=balance+%s WHERE `user_id`=%s', (result_row, user_id))
        self.connection.commit()
        return

    def add_for_check(self, user_id):
        self.cursor.execute('SELECT `set_check_money` FROM `admin_set`')
        result = self.cursor.fetchall()
        result_row = '0'
        for row in result:
            result_row = row[0]


        self.cursor.execute('UPDATE `users` SET `balance`=balance+%s WHERE `user_id`=%s', (result_row, user_id))
        self.connection.commit()
        return

    def summ_referals(self):
        self.cursor.execute('SELECT SUM(referals_quant) FROM `users`')
        result = self.cursor.fetchall()
        for row in result:
            return int(row[0])

    def check_date_btc(self, step):
        if step == '1':
            self.cursor.execute('SELECT day(date_next) FROM `btc_time`')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]
        elif step == '2':
            self.cursor.execute('SELECT month(date_next) FROM `btc_time`')
            result = self.cursor.fetchall()
            for row in result:
                return row[0]

    
    def dice_step1(self, user_id, summ):
        self.cursor.execute('DELETE FROM `dice` WHERE `user_id`=%s', (user_id))

        self.cursor.execute('SELECT `user_id` FROM `users` WHERE `user_id`=%s AND `balance` >=%s', (user_id, summ))
        result = self.cursor.fetchall()
        if len(result) == 1:

            self.cursor.execute('INSERT INTO `dice` (`user_id`, `sum`) VALUES (%s, %s)', (user_id, summ))
            self.connection.commit()
            return 'ok'
        elif len(result) == 0:
            return 'notmoney'


    def dice_step2(self, user_id):
        self.cursor.execute('SELECT `sum` FROM `dice` WHERE `user_id`=%s', (user_id))
        result = self.cursor.fetchall()
        for row in result:
            return row[0]

    def add_ticket(self, user_id):
        self.cursor.execute('UPDATE `users` SET `tickets`=tickets+1 WHERE `user_id`=%s', (user_id))
        self.connection.commit()
        return


    def add_msg(self, mesg):
        self.cursor.execute('INSERT INTO `messages` (text) VALUES (%s)', (mesg))
        self.connection.commit()
        self.cursor.execute('SELECT `text` FROM `messages` ORDER BY id DESC LIMIT 1')
        result = self.cursor.fetchall()
        for row in result:
            return row[0]
    def date_next(self):
        self.cursor.execute('UPDATE btc_time SET btc_time=(now()+INTERVAL 3 day)')
        self.connection.commit()
        return
    def send_msg(self):
        self.cursor.execute('SELECT `user_id` FROM `users`')
        result = self.cursor.fetchall()
        return result