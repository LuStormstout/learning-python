# coding:utf-8


import os

from .error import NotPathError, FormatError, NotFileError


def check_file(path):
    if not os.path.exists(path):
        raise NotPathError('not found %s' % path)

    if not path.endswith('.json'):
        raise FormatError('need json format')

    if not os.path.isfile(path):
        raise NotFileError('this is not a file')
