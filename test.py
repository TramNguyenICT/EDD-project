import mysql.connector
import random

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='elfdeliverydash',
    user='maika',
    password='180790',
    autocommit=True,
    charset='utf8mb4',
    collation='utf8mb4_unicode_ci', )

# update airport finish = FALSE
sql1 = f"UPDATE airport SET is_finished = 0"
cursor = connection.cursor()
cursor.execute(sql1)

game_intro = "Hello!"
print(game_intro)
player_name = input("How should I call you?")
print("Hello", player_name)

reindeer_instruction = " "
print(reindeer_instruction)
print("Which one do you want?")

reindeer_choice = int(input("1.Rudolph, 2.Vixen, 3.Cupid (1/2/3)"))