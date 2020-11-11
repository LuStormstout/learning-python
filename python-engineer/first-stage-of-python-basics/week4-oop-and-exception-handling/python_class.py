# coding:utf-8

# python 类的定义 class 用大驼峰命名
# self 是类函数中必传的参数，且必须放在第一个参数位置
# self 是一个对象，代表实例化的自身变量
# 类的构造函数 def __init__(self)
# 类的析构函数 def __del__(self)
# 类的私有函数、私有变量 无法被实例化后的对象调用 __ 函数名或者变量前面加两个下划线

class Person(object):
    name = '张三'
    __age = 12

    def jump(self):
        print(f'{self.name} is jumping')

    def __sleep(self):
        pass  # 占位符


zhangsan = Person()
print(zhangsan.name)
zhangsan.jump()


# 装饰器：也是一种函数 可以接受函数作为参数 可以返回函数
def check_str(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == 'ok':
            return 'result is: %s' % result
        else:
            return 'result is failed: %s' % result

    return inner


@check_str
def test(data):
    return data


test_result = test('ok')
print(test_result)

'''
类中的装饰器
classmethod 将类函数可以不经过实例化而直接被调用
    
@classmethod
def func(cls, ...):
    do

cls 替代普通类函数中的 self 代表操作的是类


staticmethod 将类函数可以不经过实例化而直接被调用，被该装饰器调用的函数不需要传递 self 或 cls 参数，
且无法再该函数内调用其他类函数或类变量

@staticmethod
def func(...):
    do
    

property 将类函数的执行免去括弧，类似于调用类属性

@property
def func(self):
    do

'''


class Test(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        print(self.name, 'run')

    @classmethod
    def jump(cls):
        print('jump')

    @staticmethod
    def sleep():
        print('I want sleep.')


t = Test('MoYiLa')
t.run()
Test.jump()
Test.sleep()
t.sleep()


class Test1(object):
    def __init__(self, name):
        self.__name = name

    @property
    def call_name(self):
        return self.__name


t1 = Test1(name='ZhangSnan')
print(t1.call_name)


# 类的继承
class Parent(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def walk(self):
        return f'{self.name} are walking'

    def is_sex(self):
        if self.sex == 'boy':
            return f'{self.name} is a boy'
        else:
            return f'{self.name} is a girl'


class ChildOne(Parent):
    def play_football(self):
        return f'{self.name} are playing football'


class ChildTwo(Parent):
    def play_ping_pong(self):
        return f'{self.name} are playing ping-pong'


p_class = Parent(name='MaZi', sex='boy')
print(p_class.walk())
c_one = ChildOne(name='DaChui', sex='boy')
print(c_one.is_sex())
print(c_one.play_football())
c_two = ChildTwo(name='MoYiLa', sex='girl')
print(c_two.walk())
print(c_two.play_ping_pong())


# 类的 super 函数，Python 子类继承父类的方法而使用的关键字，当子类继承父类后，就可以使父类的方法
class P1(object):
    def __init__(self, p):
        print('Hello i ma parent %s' % p)


class C1(P1):
    def __init__(self, c, p):
        super().__init__(p)
        print('Hello i ma Child %s' % c)


p1 = P1('父类')
print('=====')
c1 = C1('子类', '父类')


# 类的多态
# 通过重写父类方法实现类的多态
class P2(object):
    def talk(self):
        print('父类说了一句话')


class C2(P2):
    def talk(self):
        print('C2类说不一样的话')


class C3(P2):
    def talk(self):
        print('C3类在说话')


print('---------')
p2 = P2()
p2.talk()
c2 = C2()
c2.talk()
c3 = C3()
c3.talk()


# 多重继承 class Child(Parent1, Parent2, ...)
# 最左边的类会被先继承 如果多个类里面都有同一个方法的话 会执行最左边的类的函数
class ClassOne(object):
    @staticmethod
    def work():
        print('ClassOne work')


class ClassTwo(object):
    @staticmethod
    def work():
        print('ClassTwo work')


class ClassChild(ClassTwo, ClassOne):
    pass


print('----------')
class_child = ClassChild()
class_child.work()
print(ClassChild.__mro__)

'''
类中的高级函数
__str__ 当前类的描述
def __str__(self):
    return str

__getattr__ 当调用的属性或者方法不存在时，会返回该方法定义的信息
def __getattr__(self, key):
    print(something...)

__setattr__ 拦截当前类中不存在的属性与值
def __setattr__(self, key, value):
    self.__dict__[key] = value

__call__ 将一个实例化后的类变成一个函数来使用
def __call__(self, *args, **kwargs):
    print('balabala...')

'''


class ClassFunction(object):
    def __str__(self):
        return '这是一个类的自带函数联系类'

    def __getattr__(self, item):
        return f'{item} 不存在'

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __call__(self, *args, **kwargs):
        print('call 被执行了 %s' % kwargs)


print('-----------')
class_function = ClassFunction()
print(class_function)
print(class_function.name)
class_function.info = '这是测试信息'
print(class_function.info)
class_function(name='zhangsan', age='33')


# 学生信息库用类重构
class StudentInfo(object):
    def __init__(self, students):
        self.students = students

    def get(self, student_id):
        return self.students.get(student_id)

    def get_all(self):
        for id_, value in self.students.items():
            print(f"学号：{id_}， 姓名：{value['name']}， 年龄：{value['age']}， 班级：{value['class_number']}， 性别：{value['sex']}")
        return self.students

    def add(self, **student):
        check = self.validate(**student)
        if check is not True:
            print(check)
            return
        self.__add(**student)

    def batch_add(self, new_students):
        for student in new_students:
            check = self.validate(**student)
            if check is not True:
                print(check, student.get('name'))
                continue
            self.__add(**student)

    def __add(self, **student):
        new_id = max(self.students) + 1
        self.students[new_id] = student

    def delete(self, student_id):
        if student_id not in self.students:
            print(f"{student_id} 并不存在")
        else:
            user_info = self.students.pop(student_id)
            print('学号是{}, {}同学的信息已经被删除了'.format(student_id, user_info['name']))

    def batch_delete(self, ids):
        for id_ in ids:
            if id_ not in self.students:
                print(f'{id_} 不存在学生库中')
                continue
            delete_student_info = self.students.pop(id_)
            print(f"学号{id_} 学生 {delete_student_info['name']} 已经被删除")

    def update(self, student_id, **kwargs):
        if student_id not in self.students:
            print(f"{student_id} 并不存在")

        check = self.validate(**kwargs)
        if check is not True:
            print(check)
            return

        self.students[student_id] = kwargs
        print('同学信息已经更新完毕')

    def batch_update(self, update_students):
        for student in update_students:
            id_ = list(student.keys())[0]
            if id_ not in self.students:
                print(f'学号：{id_} 不存在')
                continue
            user_info = student[id_]
            check = self.validate(**user_info)
            if check is not True:
                print(check)
                continue
            self.students[id_] = user_info
        print('所有用户信息更新完成')

    def search(self, **kwargs):
        values = list(self.students.values())
        search_result = []

        if 'name' in kwargs:
            key = 'name'
            value = kwargs[key]
        elif 'age' in kwargs:
            key = 'age'
            value = kwargs[key]
        elif 'class_number' in kwargs:
            key = 'class_number'
            value = kwargs[key]
        elif 'sex' in kwargs:
            key = 'sex'
            value = kwargs[key]
        else:
            print('没有对应的查询关键字')
            return

        for user in values:
            if value in user[key]:
                search_result.append(user)
        return search_result

    @staticmethod
    def validate(**kwargs):
        if 'name' not in kwargs:
            return '请传入学生姓名'
        if 'age' not in kwargs:
            return '请传入学生年龄'
        if 'class_number' not in kwargs:
            return '请传入学生班级'
        if 'sex' not in kwargs:
            return '请传入学生性别'
        return True


students_info = {
    1: {
        'name': 'zhangsan',
        'age': 25,
        'class_number': 'A',
        'sex': 'boy'
    },
    2: {
        'name': 'lisi',
        'age': 28,
        'class_number': 'A',
        'sex': 'boy'
    },
    3: {
        'name': 'wangmazi',
        'age': 30,
        'class_number': 'A',
        'sex': 'boy'
    },
    4: {
        'name': 'xiaomei',
        'age': 29,
        'class_number': 'B',
        'sex': 'girl'
    },
    5: {
        'name': 'aishi',
        'age': 25,
        'class_number': 'B',
        'sex': 'girl'
    }
}

if __name__ == '__main__':
    print('------------------ 实现学生信息库重构 ------------------')
    student_obj = StudentInfo(students_info)
    print(student_obj.get(2))
    student_obj.add(name='JackLu', age='29', class_number='B', sex='boy')
    batch_users_info = [
        {'name': '曹操', 'age': 19, 'class_number': 'C', 'sex': 'boy'},
        {'name': '司马懿', 'age': 34, 'class_number': 'C', 'sex': 'boy'},
        {'name': '马超', 'age': 27, 'class_number': 'C', 'sex': 'boy'},
        {'name': '大乔', 'age': 22, 'class_number': 'C', 'sex': 'girl'}
    ]
    student_obj.batch_add(batch_users_info)
    student_obj.get_all()
    student_obj.batch_delete([8, 9])
    student_obj.get_all()
    print('------------------ 批量更行用户信息 ------------------')
    student_obj.batch_update([
        {7: {'name': '曹操', 'age': 20, 'class_number': 'C', 'sex': 'boy'}},
        {10: {'name': '大乔s', 'age': 23, 'class_number': 'C', 'sex': 'girl'}}
    ])
    student_obj.get_all()
    print('------------------ 模糊查找用户 ------------------')
    print(student_obj.search(name='s'))
