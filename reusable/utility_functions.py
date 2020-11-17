#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Part of reusable package
#
# Copyright (c) 2020 - Ohidur Rahman Bappy - MIT License
"""Utility Functions.

Contains a handful of utility functions.
"""

import time
import sys
import imp
import json

__all__=[
    'print_table',
    'print_time_taken',
    'is_python3',
    'is_python_above_or_equal',
    'check_modules_installed',
    'is_valid_json'
]


def print_table(table: list) -> None:
    """Print  as a table.

    For advanced table, check [`tabulate`](https://pypi.org/project/tabulate/).

    Params

        table(list) : The data for the table to be printed

    >>> print_table([[1, 2, 3], [41, 0, 1]])
     1  2  3
    41  0  1
    """
    table = [[str(cell) for cell in row] for row in table]
    column_widths = [len(cell) for cell in table[0]]
    for row in table:
        for x, cell in enumerate(row):
            column_widths[x] = max(column_widths[x], len(cell))

    formatters = []
    for width in column_widths:
        formatters.append("{:>" + str(width) + "}")
    formatter = "  ".join(formatters)
    for row in table:
        print(formatter.format(*row))


def print_time_taken(func) -> None:
    """A decorator that prints time taken by function `func` 

    Params::

        func (def): The function executed

    Usage::

    >>> from reusable import functions.print_time_taken
    >>> @print_time_taken
    >>> def hello():
    >>>    ...

    """
    def _func(*args, **kwargs):
        time_start = time.time()
        fn = func(*args, **kwargs)
        time_end = time.time()
        print(f"INFO: Time of Execution: {time_end-time_start}")
        return fn
    return _func

def is_python3():
    """Check if the python version is 3.0 or above

    """
    return sys.version_info >= (3, 0)
def is_python_above_or_equal(major,minor):
    """Check if the version of the python interpreter is above or equal to major.minor

    """
    return sys.version_info >= (major,minor)

def check_modules_installed(modules:list):
    """Checks if the given modules are installed

    Returns list of not installed module
    """
    not_installed_modules = []
    for module_name in modules:
        try:
            imp.find_module(module_name)
        except ImportError as e:
            # We also test against a rare case: module is an egg file
            try:
                __import__(module_name)
            except ImportError as e:
                not_installed_modules.append(module_name)

    return not_installed_modules


def is_valid_json(json_str:str)->bool:
    """Check if the given string is valid json string

    Return true if json is valid
    """
    try:
        json.loads(json_str)
    except ValueError:
        return False
    return True