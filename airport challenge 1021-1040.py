
airport_id = None
letter_count = 0
is_finished = False
import random


#
#1021
#Dancing Queen lyrics

if airport_id == "1021":
    print(f"Welcome to Stockholm-Arlanda Airport!")
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
        letter_count += 5
    elif answer1021 in ["a", "b"]:
        print("Oops! The correct answer is 'Digging the dancing queen'. Better luck next time!")
    else:
        print(f"Invalid choice. No letters for you!")
    

#1022
#archery game

if airport_id == "1022":
    print("Welcome to the Archery Game in Gothenburg-Landvetter Airport!")
    print("You get 1 shot. Try to hit the bullseye (score 10)!\n"
          "Press Enter to shoot!")
    answer1022 = random.randint(0, 10)
    input()
    print(f"You hit a {answer1022}!\n"
          f"So you get {answer1022} letters!")
    letter_count += answer1022

#1023
#Midsommar

if airport_id == "1023":
    print("You arrive at Stockholm-Bromma Airport!")
    print("Have you ever watch movie Midsommar from Sweden?")
    print("A. Yes\nB. No")
    answer1023 = input("Enter your choice (A or B): ").lower().strip()
    if answer1023 == "a":
        print("Here 5 letters for the traumatic experience hohoho!")
        letter_count += 5
    elif answer1023 == "b":
        print("Good, do not watch! You don't miss out anything! Let's move on!")
    else:
        print("Hey, there are only A and B to choose! No letters for you!")


#1024
#rock, scissors, paper

if airport_id == "1024":
    print("You are at Gothenburg City Airport. Let's play Rock, Scissors, Paper game!")
    #computer choice
    choices1024 = ["rock", "scissors", "paper"]
    computer_choice = random.choice(choices1024)
    #your choice
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
            letter_count += 5
        else:
            print("You lose! You lose 10 letters!")
            letter_count -= 10

#1025
#celsius

if airport_id == "1025":
    print("You arrive at Kallax airport, Swenden!")
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
        letter_count += 5
    else:
        print("Invalid choice. No letters for you!")
    

#1026
#nobel

if airport_id == "1026":
    print("Welcome to Nobel Prize Trivia at Goteborg Landvetter Airport!")
    print("Swedish entrepreneur Alfred Nobel left the majority of this fortune to the establishment of Nobel Prize.")
    print("Which of the following is NOT a Nobel Prize category?")
    print(f"A. Physics\nB. Mathematics\nC. Chemistry")

    answer1026 = input("Enter the correct choice (A, B, or C): ").lower().strip()

    if answer1026 == "a" or answer1026 == "c":
        print("Sorry it's incorrect! The answer is Mathematics.")
    elif answer1026 == "b":
        print("Correct! You gain 5 letters!")
        letter_count += 5
    else:
        print("Invalid choice. Let's go to next destination!")

#1027
#find a box

if airport_id == "1027":
    print("Yayyyy you found a mystery box in Malmo Airport!")
    print("Press Enter to open")
    input()
    print("You got 10 extra letters!")
    letter_count += 10

#1028
#icehotel

if airport_id == "1028":
    print("You just arrive at Umea Airport and you are so tired :(")
    print("You see the coolest ice hotel (pun intended)")
    print("Let's stay for a night!\n"
          "Press Enter to pay")
    input()
    print("It costed you 20 letters but it was so cooool (another pun lol)")
    letter_count -= 20


#1029
#ikea meatballs

if airport_id == "1029":
    print("Welcome to Skelleftea Airport, Sweden!")
    print("You are a bit hungry. How about some Swedish meatballs at IKEA?")
    print("Press Enter to go to IKEA")
    input()
    print("It was yummy and you exchanged 15 letters for the food!")
    letter_count -= 15

#1030
#catty cat

if airport_id == "1030":
    print("You arrived at Skelleftea Airport.")
    print("Meoooooooow\n"
          "Is that a cat?")
    print("Do you want to pet it?")

    answer1030 = input("Type Yes or No: ").lower().strip()
    if answer1030 == "yes":
        print("You got bitten hoooooman!\n"
              "The cat takes 10 letters and runs away!")
        letter_count -= 10
    elif answer1030 == "no":
        print("Boring! The cat rolls his eyes and run away!")
    else:
        print("Invalid choice. No letters for you!")

#1031
#riddle

if airport_id == "1031":
    print("At Ostersund Airport an elf appears and challenges you with a riddle!")
    print(f"Lose me once I'll come back stronger,\n"
          f"lose me twice I'll leave forever, what am I?")
    answer1031 = input("Type your guess here: ").lower().strip()

    if answer1031 == "tooth":
        print("Wow you are really smart!\n"
              "The elf gives you 15 letters!")
    else:
        print("Sorry it's incorrect.\n"
              "The answer is 'Tooth'!")
        print("The elf just laugh and go away.")

