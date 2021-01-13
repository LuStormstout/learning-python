# coding:utf-8

import os

from common import error

"""
    1、导入 user.json 文件检查
    1、导入 gift.json 文件检查
"""


class Base(object):
    def __init__(self, user_json, gift_json):
        self.user_json = user_json
        self.gift_json = gift_json

    def check_user_json(self):
        if not os.path.exists(self.user_json):
            raise error.NotFileError('not found %s' % self.user_json)

        if not self.user_json.endswith('.json'):
            raise error.FormatError()

        if not os.path.isfile():

