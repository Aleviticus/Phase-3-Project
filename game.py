import cmd 
import textwrap 
import sys 
import os 
import time 
import random 

#### Player Setup ####
class Player():

    def __init__(self):

        self.name = ""
        self.role = ""
        self.health_points = 0
        self.attack_points = 0
        self.magic_points = 0
        self.weapon = ""
        self.dabloons = 0
        self.game_over = False

myPlayer = Player()

def show_stats():
    print(f"You are now a {myPlayer.role}" )
    print(f"HP: {myPlayer.health_points}")
    print(f"Attack Power: {myPlayer.attack_points}")
    print(f"Magic Power: {myPlayer.magic_points}")
    print(f"Weapon: {myPlayer.weapon}")
    print(f"Dabloons: {myPlayer.dabloons}")

class Monster():
    def __init__(self):

        self.name = "Cryomara"
        self.health_points = 100
        self.attack_points = 50
        self.magic_points = 95
        self.game_over = False

myMonster = Monster()

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
    print(' -  Warriors are brutes who have no magic power to begin with -')
    print(' -  Mages excel in magic whilst having decent combat. -')
    print(' -  Rogues may be tiny and easy to take out, but sure do they pack a punch -')
    print(' -  Priests are balanced all round, dedicating most of their time to priest-ly things. -')
    print(' -  Hunters excel in combat,  but their magic power and large frame are nothing to underestimate. -')
    print(' -  Good luck and have fun!!! -')
    print(" - Would you like to go back? (Yes/No) -")
    option = input("> ")
    if "yes".lower() in option:
        title_screen()
    elif "no".lower()  in option:
        sys.exit()
    else:
        print("I'm asking you a yes or no question")
        help_menu()


def enter_first_town():
    s1 = "You are at the entrance to town \n"
    s2 ="You see the town is under attack by some bandits!!!\n"
    s3 = "Desperate townsfolk seek the help of a brave hero (you).\n"
    s4 = "Do you HELP the people or LEAVE this town\n"
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)   
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    option = input("> ")
    if "help" in option:
        stop_bandits()
    elif "leave" in option:
        skip_town()
    else:
        print("Stick to the adventure!")
        os.system('clear')
        

def stop_bandits():
    os.system('clear')
    print("You wipe the floor with the bandits, but one of them lands a sucker punch")
    myPlayer.health_points -= 1
    print(f"Health: {myPlayer.health_points}")
    s1 = "The townsfolk cheer in relief and celebrate your victory.\n"
    s2 = "The owner of the local inn offers you to stay the night for free.\n"
    s3 = "Do you want to REST the night or CONTINUE on?"
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)   
    option = input("> ")
    if "rest" in option:
        next_morning()
    elif "continue" in option:
        skip_town()
    else:
        print("Stick to the adventure!")
        os.system('clear')

def next_morning():
    os.system('clear')
    myPlayer.health_points += 11
    print("You wake up rejuvinated.")
    print(f"Health: {myPlayer.health_points}")
    s1 = "The sound of an angelic voice woke you up\n"
    s2 = "You see a fair maiden in the distance.\n"
    s3 = "Do you want to start the day off trying to 'RIZZ' up the maiden...\n"
    s4 = "or do you want to EXPLORE the town?\n"
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)   
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    option = input("> ")
    if "rizz" in option:
        rizz_maiden()
    elif "explore" in option:
        explore_town_one()
    else:
        print("Stick to the adventure!")
        os.system('clear')


def skip_town():
    s1 = "You follow a road to the next town over."
    s2 = "You find some change along the way"
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    myPlayer.dabloons += 10
    print(f"Dabloons: {myPlayer.dabloons}" )
    town_two()

def rizz_maiden():
    os.system('clear')
    print("The lady stops singing as you approach her\n")
    s1 = "You bestow upon the maiden your finest rizz\n"
    s2 = "She screams and files a restraining order on you.\n"
    s3 = "You have no choice but to skip town.............................\n"

    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)   
    skip_town()

