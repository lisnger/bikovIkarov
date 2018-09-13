#! usr/bin/enrandomv python
# -*- coding: utf-8 -*-

import pytest
import bikovIkarov as bik
import numpy as np

def test_unique_random_number_list():
    ar = bik.unique_random_number_list()
    uar = set(ar)
    assert len(ar) == len(uar)

