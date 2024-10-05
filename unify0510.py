import mysql.connector
import random

connection = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    database = 'elfdeliverydash',
    user = 'dokyeom',
    password = 'seventeen17',
    autocommit = True,
    charset='utf8mb4',
    collation='utf8mb4_unicode_ci',
)

# update airport finish = FALSE
sql1 = f"UPDATE airport SET is_finished = 0"
cursor = connection.cursor()
cursor.execute(sql1)
connection.commit()

#cap nhat grinch id trong airport = null
sql2 = f"UPDATE airport SET grinch_id = NULL"
cursor.execute(sql2)
connection.commit()


game_intro = ("Welcome to ELF DELIVERY DASH!\n"
              "You’re the fastest elf, and Santa’s counting on you to deliver 100 letters from children around the world.\n"
              "But it won’t be easy! As you travel across different Nordic airports, tricky challenges and the sneaky Grinch will try to stop you.\n"
              "Some challenges based on real world facts, others… well, let’s just say you’ll need a sense of humor.\n"
              "Can you make it back to Santa with all 100 letters or even more and save Christmas?")
print(game_intro)
print("Press any key to start the game!")
input()

print("What is your elf name?")
player_name = input("Type your elf name here: ")

reindeer_instruction = ("Surprise! You won't be alone on this adventure!\n"
                        "It's time to choose your reindeer - your trusty companion!\n"
                        "Each reindeer has its own special ability, useful for specific airports along the way!")
print(reindeer_instruction)
each_reindeer_introduction=("Let's get to know our reindeers!\n"
                            "Rudolph: the world famous reindeer, and everyone recognizes him!\n"
                            "Vixen: a super intelligent reindeer who's great with all things logical and linguistic\n"
                            "Cupid: the reindeer of love, with a charm that wins the hearts of everyone around")
print(each_reindeer_introduction)
print("Who will be your companion?")

reindeer_choice = int(input("1.Rudolph, 2.Vixen, 3.Cupid (Enter 1, 2 or 3): "))
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
        reindeer_choice = int(input("Invalid choice. Please choose again! 1.Rudolph, 2.Vixen, 3.Cupid  (Enter 1, 2 or 3): "))

print(f"Alright {player_name}, let's start your journey!")

# cập nhật player_name và reindeer_id vào bảng player

sql3 = f"INSERT INTO player(player_name, reindeer_id) VALUES ('{player_name}',{reindeer_id});"
cursor = connection.cursor()
cursor.execute(sql3)
connection.commit()
player_id = cursor.lastrowid

grinch_challenge = random.randint(1, 6)
grinch_airport = random.randint(1002, 1059)

# cập nhật grinch_challenge_id vào airport id đó)
sql4 = f"UPDATE airport SET grinch_id = {grinch_challenge} WHERE airport_id ={grinch_airport}"
cursor = connection.cursor()
cursor.execute(sql4)
connection.commit()

helsinki_welcome = ("Welcome to Helsinki-Vantaa Airport! This is the starting point for your exciting journey!\n"
                    "You've got 100 letters in your bag, so keep track of them!\n"
                    "The number of letters is the key to your victory!")
print(helsinki_welcome)
current_airport = 1001
sql5 = f"UPDATE player SET letter_count = (SELECT letter_change FROM airport WHERE airport_id = 1001) WHERE player_id = '{player_id}'"
cursor.execute(sql5)
letter_count = cursor.fetchone()

# cập nhật is_finished của Helsinki = 1
sql6 = f"UPDATE airport SET is_finished = '1' WHERE airport_id = '{current_airport}'"
cursor = connection.cursor()
cursor.execute(sql6)
connection.commit()

def update_current_airport(player_id, current_airport):
    sql7 = f"UPDATE player SET current_airport = '{current_airport}' WHERE player_id = '{player_id}'"
    cursor.execute(sql7)
    sql8 = f"UPDATE airport SET is_finished = '1' WHERE airport_id = '{current_airport}'"
    cursor.execute(sql8)
    connection.commit()

def airport_direction():
    # tao ra airport_list
    sql9 = f"select airport_id from airport where is_finished = '0'"
    cursor.execute(sql9)
    airport_id_tuples = cursor.fetchall()
    airport_id_list = [item[0] for item in airport_id_tuples]
    airport_id_list.remove(1060)

    next_airport_left = random.choice(airport_id_list)
    sql10 = f"select airport_name from airport where airport_id = {next_airport_left}"
    cursor.execute(sql10)
    next_airport_left_tuple = cursor.fetchall()
    next_airport_left_name = next_airport_left_tuple[0][0]
    airport_id_list.remove(next_airport_left)
    next_airport_right = random.choice(airport_id_list)
    sql11 = f"select airport_name from airport where airport_id = {next_airport_right}"
    cursor.execute(sql11)
    next_airport_right_tuple = cursor.fetchall()
    next_airport_right_name = next_airport_right_tuple[0][0]

    print(f'On your LEFT is "{next_airport_left_name}" and on the RIGHT is "{next_airport_right_name}". Where do you want to go?')
    airport_direction_choice = input("Type L for LEFT or R for RIGHT: ").lower().strip()
    while True:
        if airport_direction_choice == "l":
            current_airport = next_airport_left
            break
        elif airport_direction_choice == "r":
            current_airport = next_airport_right
            break
        else:
            airport_direction_choice = input("Invalid choice. Please type again!\nType L for left or R for right: ").lower().strip()
    # cập nhật current airport vào bảng player
    update_current_airport(player_id, current_airport)
    return current_airport

