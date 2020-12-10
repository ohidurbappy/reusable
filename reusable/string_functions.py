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
    'random_string',
    'headline',
    'splash'
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


def headline(text: str,fill_char: str='-', align: bool = False) -> str:
    r"""Format given string in headline

    Parameters::

        text (str): The string to be formatted
        fill_char (str): The character to use to style the string

    Usage::

        >>> from reusable.functions import *
        >>> print(headline("Hello World","-"))

    """
    if align:
        return f"{text.title()}\n{fill_char * len(text)}"
    else:
        return f" {text.title()} ".center(40,fill_char)


def splash(text: str,decor_char: str = '-') -> str:
    r"""Prints given string as a splash

    Parameters::

        text (str): The input string
        decor_char (str): The character to decorate the splash

    Usage::

        from reusable.functions import *
        splash("Hello World")

    """
    lines=text.split("\n")
    max_char=0
    for line in lines:
        if len(line)>max_char:
            max_char=len(line)


    txt="+"+decor_char*(max_char+6)+"+\n"
    for line in lines:
        txt+="|"+ line.center(max_char+6," ") +"|\n"
    txt+="+"+decor_char*(max_char+6)+"+"
    print(txt)

    
    