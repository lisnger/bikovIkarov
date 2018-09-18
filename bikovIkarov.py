#! usr/bin/enrandomv python
# -*- coding: utf-8 -*-


import numpy as np
import random


def unique_random_number_list():
    '''
    Returns 
    -------
    n_list: list
        list of 6 unique numbers between 0 and 9 (inculding both)
    '''
    n_list = []
    
    while (len(n_list)) < 6:
        rint = random.randint(0,9)
        if not rint in n_list:
            n_list += [rint]
        else: 
            continue

    return n_list

def compare_numbers(n_to_guess, guess):
    '''
    Compares two lists with the same length and determines 
    1) the number of same entries "same"
    2) the number of entries at the correct position "correct"
    3) returns both numbers, where the number of same entries is reduced by the correct ones

    Parameters
    ----------
    n_to_guess: list
    guess:  list, has to have the same length as n_to_guess

    Returns
    -------
    same: int
        number of same entries in both lists, excluding the numbers at the korrect position 
    correct: int
        number of entries at the correct position
    '''
    same  = 0
    correct = 0
    for i in xrange(len(n_to_guess)):
        if guess[i] in n_to_guess:
            same += 1
        if guess[i] == n_to_guess[i]:
            correct += 1
            same -= 1
    return same, correct

def human_guess_number():
    #TODO write test function
    '''
    This is the actual game bikov and karov, where a human has to guess a unique 6 digit number (0-9) in the right order.
    When this function os called it starts an interactive mode and instructions are printed on the screen. 
    '''
    print "Guess the number (6 unique digits between 0-9)"
    bikov = 0
    count = 0
    while bikov != 6:
        count += 1
        guess_int = raw_input()
        while len(guess_int) < 6 or len(guess_int) > 6 or str.isdigit(guess_int) == False:
            if len(guess_int) < 6 or len(guess_int) > 6:
                print "The number has to have exactly 6 digits. Try again."
                guess_int = raw_input()
            if str.isdigit(guess_int) == False:
                print "It has to be a number, no other characters. Try again."
                guess_int = raw_input()
        guess = map(int, guess_int)
        #guess = [int(x) for x in str(guess_int)] # list comprehansion 
        karov, bikov = compare_numbers(n_to_guess, guess)
        print "%i karov, %i bikov"%(karov, bikov)
        print "Guess again!"
    print "Congratulations! You guessed the number in %i tries."%(count)


if __name__=="__main__":

    n_to_guess = unique_random_number_list()
    print n_to_guess #TODO delete when done testing
    
    #TODO, remove when other options are available
    #print "How do you want to play?"
    #print "You guess the number provided by the computer, press: a"
    #print "You want the computer to guess your 6 digit number (must be unique between 0-9), press: b"
    #print "Do you want to play interactive? Press: c"
    #print "NOTE: only option a works right now, you can not choose the other two, haha"
    #option = raw_input()
    option = 'a'

    if option == 'a':
        human_guess_number()

    elif option == 'b':
        print "The computer will try to guess your unique 6 digit number."
        print "It will provide you with a first guess, for example: 012345"
        print "You have to prove it then with two numbers."
        print "The first number will be called 'karov'i"
        print "it is the amount of digits which the computers number and yours have in common without the ones excluding stand at the correct place"
        print "the second number is called bikov, this is the amount of numbers at the correct place."

        out = unique_random_number_list()
        print "Is your number: %i"%(out)
        print "If this is your number press: a"
        print "Otherwise, how many karov did I get?"
        karov = raw_input()
        print "How many bikov did I get?"
        bikov = raw_input()


