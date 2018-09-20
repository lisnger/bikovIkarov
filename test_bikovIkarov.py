#! usr/bin/enrandomv python
# -*- coding: utf-8 -*-

import pytest
import bikovIkarov as bik
import numpy as np
import mock
import os

def test_unique_random_number_list():
    '''
    Compares if the length of the list ar is the same as the uniqe set of ar.
    '''
    ar = bik.unique_random_number_list()
    uar = set(ar)
    assert len(ar) == len(uar)

def test_compare_numbers():
    '''
    Takes example data and known results and compares if function returns expected results.
    '''
    a = [3,5,1,9,8,0]
    b = [1,2,3,4,8,6]
    same_ab = 2
    correct_ab = 1
    same, correct = bik.compare_numbers(n_to_guess=a, guess=b)
    assert same == same_ab
    assert correct == correct_ab

def test_save_data():
    n_to_guess_string = '012345'
    guess_list = ['123456', '023456','012345']
    karov_list = [5, 4, 0]
    bikov_list = [0, 1, 6]
    file_name = './data/test_delete_me.txt'
    bik.save_data(n_to_guess_string, guess_list, karov_list, bikov_list, file_name='test_delete_me')
    file_exist = os.path.isfile(file_name)
    assert file_exist == True

#TODO find a better way to test that function
#def test_human_guess_number():
#    with mock.patch.object(__builtin__, 'raw_input', lambda: '12345'):
#        assert bik.human_guess_number() == 'The number has to have exactly 6 digits. Try again.'
#    
#    #bik.raw_input = lambda: '123456'
    


