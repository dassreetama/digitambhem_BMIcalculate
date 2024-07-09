import sqlite3
from datetime import datetime

class DataStorage:
    def __init__(self, db_name="bmi_data.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()
        
    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS bmi_records
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                           weight REAL,
                           height REAL,
                           bmi REAL)''')
        self.conn.commit()
        
    def insert_record(self, weight, height, bmi):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO bmi_records (weight, height, bmi)
                          VALUES (?, ?, ?)''', (weight, height, bmi))
        self.conn.commit()
        
    def get_all_records(self):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT * FROM bmi_records ORDER BY timestamp DESC''')
        return cursor.fetchall()
    
    def close_connection(self):
        self.conn.close()