def explore_town_one():
    os.system('clear')
    print("The town is quite small and not a lot happens this early.")
    s1 = "You find an old man riding a wagaon heading to the next town"
    s2 = "Do you want to TAKE his wagon and ride off with it..."
    s3 = "or PAY him some money to give you a ride?"
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03) 
    option = input("> ")
    if "take" in option:
        town_two()
    elif "pay" in option:
        myPlayer.dabloons -= 30
        print("You give the man 30 dabloons")
        print(f"Dabloons: {myPlayer.dabloons}" )
        town_two() 
    else:
        print("Stick to the adventure!")
        os.system('clear')


def town_two():
    os.system('clear')
    print("You've finally arrived to a new town\n")
    print("You see the sign, it's called Iron Flat\n")
    print("Although bigger than the last, this town also seems much more menacing\n")
    s1 = "Right away you search for food and shelter before it's too late\n"
    s2 = "As you're walking to nearby the halal cart you're approached by a man in black\n"
    s3 = "He says he can offer you free shelter for a fraction of the price you would have to pay otherwise.\n"
    s4 = "Do you want to EAT a mixed over rice first or FOLLOW the man\n"
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)   
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    option = input("> ")
    if "eat" in option:
        grab_halal()
    elif "follow" in option:
        follow_man_in_black()
    else:
        print("Stick to the adventure!")
        os.system('clear')

def grab_halal():
    os.system('clear')
    print("You go to the nearby halal cart and freet the man.\n")
    print("He asks you what yoou wants you go ahead and order....\n")
    option = input("> ")
    s1 = "The man in the cart look at you and says"
    s2 = f"*No the real {option} is the friends you made along the way\n"
    s3 = "*Dramatic music starts to play*\n"
    s4 = "You stand there hungry and confused...wondering what freinds he even meant...............\n"
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)   
    game_over()

    


    print("*No son, the combo over r")

def follow_man_in_black():
    os.system('clear')

    myPlayer.magic_points += 100
    print("He gave you a potion that boosts your MAGIC POWER!!!\n")
    print(f"Your magic level is now {myPlayer.magic_points}\n")
    print("He offers to train you as well, kind of like Dr. Strange")
    print("Do you want to train with the man? Yes / NO\n")
    option = input("> ")
    if "yes" in option:
        fighting_lessons()
    elif "no" in input:
        grab_halal()
    else:
        print("Stick to the adventure!")
        os.system('clear')

def fighting_lessons():
    os.system('clear')
    myPlayer.magic_points += 10 
    myPlayer.health_points += 10
    myPlayer.attack_points += 10 
    print("You meet with the man in black and do vigorous training\n")
    print(f"Your attributes are now - Magic:{myPlayer.magic_points}, Attack:{myPlayer.attack_points}, HP:{myPlayer.health_points} -\n")
    print("Do you want to TEST your skills or GO away")
    option = input("> ")
    if "test" in option:
        skill_test()
    elif "go" in option:
        grab_halal()
    else:
        print("Stick to the adventure!")
        os.system('clear')

def skill_test():
    os.system('clear')
    print("The man puts you through a test with a monster.\n")
    print("Not just any monster, this was a VSCode Syntax error in a file with 600 lines of code")
    print(f"You use your ATTACK with your {myPlayer.weapon} to kill the monster!!!!!!!\n")
    print("You fought a hard battle and took some damage\n")
    myPlayer.health_points -=20
    print(f"{myPlayer.health_points}")
    print("Do you want to a HEALER to regain health or grab some FOOD to recover.\n'")
    option = input('> ')
    if "healer" in option:
        go_to_healer()
    elif "food" in option:
        grab_halal()
    else:
        print("Stick to the adventure!")
        os.system('clear')

def go_to_healer():
    os.system('clear')
    print("You go to the temple down the road and pay the healer to help you")
    print("The healer has healed you.\n")
    myPlayer.dabloons -= 100
    myPlayer.health_points +=20
    print(f"HP: {myPlayer.health_points} Money:{myPlayer.dabloons}")
    print("You finally have time to get your food")
    print("Do you want to go get your fod now?(YES/NO)")
    option = input("> ")
    if "yes" in option:
        grab_halal()
    elif "no" in option:
        town_three()
    else:
        print("Stick to the adventure!")
        os.system('clear')

