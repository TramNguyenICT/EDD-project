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

#update airport finish = FALSE
game_intro ="Hello!"
print(game_intro)
player_name = input("How should I call you?")
print("Hello", player_name)
# tạo 1 player mới vào bảng player
reindeer_instruction = " "
print(reindeer_instruction)
print("Which one do you want?")

reindeer_choice = int(input("1.Rudolph, 2.Vixen, 3.Cupid (1/2/3)"))
while True:
    if reindeer_choice == 1:
        reindeer_id = 2001
        break
    elif reindeer_choice == 2:
        reindeer_id = 2002
        break
    elif reindeer_choice == 3:
        reindeer_id = 2003
        break
    else:
        reindeer_choice = int(input("Invalid choice. 1.Rudolph, 2.Vixen, 3.Cupid (1/2/3) ")
# cập nhật reindeer_id vào bảng player
grinch_challenge = random.randint(1,6)
grinch_airport = random.randint(1002,1059)
# cập nhật grinch_challenge_id vào airport id đó)
helsinki_welcome =" "
print(helsinki_welcome)

def airport_direction():
    
    sql15 = f"select airport_id from airport where is_finished = '0'"
    cursor = connection.cursor()
    cursor.execute(sql15)
    airport_id_tuples = cursor.fetchall()
    airport_id_list = [item[0] for item in airport_id_tuples]
    airport_id_list.remove("1001", "1060")
    
    next_airport_left = random.choice(airport_id_list)
    sql16 = f"select airport_name from airport where airport_id = {next_airport_left}"
    cursor.execute(sql16)
    next_airport_left_name = cursor.fetchall()
    airport_id_list.remove(next_airport_left)
    next_airport_right = random.choice(airport_id_list)
    sql17 = f"select airport_name from airport where airport_id = {next_airport_right}"
    cursor.execute(sql17)
    next_airport_righ_name = cursor.fetchall()
    
    print(f"On your left is {next_airport_left_name} and on the right is {next_airport_right_name}. Where do you want to go?")
    airport_direction_choice = input("Type L for left or R for right: ")
    while True:
        if airport_direction_choice == "L":
            current_airport = next_airport_left
            break
        elif airport_direction_choice == "R":
            current_airport = next_airport_right
            break
        else:
            airport_direction_choice = input("Invalid choice. Type L for left or R for right: ")
    return current_airport





if airport_id == 1041:
    print("Welcome to Kristainsand Airport, the most crowded airport in Norway.")
    print("You got 10 letters.")
    f@select description from airport
    letter_count += 10
    # cập nhật vào database is_finished = True
    # cập nhật letter_count
    sql = "UPDATE airports SET is_finished = TRUE where airport_id == 1041"

if airport_id == 1042:
    print("Hello from Hausesund Airport.")
    print("You have to answer a question. You will get 5 letters if correct!")
    print("What are two things you can never eat for breakfast? (the answers are sep")
    answer1042_1st = input("First thing is: ").lower().strip()
    answer1042_2nd = input("Second thing is: ").lower().strip()
    if (answer1042_1st == "lunch" and answer1042_2nd=="dinner") or (answer1042_1st == "dinner" and answer1042_2nd=="lunch"):
        print("That's right! You got 5 more letters!")
        letter_count += 5
    else:
        print("Incorrect! You got nothing!")
    # cập nhật vào database is_finished = True
    # cập nhật letter_count

if airport_id == 1043:
    print("You are arrived at Harstad Airport.")
    print("I was wonder are you a cat person or a dog person?")
    answer1043 = input("A.dog person\n B.cat person (A/B)").lower().strip()
    print("It's okay, both dog and cat are greats. You get 10 more letters for answering my question!")
    letter_count += 10
    # cập nhật vào database is_finished = True
    # cập nhật letter_count

if airport_id == 1044:
    print("It's Floro Airport. Can you hear me?")
    print("Yay, we have a new visitor")
    print("Unfortunately, you lost 5 letters ")
    letter_count -= 5
    print("Spend your time enjoy our city. Thank you!")
    # cập nhật vào database is_finished = True
    # cập nhật letter_count

if airport_id == 1045:
    print("Ho ho, Bodo's hereeeeeee!")
    print("In your opinion, Major General Sir Nils Oval III is...")
    answer1045 = input("A.a reindeer, B.a polar bear, C.a penguin (A/B/C)").lower().strip()
    if answer1045 == "c":
        letter_count += 10
        print("You got 10 letters")
    else:
        letter_count -= 5
        print("You lost 5 letters")
    print("Major General Sir Nils Oval III, Baron of the Bouvet Islands, is a king penguin who resides in Edingurgh Zoo, Scotland.")
    print("He is the mascot and colonel-in-chief of the Norwegian King's Guard")
    # cập nhật vào database is_finished = True
    # cập nhật letter_count

if airport_id == 1046:
    print("Welcome")
    answer1046 = input("Do you know what is the second largest city in Norway?").lower().strip()
    if answer1046 == "bergen":
        print("That's right! You got 5 letters")
        letter_count += 5
    else:
        print("Silly! It's here, Bergen. You lost 10 letters")
        letter_count -= 10
    # cập nhật vào database is_finished = True
    # cập nhật letter_count

if airport_id == 1047:
    print("Badufoss Airport's here!")
    answer1047 = input("Which came first, the chicken or the egg?").lower().strip()
    print("Just asking for fun :D. I don't care about the answer.")
    print("Here is your 5 letters. Bye bye")
    letter_count += 5
    # cập nhật vào database is_finished = True
    # cập nhật letter_count

if airport_id == 1048:
    print("Welcome to Trondheim Airport!")
    print("Do you know which sushi comes from Norway?")
    answer1048 = input("A. Salmon, B. Tuna, C. Shrimp").lower().strip()
    if answer1048 == "a":
        letter_count += 10
        print("You got 10 letters")
    else:
        letter_count -= letter_change
        print("You lost 5 letters")
    print("The Norwegians invented this dish in the 1980s")
    # cập nhật vào database is_finished = True
    # cập nhật letter_count

if airport_id == 1049:
    print("Welcome to Aalborg Airport.")
    print("Hmm")
    print("Hmm")
    print("Hmm")
    print("Hmm")
    print("You're still here?")
    print("There's nothing here! You go ahead! Bye!")
    # cập nhật vào database is_finished = True
if airport_id == 1050:
    print("You are arrived at Aarhus Airport!")
    answer1050 = input("What travels the world while stuck in one spot?").lower().strip()
    if answer1050 == "stamp" or "astamp" or "thestamp" or "stamps" or "thestamps":
        print("Brilliant! You are so smart! You got 10 more letters!")
        letter_count += 10
    else:
        print("It's the map!")
        print("You lost 5 letters")
        letter_count -= 5
    # cập nhật vào database is_finished = True
    # cập nhật letter_count
if airport_id == 1051:
    print("Welcome to Billund Air...")
    print("Oppps. You step on a LEGO block. That's hurt! You lost 5 letters to treat you leg!")
    letter_count -= 5
    print("Be careful! Cause you are in Denmark. The origin country of LEGO")
    # cập nhật vào database is_finished = True
    # cập nhật letter_count

if airport_id == 1052:
    #print("You are arrived at Bornholm Airport!")
    print("I have a question for you!")
    print("Which one is the highest mountain in Denmark?")
    answer1052 = input("A.Aarhus, B.Bergen, C.Thisted").lower().strip()
    print("Nitwit. Denmark has no mountain!")
    print("Bye bye")
    # cập nhật vào database is_finished = True
if airport_id == 1053:
    #print("Welcome")
    print("The Danish cookies is so good, you taste them and you lose 10 letters for the cookies")
    # cập nhật vào database is_finished = True
    # cập nhật letter_count
if airport_id == 1054:
    print("Welcome")
    answer1054 = input("What will you actually find at the end of every rainbow?").lower().strip()
    if answer1054 == "w":
        print("Brilliant! You got 5 letters.")
        letter_count += letter_change
    else:
        print("It's the letter W. You lost 5 letters.")
        letter_count -= letter_change
    # cập nhật vào database is_finished = True
    # cập nhật letter_count
if airport_id == 1055:
    print("Welcome")
    print("Sorry, you lost 5 letters.")
    letter_count -= letter_change
    # cập nhật vào database is_finished = True
    # cập nhật letter_count
if airport_id == 1056:
    print("Welcome")
    print("This airport is on maintenance, sorry. Keep countinuing your journey!")
    # cập nhật vào database is_finished = True
if airport_id == 1057:
    print("Welcome")
    print("Is Cinderella a story a story by Danish Writer Hans Andersen?")
    answer1057 = input("Yes/No").lower().strip()
    if answer1057 == "no" or answer1057 == "n":
        print("That's right. It's Brothers Grimm's. Hans' notable works are The Little Mermaid and The Snow White")
    else:
        print("Wrong. It's Brothers Grimm's. You lost 10 letters.")
        letter_count -= letter_change
    # cập nhật vào database is_finished = True
    # cập nhật letter_count
if airport_id == 1058:
    print("Welcome")
    answer1058 = ("Fill in the blank: Finland has Sisu, and Denmark has...").lower().strip()
    if answer1058 == "hygge":
        print("Yep, you got 10 more letters")
        letter_count += letter_change
    else:
        print("No, you lost 10 letters")
        letter_count -= letter_change
    print("Hygge is a word in Danish that describes a cozy, contented mood evoked by comfort and conviviality.")
    # cập nhật vào database is_finished = True
    # cập nhật letter_count
if airport_id == 1059:
    print("Welcome")
    answer1059 = input("Where is an ocean with no water?").lower().strip()
    if answer1059 == "map" or "themap" or "onthemap" or "inthemap":
        print("Brilliant! You are so smart! You got 10 more letters!")
        letter_count += letter_change
    else:
        print("It's the map!")
        print("You lost 5 letters")
        letter_count -= letter_change
    # cập nhật vào database is_finished = True
    # cập nhật letter_count
if airport_id == 1060:
    print("Welcome")
    print("You meet a poor girl selling matches on the street. What would you do?")
    answer1060 = input("A.Nothing. B.Buy all the matches. C. Give her food. (A/B/C)").lower().strip()
    if answer1060 == "b" or "c":
        print("You have such a warm heart. Here are your 10 letters.")
        letter_count += letter_change
    else:
        print("Don't be so cold. You lost 10 letters.")
        letter_count -= letter_change
