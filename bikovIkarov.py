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


