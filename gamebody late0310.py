import mysql.connector
import random

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='elfdeliverydash',
    user='root',
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
        reindeer_choice = int(input("Invalid choice. 1.Rudolph, 2.Vixen, 3.Cupid (1/2/3) "))

# cập nhật player_name và reindeer_id vào bảng player
sql2 = f"INSERT INTO player(player_name, reindeer_id) VALUES ('{player_name}',{reindeer_choice});"
cursor = connection.cursor()
cursor.execute(sql2)

grinch_challenge = random.randint(1, 6)
grinch_airport = random.randint(1002, 1059)

# cập nhật grinch_challenge_id vào airport id đó)
sql3 = f"UPDATE airport SET grinch_challenge_id = {grinch_challenge} WHERE airport_id ={grinch_airport}"
cursor = connection.cursor()
cursor.execute(sql3)

helsinki_welcome = " "
print(helsinki_welcome)
current_airport = 1001
sql3 = f"UPDATE player SET letter_count = (SELECT letter_change FROM airport WHERE airport_id = 1001) WHERE player_name = '{player_name}'"

def airport_direction():
    # tao ra airport_list
    sql15 = f"select airport_id from airport where is_finished = '0'"
    cursor.execute(sql15)
    airport_id_tuples = cursor.fetchall()
    airport_id_list = [item[0] for item in airport_id_tuples]
    airport_id_list.remove(1001)
    airport_id_list.remove(1060)
    print(airport_id_list)

    next_airport_left = random.choice(airport_id_list)
    sql16 = f"select airport_name from airport where airport_id = {next_airport_left}"
    cursor.execute(sql16)
    next_airport_left_tuple = cursor.fetchall()
    next_airport_left_name = next_airport_left_tuple[0][0]
    airport_id_list.remove(next_airport_left)
    next_airport_right = random.choice(airport_id_list)
    sql17 = f"select airport_name from airport where airport_id = {next_airport_right}"
    cursor.execute(sql17)
    next_airport_right_tuple = cursor.fetchall()
    next_airport_right_name = next_airport_right_tuple[0][0]

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
    # cập nhật current airport vào bảng player
    sql18 = f"UPDATE player SET current_airport = '{current_airport}' WHERE player_name = '{player_name}'"
    cursor.execute(sql18)
    return current_airport

def airport_greeting(airport_id):
    sql19 = f"SELECT greeting FROM airport WHERE airport_id = {airport_id}"
    cursor.execute(sql19)
    greeting_tuple = cursor.fetchall()
    greeting = greeting_tuple[0][0]
    return greeting

