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


def save_data(n_to_guess_string, guess_list, karov_list, bikov_list):
    import csv
    import datetime

    time = str(datetime.datetime.now())
    # replace space with _
    time_str = '_'.join(time[:10], time[11:])
    file_name = 'data/game_%s.txt'%((time))
    data_file = open(file_name, 'wt')

    try:
        writer = csv.writer(data_file)
        writer.writerow((n_to_guess, 'karov', 'bikov'))
        for i in xrange(len(guess_list)):
            writer.writerow( guess_list[i], karov_list, bikov_list  )
    finally:
        data_file.close() 

def human_guess_number():
    #TODO write test function
    '''
    This is the actual game bikov and karov, where a human has to guess a unique 6 digit number (0-9) in the right order.
    When this function is called it starts an interactive mode and instructions are printed on the screen. 

    Input
    -----
        raw input during interactive mode

    Return
    ------
    n_to_guess: string
        number that needs to be guessed 
    guess_list: list of strings
        list of all guesses made 
    karov_list: list of integers
        all digits which are the same in both numbers,
        excluding the ones at the correct place
    bikov_list: list of integers
        all digits which are at the correct place
    '''
    n_to_guess = unique_random_number_list()
    # converting list of numbers to string for later saving
    n_to_guess_string = ''.join([str(i) for i in n_to_guess])
    #print n_to_guess #TODO delete when done testing

    bikov = 0
    count = 0
    guess_list = []
    karov_list = []
    bikov_list = []
    print "If you want to end the game type: end"
    print "Guess the number (6 unique digits between 0-9)"
    while bikov != 6:
        count += 1
        guess_int = raw_input()
        if guess_int == 'end':
            break
        while len(guess_int) < 6 or len(guess_int) > 6 or str.isdigit(guess_int) == False:
            if len(guess_int) < 6 or len(guess_int) > 6:
                print "The number has to have exactly 6 digits. Try again."
                guess_int = raw_input()
                if guess_int == 'end':
                    break
            if str.isdigit(guess_int) == False:
                print "It has to be a number, no other characters. Try again."
                guess_int = raw_input()
                if guess_int == 'end':
                    break
        if guess_int == 'end':
            break
        guess = map(int, guess_int)
        #guess = [int(x) for x in str(guess_int)] # list comprehansion 
        karov, bikov = compare_numbers(n_to_guess, guess)
        guess_list += [guess_int]
        karov_list += [karov]
        bikov_list += [bikov]
        print "%i karov, %i bikov"%(karov, bikov)
        print "Guess again!"

    if guess_int == 'end':
        print "Thank you for playing! See you next time :)"
    else:
        print "Congratulations! You guessed the number in %i tries."%(count)
        print "Thank you for playing! See you next time :)"
    #TODO add a save the game option
    #return n_to_guess_string, guess_list, karov_list, bikov_list
    return n_to_guess_string, guess_list, karov_list, bikov_list


if __name__=="__main__":

    
    #TODO, remove when other options are available
    #print "How do you want to play?"
    #print "You guess the number provided by the computer, press: a"
    #print "You want the computer to guess your 6 digit number (must be unique between 0-9), press: b"
    #print "Do you want to play interactive? Press: c"
    #print "NOTE: only option a works right now, you can not choose the other two, haha"
    #option = raw_input()
    
    print "Do you want to save the game? options: yes, no"
    save = raw_input()

    option = 'a'
    if option == 'a':
        n_to_guess_string, guess_list, karov_list, bikov_list = human_guess_number()
        if save == 'yes': 
            save_data(  n_to_guess_string = n_to_guess_string, 
                        guess_list = guess_list, 
                        karov_list = karov_list, 
                        bikov_list = bikov_list)

    elif option == 'b':
        print "The computer will try to guess your unique 6 digit number."
        print "It will provide you with a first guess, for example: 012345"
        print "You have to prove it then with two numbers."
        print "The first number will be called 'karov'i,"
        print "it is the amount of digits which the computers number and yours have in common without the ones at the correct place."
        print "The second number is called bikov, this is the amount of numbers at the correct place."

        out = unique_random_number_list()
        print "Is your number: %i"%(out)
        print "If this is your number press: a"
        print "Otherwise, how many karov did I get?"
        karov = raw_input()
        print "How many bikov did I get?"
        bikov = raw_input()


