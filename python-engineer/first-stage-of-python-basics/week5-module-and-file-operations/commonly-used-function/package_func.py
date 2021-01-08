# coding: utf-8

# food = input('你想吃什么呢:')
# print(food)
# help(input())

class Test(object):
    a = 1
    b = 2

    def __init__(self):
        self.a = self.a
        self.b = self.b


test = Test()
result = vars(test)
print(result)

print(hasattr(test, 'a'))
print(hasattr(list, 'append'))

setattr(test, 'c', 3)
print(vars(test))

print(getattr(test, 'c'))
print(getattr(list, 'append'))

a = ['', None, True, 0]
print(any(a))  # 有一个为真就会返回 True
print(all(a))  # 有一个为 False 就会返回 False
