import mysql.connector
import random

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'elfdeliverydash',
    user = 'root',
    password = '180790',
    autocommit = True,
    charset='utf8mb4',
    collation='utf8mb4_unicode_ci',)

airport_id_list = list()
sql15 = f"select airport_id from airport where is_finished = '0'"
cursor = connection.cursor()
cursor.execute(sql15)
airport_id_list = cursor.fetchall()