def airport_quiz(airport_id):
    # print airport welcome
    print(airport_greeting(airport_id))

    #get the value of letter_change
    sql20 = f"SELECT letter_change FROM airport_id WHERE airport_id = {airport_id}"
    cursor.execute(sql20)
    letter_change_tuple = cursor.fetchall()
    letter_change = int(letter_change_tuple[0][0])

    #get the value of letter_count of player
    sql21 = f"SELECT letter_count FROM player WHERE player_name = '{player_name}'"
    cursor.execute(sql21)
    letter_count_tuple = cursor.fetchall()
    letter_count = int(letter_count_tuple[0][0])

    if airport_id == "1021":
        print("Do you know the famous band ABBA is from Sweden?\n"
              "Let's fill in the lyrics of their song Dancing Queen to gain 5 letters!")
        print("You can dance, you can jive\n"
              "Having the time of your life\n"
              "Ooh, see that girl, watch that scene\n"
              "_____________ the dancing queen")

        print("Choose the correct lyrics from the following options:")
        print("1. Dancing\n2. Singing\n3. Digging")

        answer1021 = input("Enter the correct choice (A, B, or C): ").lower().strip()

        if answer1021 == "c":
            print("Correct! You win 5 letters!")
            letter_count += letter_change
        elif answer1021 in ["a", "b"]:
            print("Oops! The correct answer is 'Digging the dancing queen'. Better luck next time!")
        else:
            print(f"Invalid choice. No letters for you!")

    # 1022
    # archery game

    if airport_id == "1022":
        print("You get 1 shot. Try to hit the bullseye (score 10)!\n"
              "Press Enter to shoot!")
        answer1022 = random.randint(0, 10)
        input()
        print(f"You hit a {answer1022}!\n"
              f"So you get {answer1022} letters!")
        letter_count += answer1022

    # 1023
    # Midsommar

    if airport_id == "1023":
        print("Have you ever watch movie Midsommar from Sweden?")
        print("A. Yes\nB. No")
        answer1023 = input("Enter your choice (A or B): ").lower().strip()
        if answer1023 == "a":
            print("Here 5 letters for the traumatic experience hohoho!")
            letter_count += letter_change
        elif answer1023 == "b":
            print("Good, do not watch! You don't miss out anything! Let's move on!")
        else:
            print("Hey, there are only A and B to choose! No letters for you!")

    # 1024
    # rock, scissors, paper

    if airport_id == "1024":
        # computer choice
        choices1024 = ["rock", "scissors", "paper"]
        computer_choice = random.choice(choices1024)
        # your choice
        answer1024 = input("Enter your choice (rock, scissors, paper): ").lower().strip()
        if answer1024 not in choices1024:
            print("Invalid choice. No letters for you!")
        else:
            print(f"\nYou chose {answer1024}. The computer chose {computer_choice}.\n")
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

    # 1025
    # celsius

    if airport_id == "1025":
        print("Do you know which was an important measurement unit proposed by a famous Swedish physicist?")
        print("A. ampere (electric current)\nB. degree celsius (temperature)\nC. kelvin (thermodynamic emperature)")

        answer1025 = input("Enter the correct choice (A, B, or C): ").lower().strip()

        if answer1025 == "a" or answer1025 == "c":
            print("Incorrect!\n"
                  "It was degree celsius named after the Swedish physicist Anders Celsius (1701–1744)")
        elif answer1025 == "b":
            print("Correct!\n"
                  "Degree celsius named after the Swedish physicist Anders Celsius (1701–1744)\n"
                  "You got 5 letters!")
            letter_count += letter_change
        else:
            print("Invalid choice. No letters for you!")

    # 1026
    # nobel

    if airport_id == "1026":
        print(
            "Swedish entrepreneur Alfred Nobel left the majority of this fortune to the establishment of Nobel Prize.")
        print("Which of the following is NOT a Nobel Prize category?")
        print(f"A. Physics\nB. Mathematics\nC. Chemistry")

        answer1026 = input("Enter the correct choice (A, B, or C): ").lower().strip()

        if answer1026 == "a" or answer1026 == "c":
            print("Sorry it's incorrect! The answer is Mathematics.")
        elif answer1026 == "b":
            print("Correct! You gain 5 letters!")
            letter_count += letter_change
        else:
            print("Invalid choice. Let's go to next destination!")

    # 1027
    # find a box

    if airport_id == "1027":
        print("Press Enter to open")
        input()
        print("You got 10 extra letters!")
        letter_count += letter_change

    # 1028
    # icehotel

    if airport_id == "1028":
        print("You see the coolest ice hotel (pun intended)")
        print("Let's stay for a night!\n"
              "Press Enter to pay")
        input()
        print("It costed you 20 letters but it was so cooool (another pun lol)")
        letter_count -= letter_change

    # 1029
    # ikea meatballs

    if airport_id == "1029":
        print("You are a bit hungry. How about some Swedish meatballs at IKEA?")
        print("Press Enter to go to IKEA")
        input()
        print("It was yummy and you exchanged 15 letters for the food!")
        letter_count -= letter_change

    # 1030
    # catty cat

    if airport_id == "1030":
        print("Meoooooooow\n"
              "Is that a cat?")
        print("Do you want to pet it?")

        answer1030 = input("Type Yes or No: ").lower().strip()
        if answer1030 == "yes":
            print("You got bitten hoooooman!\n"
                  "The cat takes 10 letters and runs away!")
            letter_count -= letter_change
        elif answer1030 == "no":
            print("Boring! The cat rolls his eyes and run away!")
        else:
            print("Invalid choice. No letters for you!")

    # 1031
    # riddle

    if airport_id == "1031":
        print(f"Lose me once I'll come back stronger,\n"
              f"lose me twice I'll leave forever, what am I?")
        answer1031 = input("Type your guess here: ").lower().strip()

        if answer1031 == "tooth":
            print("Wow you are really smart!\n"
                  "The elf gives you 15 letters!")
            letter_count += letter_change
        else:
            print("Sorry it's incorrect.\n"
                  "The answer is 'Tooth'!")
            print("The elf just laugh and go away.")

    # 1032
    # envelope

    if airport_id == "1032":
        print("There's an envelope slipped under your feet!")
        print("Press Enter to open")
        input()
        print("Dear Santa,\n"
              "I hate Christmas.\n"
              "      -The Grinch")
        print("Oh that's so weird. Let's continue our journey!")

    # 1033
    # mariah carey

    if airport_id == "1033":
        print("Who is she?")
        answer1028 = input("Type her name here: ").lower().strip()
        if answer1028 == "mariah carey":
            print("Very cultured, very demure! Here is 5 letters for you!")
            letter_count += letter_change
        else:
            print("OMG you don't know Mariah Carey? It's okay let's continue the journey!")

    # 1034
    # dynamite

    if airport_id == "1034":
        print("Do you know that dynamite was invented by Swedish chemist Alfred Nobel?")
        print("Press Enter to continue")
        input()
        print("You come across a stick of dynamite")
        print("Let's press Enter to run as fast as possible!")
        input()
        print("Oh noooooo you drop a quarter of your letters on the way :(. Let's continue and collect more letters!")
        letter_count -= (letter_count // 4)

    # 1035
    # reindeer accident

    if airport_id == "1035":
        print("You see that the reindeers are roaming around.")
        print("Oh noooo you get into a reindeer accident :(")
        print("Press Enter to continue")
        input()
        print("You have lost 10 letters! Let's move on!")
        letter_count -= letter_change

    # 1036
    # icelandic home

    if airport_id == "1036":
        print("A new friend invites you to visit his house in Iceland.\n"
              "Do you take off your shoes when entering the house?")
        answer1036 = input("Type here Yes or No to answer: ").lower().strip()
        if answer1036 == "yes":
            print("Good job!\n"
                  "It is an important part of Icelandic culture that guests always take off their shoes when entering someone's home.")
        elif answer1036 == "no":
            print(
                "It is an important part of Icelandic culture that guests always take off their shoes when entering someone's home.")
            print("You have been taken away 5 letters!")
            letter_count -= letter_change
        else:
            print("Invalid choice.\n"
                  "But remember to take off your shoes when entering someone's home in Iceland!")

    # 1037
    # glacier
    if airport_id == "1037":
        print("More than 10% of Iceland is covered by glaciers\n"
              "And of course you just slipped on them :(")
        print("Press Enter to get up")
        input()

        print("You just check and find out you lost 10 letters!")
        letter_count -= letter_change

    # 1038
    # troll

    if airport_id == "1038":
        print("Troll is a big part of Icelandic Folklore, along with elves which you actually are!")
        print("You walk around and meet a troll!")
        print("Do you want to talk to him?")
        answer1038 = input("Type here Yes or No to answer: ").lower().strip()
        if answer1038 == "yes":
            print("The troll is so nice and help you collect 10 more letters!")
            letter_count += letter_change
        elif answer1038 == "no":
            print("He looks upset and turn away. You hurt him a little bit :(")
        else:
            print("Invalid choice. He doesn't know what you want to do and go away.")

    # 1039
    # snowman joke

    if airport_id == "1039":
        print("He wants to tell you a joke!")
        print("Press Enter to continue")
        input()
        print("Where does Christmas (25th Dec) come before Thanksgiving (fourth Thursday in November)?")
        answer1039 = input("Just give a guess here: ").lower().strip()
        print("The answer is IN DICTIONARY hohoho")
        print("Sorry for the jokes, here is 5 letters for you - said the snowman")
        letter_count += letter_change

    # 1040
    # harry potter

    if airport_id == "1040":
        print("We want to know what is your Harry Potter house!")
        print("Harry Potter House are: Gryffindor, Hufflepuff, Ravenclaw, Slytherin.")
        answer1040 = input("Type your house here: ")
        answer1040_lower = answer1040.lower().strip()
        if answer1040_lower in ["gryffindor", "hufflepuff", "ravenclaw", "slytherin"]:
            print(f"20 points (or may we say letters) for {answer1040}!")
            letter_count += letter_change
        else:
            print(f"Hmmm is {answer1040} a made up house? No points for you!")

    if airport_id == 1041:
        print("You got 10 letters.")
        letter_count += letter_change

    if airport_id == 1042:
        print("You have to answer a question. You will get 5 letters if correct!")
        print("What are two things you can never eat for breakfast? (the answers are sep")
        answer1042_1st = input("First thing is: ").lower().strip()
        answer1042_2nd = input("Second thing is: ").lower().strip()
        if (answer1042_1st == "lunch" and answer1042_2nd == "dinner") or (
                answer1042_1st == "dinner" and answer1042_2nd == "lunch"):
            print("That's right! You got 5 more letters!")
            letter_count += letter_change
        else:
            print("Incorrect! You got nothing!")

    if airport_id == 1043:
        print("I was wonder are you a cat person or a dog person?")
        answer1043 = input("A.dog person\n B.cat person (A/B)").lower().strip()
        print("It's okay, both dog and cat are greats. You get 10 more letters for answering my question!")
        letter_count += letter_change


    if airport_id == 1044:
        print("Yay, we have a new visitor")
        print("Unfortunately, you lost 5 letters ")
        letter_count -= letter_change
        print("Spend your time enjoy our city. Thank you!")

    if airport_id == 1045:
        print("In your opinion, Major General Sir Nils Oval III is...")
        answer1045 = input("A.a reindeer, B.a polar bear, C.a penguin (A/B/C)").lower().strip()
        if answer1045 == "c":
            letter_count += letter_change
            print("You got 10 letters")
        else:
            letter_count -= letter_change
            print("You lost 10 letters")
        print(
            "Major General Sir Nils Oval III, Baron of the Bouvet Islands, is a king penguin who resides in Edingurgh Zoo, Scotland.")
        print("He is the mascot and colonel-in-chief of the Norwegian King's Guard")

    if airport_id == 1046:
        answer1046 = input("Do you know what is the second largest city in Norway?").lower().strip()
        if answer1046 == "bergen":
            print("That's right! You got 5 letters")
            letter_count += letter_change
        else:
            print("Silly! It's here, Bergen. You lost 10 letters")
            letter_count -= letter_change

    if airport_id == 1047:
        answer1047 = input("Which came first, the chicken or the egg?").lower().strip()
        print("Just asking for fun :D. I don't care about the answer.")
        print("Here is your 5 letters. Bye bye")
        letter_count += letter_change

    if airport_id == 1048:
        print("Do you know which sushi comes from Norway?")
        answer1048 = input("A. Salmon, B. Tuna, C. Shrimp").lower().strip()
        if answer1048 == "a":
            letter_count += letter_change
            print("You got 10 letters")
        else:
            letter_count -= letter_change
            print("You lost 10 letters")
        print("The Norwegians invented this dish in the 1980s")

    if airport_id == 1049:
        print("Hmm")
        print("Hmm")
        print("Hmm")
        print("Hmm")
        print("You're still here?")
        print("There's nothing here! You go ahead! Bye!")

    if airport_id == 1050:
        answer1050 = input("What travels the world while stuck in one spot?").lower().strip()
        if answer1050 == "stamp" or "astamp" or "thestamp" or "stamps" or "thestamps":
            print("Brilliant! You are so smart! You got 10 more letters!")
            letter_count += letter_change
        else:
            print("It's the map!")
            print("You lost 5 letters")
            letter_count -= letter_change

    if airport_id == 1051:
        print("Oppps. You step on a LEGO block. That's hurt! You lost 5 letters to treat you leg!")
        letter_count -= letter_change
        print("Be careful! Cause you are in Denmark. The origin country of LEGO")


    if airport_id == 1052:
        print("I have a question for you!")
        print("Which one is the highest mountain in Denmark?")
        answer1052 = input("A.Aarhus, B.Bergen, C.Thisted").lower().strip()
        print("Nitwit. Denmark has no mountain!")
        print("Bye bye")

    if airport_id == 1053:
        print("The Danish cookies is so good, you taste them and you lose 10 letters for the cookies")
        letter_count -= letter_change

    if airport_id == 1054:
        answer1054 = input("What will you actually find at the end of every rainbow?").lower().strip()
        if answer1054 == "w":
            print("Brilliant! You got 5 letters.")
            letter_count += letter_change
        else:
            print("It's the letter W. You lost 5 letters.")
            letter_count -= letter_change

    if airport_id == 1055:
        print("Sorry, you lost 5 letters.")
        letter_count -= letter_change

    if airport_id == 1056:
        print("This airport is on maintenance, sorry. Keep countinuing your journey!")

    if airport_id == 1057:
        print("Is Cinderella a story a story by Danish Writer Hans Andersen?")
        answer1057 = input("Yes/No").lower().strip()
        if answer1057 == "no" or answer1057 == "n":
            print("That's right. It's Brothers Grimm's. Hans' notable works are The Little Mermaid and The Snow White")
        else:
            print("Wrong. It's Brothers Grimm's. You lost 10 letters.")
            letter_count -= letter_change

    if airport_id == 1058:
        answer1058 = ("Fill in the blank: Finland has Sisu, and Denmark has...").lower().strip()
        if answer1058 == "hygge":
            print("Yep, you got 10 more letters")
            letter_count += letter_change
        else:
            print("No, you lost 10 letters")
            letter_count -= letter_change
        print("Hygge is a word in Danish that describes a cozy, contented mood evoked by comfort and conviviality.")

    if airport_id == 1059:
        answer1059 = input("Where is an ocean with no water?").lower().strip()
        if answer1059 == "map" or "themap" or "onthemap" or "inthemap":
            print("Brilliant! You are so smart! You got 10 more letters!")
            letter_count += letter_change
        else:
            print("It's the map!")
            print("You lost 5 letters")
            letter_count -= letter_change

    if airport_id == 1060:
        print("You meet a poor girl selling matches on the street. What would you do?")
        answer1060 = input("A.Nothing. B.Buy all the matches. C. Give her food. (A/B/C)").lower().strip()
        if answer1060 == "b" or "c":
            print("You have such a warm heart. Here are your 10 letters.")
            letter_count += letter_change
        else:
            print("Don't be so cold. You lost 10 letters.")
            letter_count -= letter_change

    # cập nhật letter_count
    sql22 = f"UPDATE player SET letter_count = {letter_count} WHERE player_name = '{player_name}'"
    cursor.execute(sql22)
    print(f"Currently, you have {letter_count} letters.")