#1032
#envelope

if airport_id == "1032":
    print("Welcome to Reykjavik Domestic Airport!")
    print("There's an envelope slipped under your feet!")
    print("Press Enter to open")
    input()
    print("Dear Santa,\n"
          "I hate Christmas.\n"
          "      -The Grinch")
    print("Oh that's so weird. Let's continue our journey!")


#1033
#mariah carey

if airport_id == "1033":
    print("At Vaxjo Airport you witness the queen of Christmas songs defrosting again this year.")
    print("Who is she?")
    answer1028 = input("Type her name here: ").lower().strip()
    if answer1028 == "mariah carey":
        print("Very cultured, very demure! Here is 5 letters for you!")
        letter_count += 5
    else:
        print("OMG you don't know Mariah Carey? It's okay let's continue the journey!")

#1034
#dynamite

if airport_id == "1034":
    print("You arrive at Kalmar Airport")
    print("Do you know that dynamite was invented by Swedish chemist Alfred Nobel?")
    print("Press Enter to continue")
    input()
    print("You come across a stick of dynamite")
    print("Let's press Enter to run as fast as possible!")
    input()
    print("Oh noooooo you drop a quarter of your letters on the way :(. Let's continue and collect more letters!")
    letter_count -= (letter_count//4)

#1035
#reindeer accident

if airport_id == "1035":
    print("You arrive at Keflavik International Airport!")
    print("You see that the reindeers are roaming around.")
    print("Oh noooo you get into a reindeer accident :(")
    print("Press Enter to continue")
    input()
    print("You have lost 10 letters! Let's move on!")
    letter_count -= 10


#1036
#icelandic home

if airport_id == "1036":
    print("Welcome to Kalmar Airport!")
    print("A new friend invites you to visit his house in Iceland.\n"
          "Do you take off your shoes when entering the house?")
    answer1036 = input("Type here Yes or No to answer: ").lower().strip()
    if answer1036 == "yes":
        print("Good job!\n"
              "It is an important part of Icelandic culture that guests always take off their shoes when entering someone's home.")
    elif answer1036 == "no":
        print("It is an important part of Icelandic culture that guests always take off their shoes when entering someone's home.")
        print("You have been taken away 5 letters!")
        letter_count -= 5
    else:
        print("Invalid choice.\n"
              "But remember to take off your shoes when entering someone's home in Iceland!")



#1037
#glacier
if airport_id == "1037":
    print("Welcome to Akureyri Airport, Iceland!")
    print("More than 10% of Iceland is covered by glaciers\n"
          "And of course you just slipped on them :(")
    print("Press Enter to get up")
    input()

    print("You just check and find out you lost 10 letters!")
    letter_count -= 10

#1038
#troll

if airport_id == "1038":
    print("Welcome to Egilsstadir Airport, Iceland!")
    print("Troll is a big part of Icelandic Folklore, along with elves which you actually are!")
    print("You walk around and meet a troll!")
    print("Do you want to talk to him?")
    answer1038 = input("Type here Yes or No to answer: ").lower().strip()
    if answer1038 == "yes":
        print("The troll is so nice and help you collect 10 more letters!")
        letter_count += 10
    elif answer1038 == "no":
        print("He looks upset and turn away. You hurt him a little bit :(")
    else:
        print("Invalid choice. He doesn't know what you want to do and go away.")

#1039
#snowman joke

if airport_id == "1039":
    print("Welcome to Isafjordur Airport and a snowman is waiting for you!")
    print("He wants to tell you a joke!")
    print("Press Enter to continue")
    input()
    print("Where does Christmas (25th Dec) come before Thanksgiving (fourth Thursday in November)?")
    answer1039 = input("Just give a guess here: ").lower().strip()
    print("The answer is IN DICTIONARY hohoho")
    print("Sorry for the jokes, here is 5 letters for you - said the snowman")
    letter_count += 5

#1040
#harry potter

if airport_id == "1040":
    print("Welcome to Husavik Airport!")
    print("We want to know what is your Harry Potter house!")
    print("Harry Potter House are: Gryffindor, Hufflepuff, Ravenclaw, Slytherin.")
    answer1040 = input("Type your house here: ")
    answer1040_lower = answer1040.lower().strip()
    if answer1040_lower in ["gryffindor", "hufflepuff", "ravenclaw", "slytherin"]:
        print(f"20 points (or may we say letters) for {answer1040}!")
        letter_count += 20
    else:
        print(f"Hmmm is {answer1040} a made up house? No points for you!")

