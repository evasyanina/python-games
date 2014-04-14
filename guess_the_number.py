# Guess the number game using simplegui in CodeSculptor
# input comes from buttons and an input field in gui
# all output for the game is printed in the console

import random
import math
import simplegui

# global variables
rand_number = 0
player_guess = 0
chosen_range = 100 
i = 0
    
# helper function to start and restart the game
def new_game():
    print "********************"
    print "New game started!!!"
    print "You have", num_guesses(), "guesses to guess the number in the range from 0 to", chosen_range
    print ''
    global rand_number
    user_input.set_text("")
    rand_number = random.randrange(0, chosen_range)
    return rand_number

def num_guesses():
    #determines number of allowed guesses
    guess_left = int(math.ceil(math.log (chosen_range, 2)))
    return guess_left

def range100():
    # button that changes range to range [0,100) and restarts
    global chosen_range
    chosen_range = 100
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global chosen_range
    chosen_range = 1000
    new_game()
    
def input_guess(guess):
    global player_guess
    global i
    try:
        player_guess = int(guess)
        if player_guess == rand_number:
            print "You entered:", player_guess
            print "This is correct number!!!"
            print "Congradulations, You won!!!"
            print ''
            new_game()
            i = 0
        elif player_guess < rand_number:
            i += 1
            if num_guesses() - i != 0:
                print "You entered:", player_guess
                print "Enter a higher number"   
            if num_guesses() - i == 1:
                print "You have", num_guesses() - i, "guess remaining"
                print ''
            elif num_guesses() - i == 0:
                print "You lost!!!"
                print "Then number you was guessing was", rand_number
                print ''
                new_game()
                i = 0
            else:
                print "You have", num_guesses() - i, "guesses remaining" 
                print ''
        elif player_guess > rand_number:
            i += 1
            if num_guesses() - i != 0:
                print "You entered:", player_guess
                print "Enter a lower number"
            if num_guesses() - i == 1:
                print "You have", num_guesses() - i, "guess remaining"
                print ''
            elif num_guesses() - i == 0:
                print "You lost!!!"
                print "Then number you was guessing was", rand_number
                print ''
                new_game()
                i = 0
            else:
                print "You have", num_guesses() - i, "guesses remaining" 
                print ''
    except ValueError:
        print "Please enter a valid number!"
        print ''
    
# create frame
frame = simplegui.create_frame("Guess the number game", 200, 200)
user_input = frame.add_input("Enter your guess:", input_guess, 100)
range_1 = frame.add_button("Range: 0-100", range100, 100)
range_2 = frame.add_button("Range: 0-1000", range1000, 100)
restart_button  = frame.add_button("Restart", new_game, 100)

# call new_game and start frame
new_game()
frame.start()


