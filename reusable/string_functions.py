#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Part of reusable package
# 
# Copyright (c) 2020 - Ohidur Rahman Bappy - MIT License
"""String Related Functions.

Contains a handful of string related functions.
"""

import random
import string

__all__=[
    'random_string'
]

def random_string(length:int=6, charset:str=string.ascii_letters+string.digits):
    r"""Return a random string of given length and charset.

    Default charset is url-friendly (base62).

    Parameters::

        length (int): The length(optional) of the string to return
        charset (str): The character set to build the string

    Usage::

        >>> from reusable.functions import *
        >>> print(random_string(5))


    """
    return ''.join([random.choice(charset) for i in range(length)])