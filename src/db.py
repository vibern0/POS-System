# -*- coding: utf-8 -*-

import sqlite3


class Database:

    def __init__(self):
        self.db = sqlite3.connect('possystem.db')
        self.db_cursor = self.db.cursor()

    def register_logs(self, user_id, log_type):
        query = 'INSERT INTO logs(id, type) VALUES('\
                + str(user_id) + ','\
                + str(log_type) + ')'
        self.db_cursor.execute(query)
        self.db.commit()

    def register_buy(self, buy_list, pay_number, employ_name):
        query = 'INSERT INTO buylist(pay_number, total_price, author) VALUES('\
                + str(pay_number) + ','\
                + str(buy_list.get_total_price()) + ', \''\
                + employ_name + '\')'
        self.db_cursor.execute(query)
        self.db.commit()

        id_list = self.db_cursor.lastrowid
        for item in buy_list.get_all_items() :
            query = 'INSERT INTO articles_buylist(id_list, id_product, price, tax) VALUES('\
                    + str(id_list) + ', '\
                    + str(item.get_id()) + ', '\
                    + str(item.get_price()) + ', '\
                    + str(item.get_tax()) + ')'
            self.db_cursor.execute(query)
            self.db.commit()
            # remove from stock
            query = 'UPDATE products SET stock=stock-1 WHERE id=' + str(item.get_id())
            self.db_cursor.execute(query)
            self.db.commit()

    def load_articles(self, menu_type, menu_page):
        # check if stock > 0
        query = 'SELECT id, name, price FROM products WHERE type="'\
                + menu_type + '" AND stock > 0  LIMIT '\
                + str(menu_page * 9) + ', '\
                + str((menu_page + 1) * 9 + 1)
        cursor = self.db.execute(query)
        return cursor

    def is_valid_login(self, username, password):
        query = 'SELECT id FROM users WHERE name=\''\
                + username + '\' AND password=\''\
                + password + '\''
        cursor = self.db.execute(query)
        row = cursor.fetchone()
        return row
