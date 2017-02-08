import sqlite3
import time
import datetime
import random

connection = sqlite3.connect('tictactoe_decision_tree_agent.dp')
cursor = connection.cursor()

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS actionSequence(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def create_table_agentExperience():
    cursor.execute('CREATE TABLE IF NOT EXISTS agentExperience(zobrist_hash INTEGER, use_value REAL, alpha_beta_window INTEGER, ply INTEGER, depth INTEGER, player_turn INTEGER)')

def insert_agent_experience(zobrist_hash, use_value, alpha_beta_window, ply, depth, player_turn):
    

def data_entry():
    cursor.execute("INSERT INTO actionSequence VALUES(123123123, '2016-01-01', 'Python', 5)")
    connection.commit()
    cursor.close()
    connection.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%d-%m-%Y %H %M %S'))
    keyword = 'Python'
    value = random.randrange(0, 10)
    cursor.execute("INSERT INTO actionSequence (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
                   (unix, date, keyword, value))
    connection.commit()

def read_from_db():
    cursor.execute("SELECT * FROM actionSequence WHERE value=3 AND keyword='Python'")
    # data = cursor.fetchall()
    # print data
    for row in cursor.fetchall():
        print row

# create_table()
# data_entry()
# for i in range(10):
#     dynamic_data_entry()
#     time.sleep(1)

read_from_db()

cursor.close()
connection.close()