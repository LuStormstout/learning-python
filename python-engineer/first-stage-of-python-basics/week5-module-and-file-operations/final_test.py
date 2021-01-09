# coding: utf-8

import json
import os
import logging

'''
    学生信息库重构
      1、将学生信息存入一个 json 文件中，添加读写 json 的函数
      2、要将用户添加、修改和删除的行为记录到日志中，添加和修改的日志级别是 info ，delete 用 warn 日志级别
'''


class NotArgError(Exception):
    def __init__(self, message):
        self.message = message


class MissPathError(Exception):
    def __init__(self, message):
        self.message = message


class FormatError(Exception):
    def __init__(self, message):
        self.message = message


class StudentInfo(object):
    def __init__(self, students_path, log_path):
        self.students_path = students_path
        self.log_path = log_path

        self.log = self.__log()
        self.__init_path()
        self.__read()

    def __log(self):
        if os.path.exists(self.log_path):
            mode = 'a'
        else:
            mode = 'w'
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s - %(message)s',
            filename=self.log_path,
            filemode=mode
        )
        return logging

    def __init_path(self):
        if not os.path.exists(self.students_path):
            raise MissPathError('没有相关的地址文件 %s' % self.students_path)

        if not os.path.isfile(self.students_path):
            raise TypeError('当前的 students_path 不是一个文件')

        if not self.students_path.endswith('.json'):
            raise FormatError('当前文件不是一个 json 文件')

    def __read(self):
        with open(self.students_path, 'r') as f:
            try:
                data = f.read()
            except Exception as e:
                raise e
            self.students = json.loads(data)

    def __save(self):
        with open(self.students_path, 'w') as f:
            json_data = json.dumps(self.students)
            f.write(json_data)

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
        self.__save()
        self.__read()

    def batch_add(self, new_students):
        for student in new_students:
            try:
                self.validate(**student)
            except Exception as e:
                print(e, student.get('name'))
                continue
            self.__add(**student)
        self.__save()
        self.__read()

    def __add(self, **student):
        if len(self.students) == 0:
            new_id = 1
        else:
            keys = list(self.students.keys())
            _keys = []
            for item in keys:
                _keys.append(int(item))
            new_id = max(_keys) + 1
        self.students[new_id] = student
        self.log.info('学生 %s 被注册了' % student['name'])

    def delete(self, student_id):
        if student_id not in self.students:
            print(f"{student_id} 并不存在")
        else:
            user_info = self.students.pop(student_id)
            print('学号是{}, {}同学的信息已经被删除了'.format(student_id, user_info['name']))
            self.log.warning('学号是{}, {}同学的信息已经被删除了'.format(student_id, user_info['name']))
        self.__save()
        self.__read()

    def batch_delete(self, ids):
        for id_ in ids:
            if id_ not in self.students:
                print(f'{id_} 不存在学生库中')
                continue
            delete_student_info = self.students.pop(id_)
            print(f"学号{id_} 学生 {delete_student_info['name']} 已经被删除")
            self.log.warning(f"学号{id_} 学生 {delete_student_info['name']} 已经被删除")
        self.__save()
        self.__read()

    def update(self, student_id, **kwargs):
        if student_id not in self.students:
            print(f"{student_id} 并不存在")
        try:
            self.validate(**kwargs)
        except Exception as e:
            raise e
        self.students[student_id] = kwargs
        self.__save()
        self.__read()
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
        self.__save()
        self.__read()
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
    student_obj = StudentInfo('students.json', 'students.log')
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
