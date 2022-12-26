'''
Chef        : gnbasyal
Chef-Id     : pvr2114
Dish        : logs
Created on  : Saturday, 25th September 2021 10:20:49 am
'''
import pandas as pd
from logs.db_manager import DBManager

class Logs:
    def __init__(self):
        self.logs = pd.DataFrame(columns=['Person','Section','EntryTime','ExitTime'])
        self.ENTRY = 'entry'
        self.EXIT = 'exit'
        self.dbm = DBManager()

    def update_df(self, person_id, aisle, action, time):
        # with self.logs as logs:
        if action == self.ENTRY:
            print(f"P{person_id} entered {aisle} at {time}")
            self.logs.loc[len(self.logs)] = {'Person':f'P{person_id}','Section':aisle,'EntryTime':time,'ExitTime':''}
            self.dbm.insert_entry_log(f'P{person_id}', aisle, time.strftime('%Y-%m-%d %H:%M:%S'))

        if action == self.EXIT:
            print(f"P{person_id} exited {aisle} at {time}")
            self.logs.loc[(self.logs['Person']==f'P{person_id}') & (self.logs['Section']==aisle) & (self.logs['ExitTime']==''), 'ExitTime'] = time
            self.dbm.set_exit_time(f'P{person_id}', aisle, time.strftime('%Y-%m-%d %H:%M:%S'))

    def save_to_csv(self,path):
        self.logs.to_csv(path)
        
        self.dbm.disconnect()

if __name__ == '__main__':
    logger = Logs()
    logger.update_df('1','A1',logger.ENTRY, '19:23:07.170704')
    logger.update_df('1','A1',logger.EXIT, '19:23:08.373235')
    logger.update_df('1','A3',logger.ENTRY, '19:23:08.387414')
    logger.save_to_csv('logs_test.csv')
    print(logger.logs)