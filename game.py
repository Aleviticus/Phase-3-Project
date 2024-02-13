
# class Warrior:

#     def __init__(self, name, hp, attack_points, magic_points, status_effect):
#         self.name = name
#         self.hp = hp
#         self.attack_points = attack_points
#         self.magic_points = magic_points 
#         self.status_effect = status_effect

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, name):
#         if type(name) == str:
#             self._name = name
#         else:
#             raise Exception("Warrior name must be a string")
        
#     @property
#     def hp(self):
#         return self._hp
    
#     @hp.setter
#     def hp(self, hp):
#         if type(hp) == int:
#             self._hp = hp
#         else:
#             raise Exception("HP must be an Integer")
        
#     @property
#     def attack_points(self):
#         return self._attack_points
    
#     @attack_points.setter
#     def attack_points(self, attack_points):
#         if type(attack_points) == int:
#             self._attack_points = attack_points
#         else:
#             raise Exception("Attack Points must be an Integer")
        
#     @property
#     def magic_points(self):
#         return self._magic_points
    
#     @magic_points.setter
#     def magic_points(self, magic_points):
#         if type(magic_points) == int:
#             self._magic_points = magic_points
#         else:
#             raise Exception("Magic point was not and Integer")


#     @property
#     def status_effect(self):
#         return self._status_effect
    
#     @status_effect.setter
#     def status_effect(self, status_effect):
#         if type(status_effect) == int:
#             self._status_effect = status_effect
#         else:
#             raise Exception("Status points was not an Integer")

import cmd 
import textwrap 
import sys 
import os 
import time 
import random 

screen_width = 100


#### Player Setup ####
class Rogue():

    def __init__(self):
        self.name = "Jaeem"
        self.role = Rogue
        self.health_points = 100
        self.attack_points = 250
        self.magic_points = 10
        self.location = 'a1'
        self.game_over = False
myPlayer = Rogue()


#### Title Screen ####

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
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


ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east' 

solved_places = { 'a1': False, 'a2': False, 'a3': False, 'a4': False,
                  'b1': False, 'b2': False, 'b3': False, 'b4': False,
                  'c1': False, 'c2': False, 'c3': False, 'c4': False,
                }

zonemap = {
    'a1': {
        ZONENAME: 'Town Entrance',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b1',
        LEFT: '',
        RIGHT:'a2',
    },
    'a2': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3',
    },
    'a3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4',
    },
    'a4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: '',
    },
    'b1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a1',
        DOWN: 'c1',
        LEFT: '',
        RIGHT: 'b2',
    },
    'b2': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',
    },
    'b3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a3',
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: 'b4',
    },
    'b4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a4',
        DOWN: 'c4',
        LEFT: 'b3',
        RIGHT: '',
    },
    'c1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'b1',
        DOWN: '',
        LEFT: '',
        RIGHT: 'c2',
    },
    'c2': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'b2',
        DOWN: '',
        LEFT: 'c1',
        RIGHT: 'c3',
    },
    'c3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'b3',
        DOWN: '',
        LEFT: 'c2',
        RIGHT: 'c4',
    },
    'c4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'b4',
        DOWN: '',
        LEFT: 'c3',
        RIGHT: '',
    }
}

#### Game Interactivity ####
def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('#' + myPlayer.location.upper() + '#')
    print('#' + zonemap[myPlayer.location][DESCRIPTION] + '#')
    print('\n' + ('#' * (4 + len(myPlayer.location))))

def prompt():
    print("What would you like to do?")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again.\n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'intersact', 'look']:
        player_examine(action.lower())

def player_move(myAction):
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
    elif dest in [ 'down', 'south' ]:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)


def movement_handler(destination):
    print("\n" + "You have moved to the" + destination + ".")
    myPlayer.location = destination
    print_location()

def player_examine(action):
    if zonemap[myPlayer.location][SOLVED] == True:
        print("You have already exhausted this zone.")
    else:
        print("Trigger puzzle here")

#### Game Functionality ####
def main_game_loop():
    while myPlayer.game_over is False:
        prompt()

def setup_game():
    os.system('clear')

    q1 = "Hello, what's your name?\n"
    for character in q1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_name = input("> ")
    myPlayer.name = player_name

    q2 = "What role are you?\n"
    for character in q2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_role = input("> ")
    valid_roles = ["warrior", "mage", "rogue", "priest", "hunter"]
    if player_role.lower() in valid_roles:
        print("You are now a " + player_role + "!\n")
        myPlayer.role = player_role
    

    q3 = "Welcome, " + player_name + " the " + player_role
    for character in q3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input(">")
    myPlayer.name = player_name

    speech1 = "Welcome to this fantasy world!\n"
    speech2 = "I hope its greets you well!\n"
    speech3 = "Just make sure you don't get too lost...!\n"
    speech4 = "HEHEHEHEHEH.....\n"
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)   
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    os.system("clear")
    print("##########################")
    print("#    Let the game begin! #")
    print("##########################")
    main_game_loop()










title_screen()
