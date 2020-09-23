#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Part of reusable package
#
# Copyright (c) 2020 - Ohidur Rahman Bappy - MIT License
"""Network related Functions.

Contains a handful of network functions.
"""


import os
import sys
from urllib.request import urlopen

def download_file(url, path,overrite=False):
    """Downloads a file from `url` and saves it to `path`

    Usage::

        >>> from reusable.functions import download_file
        >>> download_file('https://www.exaple.com/example.jpg','./images',True)

    """
    file_name = os.path.basename(url)
    if not overrite and os.path.exists(file_name):
        raise Exception("Target file already exists")
    u = urlopen(url)
    target = file_name
    if path:
        target = os.path.join(path,target)
    f = open(target+".temp", 'wb')
    meta = u.info()
    file_size = int(meta.get("Content-Length")[0])
    print("Downloading: %s Bytes: %s" % (file_name, file_size))
    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (
            file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        sys.stdout.write(status)
        if not '100.00' in status:
            sys.stdout.write('\r')
    f.close()
    if overrite:
        if os.path.exists(target):
            os.remove(target)
    os.rename(target+".temp", target)
    return target