def airport_greeting(airport_id):
    sql12 = f"SELECT greeting FROM airport WHERE airport_id = {airport_id}"
    cursor.execute(sql12)
    greeting_tuple = cursor.fetchall()
    greeting = greeting_tuple[0][0]
    return greeting

def get_airport_reindeer_id(airport_id):
    # test the reindeer_id in this airport
    sql13 = f"SELECT reindeer_id FROM airport WHERE airport_id = {airport_id}"
    cursor.execute(sql13)
    airport_reindeer_id_tuple = cursor.fetchall()
    airport_reindeer_id = int(airport_reindeer_id_tuple[0][0])
    return airport_reindeer_id

def get_letter_count(player_id):
    sql14 = f"SELECT letter_count FROM player WHERE player_id = {player_id}"
    cursor.execute(sql14)
    letter_count_tuple = cursor.fetchall()
    return int(letter_count_tuple[0][0])

def update_letter_count(player_id,letter_count):
    sql15 = f"UPDATE player SET letter_count = {letter_count} WHERE player_id = '{player_id}'"
    cursor.execute(sql15)
    connection.commit()

def grinch_quiz(challenge_id):
    sql16= f"SELECT letter_change_grinch FROM grinch WHERE grinch_challenge_id = {grinch_challenge}"
    cursor.execute(sql16)
    letter_change_grinch_tuple = cursor.fetchall()
    letter_change_grinch = int(letter_change_grinch_tuple[0][0])
    letter_count = get_letter_count(player_id)
    print("Hahaha, Grinch is here.")
    print("What a coincidence we met!")
    print("I have a challenge for you, little elf.")
    if challenge_id == 1:
        print("Do you like Christmas Carol?")
        choice = input("Type Yes or No: ").lower().strip()
        if choice in ["no", "n"]:
            print("It's strange for an elf not to like any Christmas Carols.")
            print("I like you, sweetie.")
            print("Take these 20 letters.")
            letter_count += letter_change_grinch
        else:
            print("I hate Christmas, I hate anything related to Christmas.")
            print("I will stole 20 letters from you, hahaha.")
            print("Good bye, little elf!")
            letter_count -= letter_change_grinch
    if challenge_id == 2:
        print("What is your favorite color?")
        choice = input("Answer: ").lower().strip()
        if choice == "green":
            print("That's basically me!")
            print("I will give you 10 letters for that.")
            letter_count += letter_change_grinch
        else:
            print("Noooo, only green is beautiful! Nothing else!")
            print("I don't like you! Bye bye!")
    if challenge_id == 3:
        print("What’s faster: a sneeze or a cheetah?")
        choice = input("A. Sneeze\nB. Cheetah\n"
                       "Type A or B: ").lower().strip()
        if choice == "a" or choice == "sneeze":
            print("Hmm, a smart elf. I've never thought you could get the right answer!")
            print("Here is 20 letters for you!")
            letter_count += letter_change_grinch
        else:
            print("It's Sneeze, silly elf! A sneeze can travel up to 160 km/h, faster than a cheetah’s sprint!")
            print("So sad, you lost 20 letters!")
            letter_count -= letter_change_grinch
    if challenge_id == 4:
        print("Which would taste worse: a sock-flavored ice cream or ketchup-flavored toothpaste?")
        choice = input('A. A sock-flavored ice cream\nB, A ketchup-flavored toothpaste').lower().strip()
        if choice == "b":
            print("Okay, at least it is edible but ewwww! Here are 20 letters for your unique taste!")
            letter_count += letter_change_grinch
        else:
            print("No silly elf, you can't eat the toothpaste. Give me 20 letters!")
            letter_count -= letter_change_grinch
    if challenge_id == 5:
        print("What is the name of my dog? ")
        choice = input("A.Milo, B.Max, C.Rex, D.Leo").lower().strip()
        if choice == "b" or choice == "max":
            print(
                "Yes, the most adorable dog in the world is Max!!! I will give you 10 letters just because I love Max!")
            letter_count += letter_change_grinch
        else:
            print("How come you don't know my Max, such a cute dog! How pitiful. Give me 10 letters!")
            letter_count -= letter_change_grinch
    if challenge_id == 6:
        print("What do I want to receive for Christmas?")
        choice = input("A. A huge Christmas cake\nB. New Iphone 16\nC. New dogs clothes\nD. A Sweaters\n"
                       "Type A,B,C or D: ")
        if choice == "c":
            print("I hate Christmas but Max, my dog, always has to be warm. You want to give him some, right?")
            print("Anyway, I give you 10 letters, just because of Max")
            letter_count += letter_change_grinch
        else:
            print("You silly elf! I hate Christmas so I don't need anything.\n"
                  "But perhaps Max, my dog, needs some more clothes to survive this winter.")
            print("I'm not happy with your answer. I will take 10 letters from you.")
            letter_count -= letter_change_grinch
    update_letter_count(player_id, letter_count)

