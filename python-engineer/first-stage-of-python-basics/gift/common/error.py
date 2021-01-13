# coding:utf-8


class NotFileError(Exception):
    def __init__(self, message):
        self.message = message


class FormatError(Exception):
    def __init__(self, message='need json format'):
        self.message = message
