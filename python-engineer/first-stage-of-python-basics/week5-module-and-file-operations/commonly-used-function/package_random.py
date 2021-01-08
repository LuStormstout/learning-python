# coding: utf-8

import random

# random.random() 随机返回 0 - 1 之间的浮点数
# random.uniform(a, b) 返回 a,b 区间的一个随机浮点数
# random.randint(a, b) 返回 a,b 区间的一个随机整数
# random.choice(object) 返回对象中的一个随机元素
# random.sample(object, number) 随机返回对象中指定数量的元素
# random.randrange(a, b, c) 获取区间内的一个随机数，c 步长

gifts = ['iphone', 'ipad', 'car', 'tv']


def choice_gift():
    gift = random.choice(gifts)
    print('你抽到了:%s' % gift)


def choice_gift_new():
    count = random.randrange(0, 100, 1)
    if 0 <= count <= 50:
        print('你抽中了 iphone')
    elif 50 < count <= 70:
        print('你抽中了 ipad')
    elif 70 < count < 90:
        print('你抽中了 tv')
    elif count >= 90:
        print('你抽中了 car')


if __name__ == '__main__':
    choice_gift_new()
