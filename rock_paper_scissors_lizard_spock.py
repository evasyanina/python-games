# Rock-paper-scissors-lizard-Spock Game

import random

def name_to_number(name):
    if (name == 'rock' or name == 'Rock'):
        number = 0
    elif (name == 'spock' or name == 'Spock'):
        number = 1
    elif (name == 'paper' or name == 'Paper'):
        number = 2
    elif (name == 'lizard' or name == 'Lizard'):
        number = 3
    elif (name == 'scissors' or name == 'Scissors'):
        number = 4
    else:
        print "Entered name doesn't exist in this game"
    return number

def number_to_name(number):
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        print "Entered number is not in the correct range"
    return name
    
def rpsls(player_choice): 
    print "=============="
    print "Player chooses", player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses", comp_choice
    # compute difference of comp_number and player_number modulo five
    diff = (comp_number - player_number) % 5
    # use if/elif/else to determine winner, print winner message
    if (diff == 3 or diff == 4):
        print "Player wins!"
    elif (diff == 1 or diff == 2):
        print "Computer wins!"
    elif diff == 0:
        print "It's a tie"
    else:
        print "Something went wrong!"

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



