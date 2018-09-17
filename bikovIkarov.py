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


if __name__=="__main__":

    n_to_guess = unique_random_number_list()
    print n_to_guess
    
    print "Guess the number (6 unique digits between 0-9)"
    guess_int = raw_input()
    guess = [int(x) for x in str(guess_int)]
    print guess
    karov, bikov = compare_numbers(n_to_guess, guess)
    print "%i karov, %i bikov"%(karov, bikov)

    count = 1
    while bikov != 6:
        count += 1
        print "Guess again!"
        guess_int = input()
        guess = map(int, str(guess_int))
        karov, bikov = compare_numbers(n_to_guess, guess)
        print "%i karov, %i bikov"%(karov, bikov)
    print "Congratulations! You guessed the number in %int tries"%(count)


