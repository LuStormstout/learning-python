# Python3 的六个标准数据类型中：
#     不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
#     可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

# 字符串 str
# x = 'abc'
# print(type(x), dir(x))
#
# # 字典 dict
# y = dict()
# print(type(y), dir(y))
#
# # 列表 list
# z = list()
# print(type(z), dir(z))
#
# # 整型 int
# a = 123
# print(type(a), dir(a))
#
# # 浮点型 float
# b = 1.23
# print(type(b), dir(b))
#
# # 元组 tuple
# c = tuple()
# print(type(c), dir(c))
#
# # 集合 set
# d = set()
# print(type(d), dir(d))


class FirstObject:
    x = 0
    name = ''

    def __init__(self, z):
        self.name = z
        print('I am construct')

    def party(self):
        self.x = self.x + 1
        print('x:', self.x, 'name:', self.name)

    # def __del__(self):
    #     print('I am destruct', self.name, self.x)


# fo = FirstObject('lu')
# fo.party()
# fo.party()
# fo.party()
# print("======================")
#
# fo1 = FirstObject('chrome')
# fo1.party()
# print("======================")
#
# print(dir(fo))

class NewObject(FirstObject):
    points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points:", self.points)


no = NewObject('Apple')
no.party()
no.touchdown()