def town_three():
    os.system('clear')
    print("The civilians welcome you into their town.\n")
    print(f"The King notices you are in town and requests your help {myPlayer.name}.\n")
    print("Do you wish to take on the request reply? (yes/no)")
    option = input("> ")
    if "yes" in option:
        defend_town()
    elif "no" in option:
        grab_halal()

def defend_town():
    os.system('clear')
    print("The King see's your potential and ask for your help.\n")
    print("The King says he needs your help with the monster that attack his town. (yes/no).\n")  
    option = input("> ")
    if "yes" in option:
        fight_monster()
    elif "no" in option:
        grab_halal()  


def fight_monster():
    os.system('clear')
    print(f"Night comes and the monster {myMonster.name} tries to enter town.\n")
    print("The civilians ask for your help to fight the monster.\n")
    print(f"The monster has great attributes HP:{myMonster.health_points}, Attack:{myMonster.attack_points}, Magic;{myMonster.magic_points}\n")
    print("What attack stragtey would you like to use attack or magic? (attack/magic)\n")
    option = input("> ")
    if "attack" in option:
        seek_healer()
    elif "magic" in option:
        seek_healer()

def seek_healer():
    os.system('clear')
    myPlayer.health_points -= 70
    print("You got taken back to town")
    print(f"You are badly injured HP:{myPlayer.health_points}")
    print("The healer advises you to rest")
    print("Do you want to restart or recover")
    option = input("> ")
    if "restart" in option:
        restart_game()
    elif "recover" in option:
        myPlayer.health_points == 100
        skill_test()
    


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
            enter_first_town()
def setup_game():
    os.system('clear')

    q1 = "Hello traveler, what's your name?\n"
    for character in q1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

    q2 = "That weapon you have...it's one of a (Hunter, Mage, Rogue, Priest, Warrior)\n"
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
        os.system("clear")
        myPlayer.role = player_role
    
    if myPlayer.role == 'warrior':
        myPlayer.health_points = 300
        myPlayer.attack_points = 250
        myPlayer.magic_points = 0
        myPlayer.weapon = "Broadsword"
        myPlayer.dabloons = 100
        show_stats()
    elif myPlayer.role == 'mage':
        myPlayer.health_points = 150
        myPlayer.attack_points = 100
        myPlayer.magic_points = 200
        myPlayer.weapon = "Wand"
        myPlayer.dabloons = 100
        show_stats()
    elif myPlayer.role == 'rogue':
        myPlayer.health_points = 100
        myPlayer.attack_points = 300
        myPlayer.magic_points = 150
        myPlayer.weapon = "Dagger"
        myPlayer.dabloons = 100
        show_stats()
    elif myPlayer.role == 'priest':
        myPlayer.health_points = 150
        myPlayer.attack_points = 150
        myPlayer.magic_points = 150
        myPlayer.weapon = "Staff"
        myPlayer.dabloons = 100
        show_stats()
    elif myPlayer.role == 'hunter':
        myPlayer.health_points =200
        myPlayer.attack_points = 150
        myPlayer.magic_points = 100
        myPlayer.weapon = "Crossbow"
        myPlayer.dabloons = 100
        show_stats()



    

    q3 = "A " + player_role + "!" + " Perfect test sub-... lab ra-.... *cough* HERO for this adventure" ".\n"
    for character in q3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    speech1 = f"Welcome to this little adventure travler, {myPlayer.name}!\n"
    speech2 = "I hope its greets you well!\n"
    speech3 = "Just make sure to choose your paths wisely\n"
    speech4 = "HEHEHEHEHEHEHEHEHEHHEHEHEHE......................\n"
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
        time.sleep(0.1)   
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)

    os.system("clear")
    print("###########################")
    print("#Let the adventure begin! #")
    print("###########################")
    main_game_loop()




title_screen()



