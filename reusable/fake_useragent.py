#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Part of reusable package
# 
# Copyright (c) 2020 - Ohidur Rahman Bappy - MIT License
"""Random fake useragent Functions.

Contains functions to return fake random useragent.
"""

import os
import random

__all__=[
    'random_useragent_pc'
]

def random_useragent()->str:
    r"""Return a random useragent for pc.

    Parameters::

        None

    Usage::

        >>> from reusable.fake_useragent import random_useragent
        >>> print(random_useragent_pc())


    """
    dir_path= os.path.dirname(__file__)
    useragents_file_path = os.path.join(dir_path, "data", "useragents.txt")
    _pc_useragents=[line.rstrip('\n') for line in open(useragents_file_path)]
    return random.choice(_pc_useragents)