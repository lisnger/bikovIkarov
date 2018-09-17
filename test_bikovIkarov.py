#! usr/bin/enrandomv python
# -*- coding: utf-8 -*-

import pytest
import bikovIkarov as bik
import numpy as np

def test_unique_random_number_list():
    ar = bik.unique_random_number_list()
    uar = set(ar)
    assert len(ar) == len(uar)

def test_compare_numbers():
    a = [3,5,1,9,8,0]
    b = [1,2,3,4,8,6]
    same_ab = 2
    correct_ab = 1
    same, correct = bik.compare_numbers(n_to_guess=a, guess=b)
    assert same == same_ab
    assert correct == correct_ab


