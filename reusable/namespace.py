#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Part of reusable package
# 
# Copyright (c) 2020 - Ohidur Rahman Bappy - MIT License
"""Improved dictionary management.

Dictionary management for python inspired by javascript style referencing.
"""
import sys

try:
    from collections.abc import Mapping, Iterable
except ImportError:
    Mapping = dict
    Iterable = (tuple, list)

if sys.version_info >= (3, 0):
    basestring = str


def _recursive_create(self, iterable):
    for k, v in iterable:
        if isinstance(v, dict):
            v = Namespace(v)
        setattr(self, k, v)


class Namespace(dict):
    r"""
    Namespace container.
    Allows access to attributes by either class dot notation or item reference

    Valid::

        - namespace.spam.eggs
        - namespace['spam']['eggs']
        - namespace['spam'].eggs
    """

    _protected_keys = dir({}) + ['to_dict', 'tree_view']

    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            if isinstance(args[0], basestring):
                raise ValueError("Cannot extrapolate Namespace from string")
            if isinstance(args[0], Mapping):
                _recursive_create(self, args[0].items())
            elif isinstance(args[0], Iterable):
                _recursive_create(self, args[0])
            else:
                raise ValueError("First argument must be mapping or iterable")
        elif args:
            raise TypeError("Namespace expected at most 1 argument, "
                            "got {0}".format(len(args)))
        _recursive_create(self, kwargs.items())

    def __contains__(self, item):
        try:
            return dict.__contains__(self, item) or hasattr(self, item)
        except Exception:
            return False

    def __getattr__(self, item):
        try:
            return object.__getattribute__(self, item)
        except AttributeError:
            try:
                return self[item]
            except KeyError:
                raise AttributeError(item)

    def __setattr__(self, key, value):
        if key in self._protected_keys:
            raise AttributeError("Key name '{0}' is protected".format(key))
        if isinstance(value, dict):
            value = self.__class__(**value)
        try:
            object.__getattribute__(self, key)
        except AttributeError:
            try:
                self[key] = value
            except Exception:
                raise AttributeError(key)
        else:
            object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item in self._protected_keys:
            raise AttributeError("Key name '{0}' is protected".format(item))
        try:
            object.__getattribute__(self, item)
        except AttributeError:
            try:
                del self[item]
            except KeyError:
                raise AttributeError(item)
        else:
            object.__delattr__(self, item)

    def __repr__(self):
        return "<Namespace: {0}>".format(str(self.to_dict()))

    def __str__(self):
        return str(self.to_dict())

    def __call__(self, *args, **kwargs):
        return tuple(self.values())

    def to_dict(self, in_dict=None):
        """
        Turn the Namespace and sub Namespaces back into a native
        python dictionary.
        
        :param in_dict: Do not use, for self recursion
        :return: python dictionary of this Namespace
        """
        in_dict = in_dict if in_dict else self
        out_dict = dict()
        for k, v in in_dict.items():
            if isinstance(v, Namespace):
                v = v.to_dict()
            out_dict[k] = v
        return out_dict

    def tree_view(self, sep="    "):
        base = self.to_dict()
        return tree_view(base, sep=sep)