def check_the_grinch(airport_id):
    if grinch_airport == airport_id:
        grinch_quiz(grinch_challenge)
        letter_count = get_letter_count(player_id)
        print(f"Currently, you have {letter_count} letters.")
        print("That was an unexpected interaction! Press ENTER to continue the journey. ")


def airport_quiz(airport_id):
    # print airport welcome
    print(airport_greeting(airport_id))

    #get the value of letter_change
    sql17 = f"SELECT letter_change FROM airport WHERE airport_id = {airport_id}"
    cursor.execute(sql17)
    letter_change_tuple = cursor.fetchall()
    letter_change = int(letter_change_tuple[0][0])

    #get the value of letter_count of player
    letter_count = get_letter_count(player_id)

    #get the reindeer_id
    sql18 = f"SELECT reindeer_id FROM player WHERE player_id = '{player_id}'"
    cursor.execute(sql18)
    reindeer_id_tuple = cursor.fetchall()
    reindeer_id = int(reindeer_id_tuple[0][0])

    if airport_id == 1002:
        print("Where is Ivalo Aiport located?")
        a1002 = input('A. Northern Finland\nB. Southern Finland\n'
                      'Type A or B to answer: ').lower().strip()
        if a1002 == 'a':
            print('Congratulations! You got 10 letters!')
            letter_count += letter_change
        else:
            print("Sorry, it's in the Northern part of Finland! You lose 10 letters this time!")
            letter_count -= letter_change

    if airport_id == 1003:
        a1003 = input("Why did two 4s skip lunch? Because they already ...?").lower().strip()
        if a1003 in ["8", "eight", "ate"]:
            print("Correct! You got 4 letters!")
            letter_count += letter_change
        else:
            print("Not the right answer. It's 8 (or ate)! You lose 4 letters!")
            letter_count -= letter_change

    if airport_id == 1004:
        print("What's the English equivalent of 'Opiskelija'?")
        a1004 = input('Opiskelija means: ').lower().strip()
        if a1004 == 'student':
            print("Somebody knows their Finnish! You got 2 letters!")
            letter_count += letter_change

        else:
            print("Not really, you lose 2 letters!")
            letter_count -= letter_change

    if airport_id == 1005:
        print("You’re in a Finnish forest and spot a polar bear! What should you do?")
        a1005 = input("A. Run for your life\nB. Play dead\nC. Try to make yourself look bigger").lower().strip()
        print("HAHAHA! Good one, but there are no polar bears in the wild here! You get nothing!")

    if airport_id == 1006:
        print("Ready to test your knowledge about the Northern Lights?")
        print("What are the Northern Lights also known as?")
        answer1006 = 'aurora borealis'
        a1006 = input("The answer is: ").lower().strip()
        if a1006 == answer1006 or a1006 == 'aurora':
            print("Congratulations! 10 more letters now are in your bag!")
            letter_count += letter_change
        else:
            print("Sorry, the answer is 'aurora'. You lose 10 letters!")
            letter_count -= letter_change

    if airport_id == 1007:
        print("Let's rearrange the letters of these English words so that they still have meanings:\n"
              "LISTEN, RACE, CINEMA")
        if reindeer_id == 2002:
            print("Hi, it's me, Vixen - your reindeer!")
            print("I can help you with this!")
            print("I have a close friend, he is a care iceman but he is a bit silent.")
            print("That's the hint. Good luck")
        a1007a = input("LISTEN--> ").lower().strip()
        a1007b = input("RACE--> ").lower().strip()
        a1007c = input("CINEMA--> ").lower().strip()
        if a1007a == 'silent' and a1007b == 'care' and a1007c == 'iceman':
            print("Congratulations! You got 6 letters!")
            letter_count += letter_change
        else:
            print("Sorry, you lose 6 letters! The answers are 'silent', 'care' and 'iceman'!")
            letter_count -= letter_change

    if airport_id == 1008:
        a1008 = input("Can you guess what is the largest living organism on Earth?\n"
                      "Type your answer here: ").lower().strip()
        if a1008 == 'mushroom':
            print("Bravo! You got 4 letters!")
            letter_count += letter_change
        else:
            print("Sorry, 4 letters are taken from your bag! The answer is mushroom!")
            letter_count -= letter_change

    if airport_id == 1009:
        letter_count += letter_change

        # change random two remaining reindeers
    if airport_id == 1010:
        print("Which of the following is a unique feature of Oulu Airport?")
        a1010 = input("A. It has a sea-facing runway\nB. It operates only at night.\nC. It has a cold weather laboratory for aircraft\nD. It uses solar-powered control towers\n"
                      "Type A,B,C or D: ").lower().strip()
        if a1010 == 'c':
            print("You are correct! You get more 10 letters.")
            letter_count+=letter_change
        elif a1010 == 'a' or a1010 == 'b' or a1010=='d':
            print("Not quite! The answer is C: It has a cold weather laboratory for aircraft.")
            letter_count-=letter_change
        else:
            print("Hmm... that doesn't seem like a valid choice. Let's keep moving!")
            letter_count-=letter_change

    if airport_id == 1011:
        letter_count -= letter_change

    if airport_id == 1012:
        letter_count += letter_change

    if airport_id == 1013:
        print("Phew! This airport is challenge-free! You can move to the next airport.")

    if airport_id == 1014:
        print("You meet a poor girl selling matches on the street. What would you do?")
        answer1060 = input("A. Ignore here\nB. Buy all the matches\nC. Share some food with her \nType A,B or C\n").lower().strip()
        if answer1060 in ["b", "c"]:
            print("You have such a warm heart. Here are your 10 letters.")
            letter_count += letter_change
        else:
            print("Don't be so cold-hearted. You lost 10 letters for not helping.")
            letter_count -= letter_change

    if airport_id == 1015:
        print("I am an odd number. But if you take away a letter from my name, I will become even. What am I?")
        a1015 = input("I am ").lower().strip()
        if a1015 == 'seven' or a1015 == '7':
            print("Congratulations, smart one! You got 5 letters!")
            letter_count += letter_change
        else:
            print("Sorry, the answer is 7 (seven). You've just lost 5 letters!")
            letter_count -= letter_change

    if airport_id == 1016:
        print("Yikes! You just lost 50 letters at this airport for some reasons. How unfair!")
        letter_count -= letter_change

        if reindeer_id == 2001:
            print('Citizens:"Wait a minute, is that RUDOLPH?????"\n'
                  'We are your biggest fans!\n'
                  'We’ll help you get your letters back!')
            print("Press Enter for the citizens to help Rudolph")
            input()
            print('Yay, here is your 50 letters.\n'
                  'Goodbye, Rudolph. Have a nice trip!')
            letter_count += letter_change

    if airport_id == 1017:
        print("Alert!!! Your letters have just magically doubled! What a nice day to be an elf!")
        letter_count *= letter_change

    if airport_id == 1018:
        print("Do you like chocolate? 🍫")
        a1018 = input("Type 'Yes' or 'No':\n ").lower().strip()
        if a1018 == 'yes':
            print("You're off to explore the magical Chocolate Factory (just like Charlie and the Chocolate Factory).\n"
                  "It cost you 10 letters but it was super fun!.")
            letter_count -= letter_change
        if a1018 == 'no':
            print("Boring! But hey, let's go to the next airport instead!")

    if airport_id == 1019:
        print("A sneaky elf who is also on a mission steals your bag!\n"
              "Press Enter to go find your bag!")
        input()
        print("You found it! But half of your letters is already gone! So rude! Let's move out of here!")
        letter_count = letter_count // letter_change

    if airport_id == 1020:
        print("🐄 Let's help the farmer out!")
        a1020 = input("A farmer has 15 cows, and all but 8 of them run away.\n"
                      "How many cows does the farmer have left?\n"
                      "Give a number: ").lower().strip()
        if a1020 == '8' or a1020 == 'eight':
            print("You're right! 5 letters more for you!")
            letter_count += letter_change
        else:
            print("Oops! Read it again! 8 is the correct answer. You lose 5 letters.")
            letter_count -= letter_change

    if airport_id == 1021:
        print("Do you know the famous band ABBA is from Sweden?\n"
              "Let's fill in the lyrics of their song Dancing Queen to gain 5 letters!\n"
              "Press Enter to see the lyrics")
        input()
        print("You can dance, you can jive\n"
              "Having the time of your life\n"
              "Ooh, see that girl, watch that scene\n"
              "_____________ the dancing queen")

        print("Choose the correct lyrics from the following options:")
        print("A. Dancing\nB. Singing\nC. Digging")
        answer1021 = input("Enter the correct choice (A, B, or C)\n").lower().strip()
        if answer1021 == "c":
            print("Correct! You win 5 letters!")
            letter_count += letter_change
        elif answer1021 in ["a", "b"]:
            print("Oops! The correct answer is 'Digging the dancing queen'. Better luck next time!")
        else:
            print(f"Invalid choice. No letters for you!")


    if airport_id == 1022:
        print("You get 1 shot. Try to hit the bullseye (score 10)!\n"
              "Press Enter to shoot!")
        answer1022 = random.randint(0, 10)
        input()
        print(f"You hit a {answer1022}!\n"
              f"So you get {answer1022} more letters!")
        letter_count += answer1022


    if airport_id == 1023:
        print("Have you ever watch movie Midsommar from Sweden?")
        print("A. Yes\nB. No")
        answer1023 = input("Enter your choice (A or B)\n").lower().strip()
        if answer1023 == "a":
            print("Here is 5 letters for the traumatic experience lol")
            letter_count += letter_change
        elif answer1023 == "b":
            print("Good, do not watch! You don't miss out anything! Let's move on!")
        else:
            print("Hey, there are only A and B to choose! No letters for you!")


    if airport_id == 1024:
        # computer choice
        choices1024 = ["rock", "scissors", "paper"]
        computer_choice = random.choice(choices1024)
        # player choice
        answer1024 = input("Enter your choice (rock, scissors, paper)\n").lower().strip()
        if answer1024 not in choices1024:
            print("Invalid choice. No letters for you!")
        else:
            print(f"You chose {answer1024}. We chose {computer_choice}.")
            if answer1024 == computer_choice:
                print("It's a draw! To the next destination!")
            elif (answer1024 == "rock" and computer_choice == "scissors") or \
                    (answer1024 == "scissors" and computer_choice == "paper") or \
                    (answer1024 == "paper" and computer_choice == "rock"):
                print("You win! You gain 10 letters!")
                letter_count += letter_change
            else:
                print("You lose! You lose 10 letters!")
                letter_count -= letter_change

    if airport_id == 1025:
        print("Do you know which was an important measurement unit proposed by a famous Swedish physicist?")
        print("A. ampere (electric current)\nB. degree celsius (temperature)\nC. kelvin (thermodynamic temperature)")

        answer1025 = input("Enter the correct choice (A, B, or C)\n").lower().strip()

        if answer1025 in ["a", "c"]:
            print("Incorrect!\n"
                  "It was degree celsius named after the Swedish physicist Anders Celsius (1701–1744).")
        elif answer1025 == "b":
            print("Correct!\n"
                  "Degree celsius named after the Swedish physicist Anders Celsius (1701–1744)\n"
                  "You got 5 letters!")
            letter_count += letter_change
        else:
            print("Invalid choice. No letters for you!")

    if airport_id == 1026:
        print("Did you know Swedish entrepreneur Alfred Nobel left most of his fortune to create the Nobel Prize?")
        print("Which of the following is NOT a Nobel Prize category?")
        print(f"A. Physics\nB. Mathematics\nC. Chemistry")

        answer1026 = input("Enter the correct choice (A, B, or C)\n").lower().strip()

        if answer1026 in ["a", "c"]:
            print("Sorry it's incorrect! The answer is Mathematics. You'll lose 5 letters!")
            letter_count += letter_change
        elif answer1026 == "b":
            print("Correct! You gain 5 letters!")
            letter_count += letter_change
        else:
            print("Invalid choice. Let's go to next destination!")

    # 1027
    # find a box

    if airport_id == 1027:
        print("Press Enter to open")
        input()
        print("You got 2 extra letters!")
        letter_count += letter_change

    # 1028
    # icehotel

    if airport_id == 1028:
        print("You come across the coolest ice hotel (pun totally intended)!")
        print("How about staying the night?\n"
              "Press Enter to check in!")
        input()
        print("It cost you 20 letters but it was so cooool (yes, another pun!)!")
        letter_count -= letter_change

    if airport_id == 1029:
        print("You are a bit hungry. How about some delicious Swedish meatballs at IKEA?")
        print("Press Enter to head over there and grab a bite!")
        input()
        print("It was yummy and you spent 15 letters for the food!")
        letter_count -= letter_change

    if airport_id == 1030:
        print("Meoooooooow!\n"
      "Is that a cat I see? 🐱")
        print("Do you want to pet it?")

        answer1030 = input("Type Yes or No\n").lower().strip()
        if answer1030 == "yes":
            print("You got bitten hoooooman!\n"
                  "The cat takes 10 letters and runs away!")
            letter_count -= letter_change
        elif answer1030 == "no":
            print("Boring! The cat rolls his eyes and run away!")
        else:
            print("Invalid choice. No letters for you!")

    if airport_id == 1031:
        print(f"Lose me once I'll come back stronger,\n"
              f"lose me twice I'll leave forever, what am I?")
        answer1031 = input("Type your guess here: ").lower().strip()

        if answer1031 == "tooth":
            print("Wow such a genius!\n"
                  "The elf gifts you 15 letters!")
            letter_count += letter_change
        else:
            print("The answer is 'Tooth'! But I guess that’s too tough for you - said the elf")
            print("He smirks and says, 'Good luck next time, genius!'")

    # 1032
    # envelope

    if airport_id == 1032:
        print("There's an envelope slipped under your feet!")
        print("Press Enter to open")
        input()
        print("Hey Santa,\n"
              "I hate Christmas. I mean A LOT!\n"
              "        -The Grinch")
        print("Well somebody is too grumpy! Let's continue your journey!")

    # 1033
    # mariah carey

    if airport_id == 1033:
        print("Who is she?")
        answer1028 = input("Type her name here: ").lower().strip()
        if answer1028 == "mariah carey":
            print("Very cultured, very demure! Here is 5 letters for you!")
            letter_count += letter_change
        else:
            print("OMG you don't know Mariah Carey? It's okay not everyone needs to know pop culture.")

    if airport_id == 1034:
        print("Fun fact: Dynamite was invented by Swedish chemist Alfred Nobel!")
        print("Hit Enter to see what's next...")
        input()
        print("Wait... Is that a stick of dynamite?!")
        print("Press Enter to make a quick escape!")
        input()
        print("Oh noooooo you drop a quarter of your letters on the way out! Let's continue and collect more letters!")
        letter_count -= (letter_count // letter_change)

    if airport_id == 1035:
        print("Whoa! Those reindeer are all over the place!")
        print("Oh no! You just got into a reindeer accident :(")
        print("Hit Enter to get back up...")
        input()
        print("Yikes! A reindeer just took 10 letters from your bag in this chaos! Let's move on!")
        letter_count -= letter_change

    if airport_id == 1036:
        print("A new friend invites you to visit his house in Iceland.\n"
              "Do you take off your shoes when entering the house?")
        answer1036 = input("Type here Yes or No to answer\n").lower().strip()
        if answer1036 == "yes":
            print("Good job!\n"
                  "In Icelandic culture, it's customary for guests to remove their shoes when entering a home.")
        elif answer1036 == "no":
            print("In Icelandic culture, it's customary for guests to remove their shoes when entering a home.")
            print("You have been taken away 5 letters!")
            letter_count -= letter_change
        else:
            print("Invalid choice.\n"
                  "But remember to take off your shoes when entering someone's home in Iceland!")


    if airport_id == 1037:
        print("More than 10% of Iceland is covered by glaciers\n"
              "And of course you just took an unexpected slide on one of them :(")
        print("Press Enter to pick yourself up")
        input()

        print("You just check your bag and find out you lost 10 letters!")
        letter_count -= letter_change

    if airport_id == 1038:
        print("In Icelandic folklore, trolls are a big deal - just like you, the greatest elf!\n"
              "You walk around and meet a troll!\n"
              "Do you want to chat with him?")
        answer1038 = input("Type here Yes or No to answer\n").lower().strip()
        if answer1038 == "yes":
            print("The troll is so nice and help you collect 10 more letters!")
            letter_count += letter_change
        elif answer1038 == "no":
            print("He looks upset and turn away. You hurt him a little bit 😔")
        else:
            print("Invalid choice. He doesn't know what you want to do and go away.")


    if airport_id == 1039:
        print("He wants to tell you a joke!")
        print("Press Enter to hear: ")
        input()
        print("Where does Christmas (25th Dec) come before Thanksgiving (fourth Thursday in November)?")
        answer1039 = input("Just give a guess here: ").lower().strip()
        print("The answer is IN DICTIONARY you silly!")
        print("Okay, sorry for the jokes, here is 5 letters for you - said the snowman")
        letter_count += letter_change

    if airport_id == 1040:
        print("🧙‍♂️ We’re curious! Which Harry Potter house do you belong to?")
        print("Your options are: Gryffindor, Hufflepuff, Ravenclaw or Slytherin.")
        answer1040 = input("Type your house here: ")
        answer1040_lower = answer1040.lower().strip()
        if answer1040_lower in ["gryffindor", "hufflepuff", "ravenclaw", "slytherin"]:
            print(f"20 points (or may we say letters) for {answer1040}!")
            letter_count += letter_change
        else:
            print(f"Hmmm... {answer1040}? Are you sure that's a real house? No points (or letters) for you!")

    if airport_id == 1041:
        print("🌟 Surprise! You’ve gained 10 letters for being the cutest elf! We love your energy!")
        letter_count += letter_change

    if airport_id == 1042:
        print("Time for a quick riddle! Get it right, nd you’ll get 5 letters!")
        print("What are two things you can never eat for breakfast?\n"
              "Type your answer below: ")
        answer1042_1st = input("First thing is: ").lower().strip()
        answer1042_2nd = input("Second thing is: ").lower().strip()
        if (answer1042_1st == "lunch" and answer1042_2nd == "dinner") or (
                answer1042_1st == "dinner" and answer1042_2nd == "lunch"):
            print("So smart! We hope you always eat well! You got 5 more letters!")
            letter_count += letter_change
        else:
            print("Not the answer we were looking for! They are 'LUNCH' and 'Dinner'.\n"
                  "No extra letter this time!")

    if airport_id == 1043:
        print("🐶🐱 The ultimate question: Are you a dog person or a cat person?")
        answer1043 = input("A. Dog person\n B. Cat person\n"
                           "Type A or B to answer\n").lower().strip()
        print("You know what? We love all pets here! Here are 10 letters just for sharing your thoughts!")
        letter_count += letter_change


    if airport_id == 1044:
        print("Yay! We have a new visitor in da town!")
        print("Looks like you were too busy sightseeing and dropped 5 letters!")
        letter_count -= letter_change
        print("Take your time and explore the city 'cause you've lost the letters anyway!")

    if airport_id == 1045:
        print("Quick quiz! Major General Sir Nils Oval III is...")
        answer1045 = input("A. a reindeer\nB. a polar bear\nC. a penguin\n"
                           "Answer by typing A, B or C\n").lower().strip()
        if answer1045 == "c":
            letter_count += letter_change
            print("Bingo! 🐧 You got 10 letters")
        elif answer1045 in ["a", "b"]:
            letter_count -= letter_change
            print("Oops incorrect! You’ve lost 10 letters.")
        else:
            letter_count -= letter_change
            print("Oops! You’ve lost 10 letters.")
        print(
            "Major General Sir Nils Oval III, Baron of the Bouvet Islands, is a king penguin who resides in Edingurgh Zoo, Scotland.\n"
            "He is the mascot and colonel-in-chief of the Norwegian King's Guard.")

    if airport_id == 1046:
        print("Quick geography quiz! Do you know what the second largest city in Norway is?")
        answer1046 = input("Type your answer here: ").lower().strip()
        if answer1046 == "bergen":
            print("That’s right, you're standing in it! You just earned 5 letters!")
            letter_count += letter_change
        else:
            print("Hey you're literally here in Bergen! The reindeer is confused, and you lost 10 letters for that!")
            letter_count -= letter_change

    if airport_id == 1047:
        print("🐣 Here’s a classic brain teaser: Which came first, the chicken or the egg?")
        answer1047 = input("Type your answer here: ").lower().strip()
        print("Just kidding! I don't really care about the answer!")
        print("Here is 5 letters because you deserve them. See you later!")
        letter_count += letter_change

    if airport_id == 1048:
        print("Do you know which type of sushi comes from Norway?\n"
              "A. Salmon\nB. Tuna\nC. Shrimp")
        answer1048 = input("Type A, B or C to answer\n").lower().strip()
        if answer1048 == "a":
            letter_count += letter_change
            print("Good job! You got 10 letters")
        elif answer1048 in ["b", "c"]:
            letter_count -= letter_change
            print("Wrong! You lost 10 letters")
        print("It's Salmon sushi. The Norwegians invented this dish back in the 1980s.")

    if airport_id == 1049:
        print("Hmm...")
        print("Hmm...")
        print("Hmm...")
        print("Hmm...")
        print("Press any key to continue")
        input()
        print("You're still here?")
        print("There's nothing in this airport! Go ahead! Bye bye!")

    if airport_id == 1050:
        print("What travels the world while stuck in one spot?")
        answer1050 = input("Type your guess here: ").lower().strip()
        if answer1050 in ["stamp", "a stamp", "the stamp", "stamps", "the stamps"]:
            print("Brilliant! You are so smart! You got 10 more letters!")
            letter_count += letter_change
        else:
            print("It's the stamps!")
            print("You lost 5 letters")
            letter_count -= letter_change

    if airport_id == 1051:
        print("Ooooooops! You just stepped on a LEGO block! That's must be so painful!\n"
              "You lost 5 letters to call an ambulance and go to the hospital!")
        letter_count -= letter_change
        print("Just so you know, you’re in Denmark, the land where LEGOs were born!")

    if airport_id == 1052:
        print("At this airport we have a question for you!")
        print("Which one is the highest mountain in Denmark?\n"
              "A.Aarhus\nB.Bergen\nC.Thisted")
        answer1052 = input("Type A, B or C to answer\n").lower().strip()
        print("Haha! Nice try, but Denmark has no mountains! Just lots of flat land and delicious pastries!")
        print("Let's continue your journey!")

    if airport_id == 1053:
        sql_for_reindeer_2003 = f"SELECT letter_change_reindeer from reindeer where reindeer_id = 2003"
        cursor.execute(sql_for_reindeer_2003)
        letter_change_reindeer = cursor.fetchone()
        print("You can't resist the famous Danish cookies!\n"
              "You take a bite... and those cookies cost you 10 letters!")
        letter_count -= letter_change
        if reindeer_id == 2003:
            print("Oh wait, look who it is! Cupid has graced us with his adorable presence! 💘")
            print(
                "Did you know Denmark was the first country to legalise same-sex unions in 1989? Love truly has no bounds!")
            print("Thanks to Cupid, you’ll earn 20 more letters in celebration of love!")
            letter_count += letter_change_reindeer

    if airport_id == 1054:
        print("What do you actually find at the end of every rainbow?")
        answer1054 = input("Type your answer here: ").lower().strip()
        if answer1054 == "w" or answer1054 == "letter w":
            print("Brilliant! You got 5 letters.")
            letter_count += letter_change
        else:
            print("It's the letter W! You lost 5 letters.")
            letter_count -= letter_change

    if airport_id == 1055:
        print(f"Whoops! Your reindeer spotted a squirrel and took off like a rocket!\n"
              f"You lost 5 of your letters along the way!")
        letter_count -= letter_change

    if airport_id == 1056:
        print("This airport is on maintenance, sorry. Keep continuing your journey!")

    if airport_id == 1057:
        print("Is Cinderella a story a story by Danish writer Hans Christian Andersen?")
        answer1057 = input("Type here Yes or No to answer: ").lower().strip()
        if answer1057 == "no":
            print("That's right! Cinderella is a story by the Brothers Grimm.\n"
                  "Hans' notable works includes The Little Mermaid and Snow White")
            letter_count += letter_change
        elif answer1057 == "yes":
            print("Wrong! Cinderella is indeed a story by the Brothers Grimm. You lost 10 letters.")
            letter_count -= letter_change
        else:
            print("Cinderella is indeed a story by the Brothers Grimm. You lost 10 letters.")
            letter_count -= letter_change

    if airport_id == 1058:
        answer1058 = input("Fill in the blank: Finland has Sisu, and Denmark has...").lower().strip()
        if answer1058 == "hygge":
            print("Correct! You've gained 10 more letters")
            letter_count += letter_change
        else:
            print("Incorrect! You've lost 10 letters")
            letter_count -= letter_change
        print("Hygge is a word in Danish that describes a cozy, contented mood evoked by comfort and conviviality.")

    if airport_id == 1059:
        print("Where is an ocean with no water?")
        answer1059 = input("Type your guess here: ").lower().strip()
        if answer1059 == "map" or answer1059 == "the map" or answer1059 == "on the map" or answer1059 == "in the map":
            print("Brilliant! You are so smart! You got 10 more letters!")
            letter_count += letter_change
        else:
            print("It's on the map!")
            print("You lost 5 letters.")
            letter_count -= letter_change



    # cập nhật letter_count
    update_letter_count(player_id,letter_count)
    print(f"Currently, you have {letter_count} letters.")

# players go through 10 first airport
for i in range(56):
    current_airport = airport_direction()
    airport_quiz(current_airport)
    check_the_grinch(current_airport)
    print("----------------------------------------------------------------------------------------------------------")

#print the script that the map was lost
map_lost_script = ("Oh no you've just dropped the map and you can't see the next airport that you are going through!\n"
                   "From now on you can only go LEFT or RIGHT until you meet Santa again!")
print(map_lost_script)

#random 2 airports next to the goal
sql19 = f"select airport_id from airport where is_finished = '0'"
cursor.execute(sql19)
airport_id_tuples = cursor.fetchall()
airport_id_list = [item[0] for item in airport_id_tuples]
airport_id_list.remove(1060)
airport_n_2 = random.choice(airport_id_list)
airport_id_list.remove(airport_n_2)
airport_n_1 = random.choice(airport_id_list)

#player go through 2 airports next to the goal
print("Which way do you want to go next?")
user_random_choice = input("Type L for LEFT or R for RIGHT: ").lower().strip()
while True:
    if user_random_choice == "l" or user_random_choice == "r":
        airport_quiz(airport_n_2)
        break
    else:
        user_random_choice = input("Invalid choice! Type L for LEFT or R for RIGHT: ")

update_current_airport(player_id, airport_n_2)

print("---------------------------------------------------------------------------------------------------------------")

print("Which way do you want to go next?")
user_random_choice = input("Type L for LEFT or R for RIGHT: ").lower().strip()
while True:
    if user_random_choice == "l" or user_random_choice == "r":
        airport_quiz(airport_n_1)
        break
    else:
        user_random_choice = input("Invalid choice! Type L for LEFT or R for RIGHT: ").lower().strip()
update_current_airport(player_id, airport_n_1)

print("---------------------------------------------------------------------------------------------------------------")

#player reach the goal
rova_script= ("✨ You've arrived at Rovaniemi, the magical home of Santa Claus! ✨\n"
              "The air is filled with laughter, music, and the delightful scent of cinnamon!\n"
              "Santa’s waiting for you, but wait... did you bring the letters?")
print(rova_script)
print("Let’s make Christmas magical! Press any key to give your letters to Santa Claus!")
input()
update_current_airport(player_id, 1060)

#lay letter count tron database
final_letter_count = get_letter_count(player_id)

if int(final_letter_count) >= 100:
    result = "Win"
else:
    result = "Lose"
sql20 = f"UPDATE player SET result = '{result}' WHERE player_id = '{player_id}'"
cursor.execute(sql20)
win_goal_intro = (f"You did it!\n"
                  f"You delivered the total of {final_letter_count} letters to Santa!\n"
                  f"Christmas is saved, and Santa couldn’t be prouder of his fastest elf!\n"
                  f"Thank you for playing ELF DELIVERY DASH, and have a great holiday!")
lose_goal_intro = (f"Oh no...\n"
                   f"You delivered the total of {final_letter_count} letters to Santa.\n"
                   f"The Grinch was just a little too sneaky, and a few letters slipped away.\n"
                   f"But Christmas isn’t over yet! There’s still time to try again.\n"
                   f"Santa believes in you, and next time, let's bring all the letters to him!")

if result == "Win":
    print(win_goal_intro)
else:
    print(lose_goal_intro)