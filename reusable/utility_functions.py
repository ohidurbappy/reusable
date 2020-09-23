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
        print(f"INFO: Time of Execution: {time_end-time_end}")
        return fn
    return _func
