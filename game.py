import cmd 
import textwrap 
import sys 
import os 
import time 
import random 


screen_width = 100


#### Player Setup ####
class Player():

    def __init__(self):

        self.name = ""
        self.role = ""
        self.health_points = 0
        self.attack_points = 0
        self.magic_points = 0
        self.game_over = False

myPlayer = Player()


#### Title Screen ####

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()#####
    while option.lower() not in ['play' , 'help' , 'quit']:
        print("Please enter a valid command")
        if option.lower() == ("play"):
            setup_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('clear')
    print('###########################################################')
    print('         _______ _       _______ _______ _______ ______') 
    print('|\     /(  ____ ( \     (  ____ (  ___  (       (  ____ \ ')
    print('| )   ( | (    \| (     | (    \| (   ) | () () | (    \/')
    print('| | _ | | (__   | |     | |     | |   | | || || | (__    ')
    print('| |( )| |  __)  | |     | |     | |   | | |(_)| |  __)   ')
    print('| || || | (     | |     | |     | |   | | |   | | (      ')
    print('| () () | (____/| (____/| (____/| (___) | )   ( | (____/\ ')
    print('(_______(_______(_______(_______(_______|/     \(_______/')
    print('###########################################################')
    print('                        - PLAY -                           ')
    print('                        - HELP -                           ')
    print('                        - QUIT -                           ')
    title_screen_selections()

def help_menu():
    os.system('clear')
    print('###########################################################')
    print('         _______ _       _______ _______ _______ ______') 
    print('|\     /(  ____ ( \     (  ____ (  ___  (       (  ____ \ ')
    print('| )   ( | (    \| (     | (    \| (   ) | () () | (    \/')
    print('| | _ | | (__   | |     | |     | |   | | || || | (__    ')
    print('| |( )| |  __)  | |     | |     | |   | | |(_)| |  __)   ')
    print('| || || | (     | |     | |     | |   | | |   | | (      ')
    print('| () () | (____/| (____/| (____/| (___) | )   ( | (____/\ ')
    print('(_______(_______(_______(_______(_______|/     \(_______/')
    print('###########################################################')
    print('         - Use up, down, left, right to move -')
    print('         - Type your commands to do them -')
    print('         - Use "look" to inspect something -')
    print('         - Good luck and have fun!!! -')



def enter_town():
    s1 = "You are at the entrance to town \n"
    s2 ="You get greeted by the civilians\n"
    # print(f"Your health is now {myPlayer.health_points}")
    s3 = "They offer you to either follow them or take a piece of cake\n"
    s4 = "What would you like to do? Take the cake or Follow the people\n"
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)   
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    option = input("> ")
    if "cake" in option:
        takes_cake()
    elif "follow" in option:
        follow_people()
        

def takes_cake():
    myPlayer.health_points += 10
    print("You gained 10 hp")
    print(f"Health: {myPlayer.health_points}")
    print("Now the people ask you to follow them.\n")
    print("But you're distracted by a man holding a chest.\n")
    print("Do you follow the people or go to the man?")
    option = input("> ")
    if "follow" in option:
        follow_people()
    elif "go" in option:
        go_to_man()

def follow_people():
    myPlayer.health_points = 0
    print("The locals jumped you and took everything you have.")
    print(f"Health: {myPlayer.health_points}")
    game_over()

def go_to_man():
        myPlayer.magic_points += 100
        print("He gave you a potion that boosts your MAGIC POWER!!!\n")
        print(f"Your magic level is now {myPlayer.magic_points}")

def fighting_lessons():
    pass

def town_two():
    pass

def game_over():
        print(f"Thank you for playing {myPlayer.name}.")
        ask_to_play_again()

def ask_to_play_again():
        decision = input("Do you want to play again? (yes/no): ").lower()
        if decision == "yes":
            restart_game()
        elif decision == "no":
            print(f"Thank you for playing! Goodbye, {myPlayer.name}. You wuss")
        else:
            print("Invalid command. Please answer with 'yes' or 'no'.")
            ask_to_play_again()

def restart_game():
        print("Restarting the game...\n")
        title_screen()


    


    
 
def main_game_loop():
        while myPlayer.game_over is False:
            enter_town()
def setup_game():
    os.system('clear')

    q1 = "Hello, what's your name?\n"
    for character in q1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

    q2 = "What role are you?\n"
    for character in q2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_role = input("> ")
    valid_roles = ["warrior", "mage", "rogue", "priest", "hunter"]
    while player_role.lower() not in valid_roles:
        print("Not a valid role")
        player_role = input("> ")
    if player_role.lower() in valid_roles:
        print("You are now a " + player_role + "!\n")
        myPlayer.role = player_role
    # import ipdb; ipdb.set_trace()
    
    if myPlayer.role == 'warrior':
        myPlayer.health_points = 300
        myPlayer.attack_points = 250
        myPlayer.magic_points = 0
    elif myPlayer.role == 'mage':
        myPlayer.health_points = 150
        myPlayer.attack_points = 100
        myPlayer.magic_points = 200
    elif myPlayer.role == 'rogue':
        myPlayer.health_points = 100
        myPlayer.attack_points = 300
        myPlayer.magic_points = 150
    elif myPlayer.role == 'priest':
        myPlayer.health_points = 150
        myPlayer.attack_points = 150
        myPlayer.magic_points = 150
    elif myPlayer.role == 'hunter':
        myPlayer.health_points =200
        myPlayer.attack_points = 150
        myPlayer.magic_points = 100

    

    q3 = "Welcome, " + player_name + " the " + player_role + ".\n"
    for character in q3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    # player_name = input(">")
    # myPlayer.name = player_name

    speech1 = "Welcome to this fantasy world!\n"
    speech2 = "I hope its greets you well!\n"
    speech3 = "Just make sure you don't get too lost...!\n"
    speech4 = "HEHEHEHEHEH.....\n"
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0)   
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0)

    os.system("clear")
    print("##########################")
    print("#    Let the game begin! #")
    print("##########################")
    main_game_loop()




title_screen()



