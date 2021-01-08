# coding: utf-8

# iter_obj = iter((1, 2, 3))


# def _next(iter_obj):
#     try:
#         return next(iter_obj)
#     except StopIteration:
#         return None

# print(_next(iter_obj))
# print(_next(iter_obj))
# print(_next(iter_obj))
# print(_next(iter_obj))

# for i in iter_obj:
#     print(i)


# def make_iter():
#     for i in range(10):
#         yield i
# 
# 
# iter_obj = make_iter()
# for item in iter_obj:
#     print(item)


iter_obj = (i for i in range(10))
for item in iter_obj:
    print(item)
