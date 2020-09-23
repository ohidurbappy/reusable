#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Part of reusable package
#
# Copyright (c) 2020 - Ohidur Rahman Bappy - MIT License
"""Iterable Functions.

Contains a handful of iterable functions.
"""


from collections import defaultdict


def groupby_count(i, key=None, force_keys=None):
    """Group a list of elements as per the count

    Usage::

        >>> from reusable.functions import groupby_count
        >>> print(groupby_count([1,1,1,2,3]))
        [(1,3),(2,1),(3,1)]
    """
    counter = defaultdict(lambda: 0)
    if not key:
        def key(o): return o

    for k in i:
        counter[key(k)] += 1

    if force_keys:
        for k in force_keys:
            counter[k] += 0

    return counter.items()