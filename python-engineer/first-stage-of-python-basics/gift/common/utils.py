# coding:utf-8


import os
import time

from .error import NotPathError, FormatError, NotFileError


def timestamp_to_string(timestamp):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))


def check_file(path):
    if not os.path.exists(path):
        raise NotPathError("file '%s' does not exist" % path)

    if not path.endswith('.json'):
        raise FormatError('need json format')

    if not os.path.isfile(path):
        raise NotFileError('not a file')
