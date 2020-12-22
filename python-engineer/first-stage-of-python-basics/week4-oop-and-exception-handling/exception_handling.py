# coding:utf-8

"""
Python 异常处理

try:
    <代码块1>
except <异常的类型>:
    <代码块2>

通用异常类型 Exception
try:
    <代码块1>
except Exception as e:
    <代码块2>

具体异常捕获

多重异常捕获：
    写多个 except:
    except(异常类型1, 异常类型2, ...) as e:

"""


# def upper(str_data):
#     try:
#         new_str = str_data.upper()
#         return new_str
#     except Exception as e:
#         print('程序出错了:{}'.format(e))
#
#
# class Test(object):
#     pass


# t = Test()
# try:
#     t.name
# except AttributeError as e:
#     print(e)

# def test1():
#     try:
#         1 / 0
#     except Exception as e:
#         return e
#     finally:
#         return 'finally'
#
#
# print(test1())


# 自定义异常 raise
# def test2(number):
#     if number == 100:
#         raise ValueError('number 不可以是 100')
#     return number
#
#
# print(test2(50))


# print(test2(100))


# def test3(number):
#     try:
#         return test2(number)
#     except ValueError as e:
#         return e
#
#
# print(test3(100))
#
#
# class NumberLimitError(Exception):
#     def __init__(self, message):
#         self.message = message
#
#
# class NameLimitError(Exception):
#     def __init__(self, message):
#         self.message = message
#
#
# def test4(name):
#     if name == 'jacklu':
#         raise NameLimitError('jacklu 不可以被填写')
#     return name
#
#
# def test5(number):
#     if number > 100:
#         raise NumberLimitError('数字不能大于 100')
#     return number
#
#
# try:
#     test4('jacklu')
# except NameLimitError as e:
#     print(e)
#
# try:
#     test5(101)
# except NumberLimitError as e:
#     print(e)


# 断言：用于判断一个表达式，在表达式条件为 false 的时候出发异常
# assert expression, message
#   expression：表达式
#   message：具体的错误信息

class NotArgError(Exception):
    def __init__(self, message):
        self.message = message


# 学生信息库用异常捕获重构
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
        try:
            self.validate(**student)
        except Exception as e:
            print(e)
            raise e
        self.__add(**student)

    def batch_add(self, new_students):
        for student in new_students:
            try:
                self.validate(**student)
            except Exception as e:
                print(e, student.get('name'))
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
        try:
            self.validate(**kwargs)
        except Exception as e:
            raise e
        self.students[student_id] = kwargs
        print('同学信息已经更新完毕')

    def batch_update(self, update_students):
        for student in update_students:
            try:
                id_ = list(student.keys())[0]
            except IndexError as e:
                print(e)
                continue
            if id_ not in self.students:
                print(f'学号：{id_} 不存在')
                continue
            user_info = student[id_]
            try:
                self.validate(**user_info)
            except Exception as e:
                print(e)
                continue
            self.students[id_] = user_info
        print('所有用户信息更新完成')

    def search(self, **kwargs):
        assert len(kwargs) == 1, '参数数量传递错误'
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
            raise NotArgError('没有对应的查询关键字')

        for user in values:
            if value in user[key]:
                search_result.append(user)
        return search_result

    @staticmethod
    def validate(**kwargs):
        assert len(kwargs) == 4, '参数必须是 4 个'
        if 'name' not in kwargs:
            raise NotArgError('缺少学生姓名参数')
        if 'age' not in kwargs:
            raise NotArgError('缺少学生年龄参数')
        if 'class_number' not in kwargs:
            raise NotArgError('缺少学生班级参数')
        if 'sex' not in kwargs:
            raise NotArgError('缺少学生性别参数')

        name_value = kwargs['name']
        age_value = kwargs['age']
        class_number_value = kwargs['class_number']
        sex_value = kwargs['sex']

        # isinstance(对比的数据, 目标类型) isinstance(1, int)
        if not isinstance(name_value, str):
            raise TypeError('name 应该是字符串类型')
        if not isinstance(age_value, int):
            raise TypeError('age 应该是整型')
        if not isinstance(class_number_value, str):
            raise TypeError('class_number 应该是字符串类型')
        if not isinstance(sex_value, str):
            raise TypeError('sex 应该是字符串类型')


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
    student_obj.add(name='JackLu', age=29, class_number='B', sex='boy')
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
