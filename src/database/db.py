# -*- coding: utf-8 -*-

import sqlite3

import sys
sys.path.append('./../src/')

from pos.pos_system import Item

class Database():
    
    def __init__(self):
        self.db = sqlite3.connect('database/possystem.db')
        self.db_cursor = self.db.cursor()
    
    
    def registerLogs(self, user_id, log_type):
        query = 'INSERT INTO logs(id, type) VALUES(' + str(user_id) + ',' + str(log_type) + ')'
        self.db_cursor.execute(query)
        self.db.commit()
    
    
    def registerBuy(self, buy_list, pay_number, employ_name):
        query = 'INSERT INTO buylist(pay_number, total_price, author) VALUES(' + str(pay_number) + ',' + str(buy_list.getTotalPrice()) + ', \'' + employ_name + '\')'
        
        self.db_cursor.execute(query)
        self.db.commit()
        
        id_list = self.db_cursor.lastrowid
        for item in buy_list.getAllItems() :
            query = 'INSERT INTO articles_buylist(id_list, id_product, price, tax) VALUES(' + str(id_list) + ', ' + str(item.getID()) + ', ' + str(item.getPrice()) + ', ' + str(item.getTax()) + ')'
            self.db_cursor.execute(query)
            self.db.commit()
            #remove from stock
            query = 'UPDATE products SET stock=stock-1 WHERE id=' + str(item.getID())
            self.db_cursor.execute(query)
            self.db.commit()
    
    def loadArticles(self, menu_type, menu_page):
        #check if stock > 0
        query = 'SELECT id, name, price FROM products WHERE type="' + menu_type + '" AND stock > 0  LIMIT ' + str(menu_page * 9) + ', ' + str((menu_page + 1) * 9 + 1)
        cursor = self.db.execute(query)
        return cursor
    
    
    def isValidLogin(self, username, password):
        query = 'SELECT id FROM users WHERE name=\'' + username + '\' AND password=\'' + password + '\''
        cursor = self.db.execute(query)
        row = cursor.fetchone()
        #
        return row