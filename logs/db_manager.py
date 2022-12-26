'''
Chef        : gnbasyal
Chef-Id     : pvr2114
Dish        : db_manager
Created on  : Saturday, 25th September 2021 8:51:12 pm
'''
import json
import pandas as pd
import pyodbc
from datetime import datetime

with open(r'logs\db_config.json') as file:
    db_config = json.load(file)

class DBManager:
    def __init__(self):
        self.dbname = db_config['db_name']
        self.driver = db_config['driver']
        self.host = db_config['host']
        self.server = db_config['server']

        self.is_connected = self.try_connection()

        if self.is_connected:
            self.cur = self.connection.cursor()

    def try_connection(self):
        try:
            self.connection = pyodbc.connect(driver=self.driver,
                                            host=self.host,
                                            server=self.server,
                                            database=self.dbname,
                                            trusted_connection = 'Yes')
            print("Database connection established.")   
            return True

        except:
            print("Database connection failed.")
            return False
    
    def insert_entry_log(self,person,aisle,entry_time):
        if not self.is_connected:
            print("Database connection is not established. Log insertion failed.")
            return

        query = f"""
            INSERT INTO Logs (Person, Section, EntryTime, ExitTime)
            VALUES ('{person}','{aisle}','{entry_time}', null)
        """

        self.cur.execute(query)
        self.cur.commit()
        print('Log insertion successfull.')

    def set_exit_time(self,person,aisle,exit_time):
        if not self.is_connected:
            print("Database connection is not established. Setting exit time failed.")
            return

        query = f"""
            UPDATE Logs
            SET ExitTime = '{exit_time}'
            WHERE Person = '{person}' and Section = '{aisle}' and ExitTime IS NULL
        """

        self.cur.execute(query)
        self.cur.commit()
        print('Setting exit time successfull.')
    
    def disconnect(self):
        if self.is_connected:
            self.connection.close()
            print("Disconnected from database.")
            self.is_connected = False


if __name__ == '__main__':
    dbm = DBManager()
    # print(dbm.is_connected)
    # print(type(datetime.now().time()))
    dbm.insert_entry_log("P1","A2",datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    dbm.set_exit_time("P1", "A2", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))