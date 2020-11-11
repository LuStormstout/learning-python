# coding:utf-8

def add(a, b):
    return a + b


result = add(1, 1)
print(result)


# 参数传递顺序应该是 必传参数 默认参数 可变元组参数（*xxx） 可变字典参数（**xxx）


def test_args(*numbers, **users):
    print(numbers)
    print(users
          )


test_args(1, 2, 3, 4, 7, 3, name='zhangsan', age=28)


# 参数类型定义 > python3.7 只起到说明作用并不会强制限制


def person(name: str, age: int = 30):
    print(name)
    print(age)


person(age=25, name='lisi')


# global 可以在函数体内声明全局变量

# 匿名函数的定义


def f(): print(121)


f()


def f1(a, b): return a + b


print(f1(1, 2))

# 实现学生信息库
print('------------------ 实现学生信息库 ------------------')
students = {
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


def get_all_students():
    for id_, value in students.items():
        print(f"学号：{id_}， 姓名：{value['name']}， 年龄：{value['age']}， 班级：{value['class_number']}， 性别：{value['sex']}")

    return students


def add_student(**kwargs):
    id_ = max(students) + 1

    check = validate_student_info(**kwargs)
    if check is not True:
        print(check)
        return
    students[id_] = {
        'name': kwargs['name'],
        'age': kwargs['age'],
        'class_number': kwargs['class_number'],
        'sex': kwargs['sex'],
    }


def delete_student(student_id):
    if student_id not in students:
        print(f"{student_id} 并不存在")
    else:
        user_info = students.pop(student_id)
        print('学号是{}, {}同学的信息已经被删除了'.format(student_id, user_info['name']))


def update_student(student_id, **kwargs):
    if student_id not in students:
        print(f"{student_id} 并不存在")

    check = validate_student_info(**kwargs)
    if check is not True:
        print(check)
        return

    students[student_id] = kwargs
    print('同学信息已经更新完毕')


def validate_student_info(**kwargs):
    if 'name' not in kwargs:
        return '请传入学生姓名'
    if 'age' not in kwargs:
        return '请传入学生年龄'
    if 'class_number' not in kwargs:
        return '请传入学生班级'
    if 'sex' not in kwargs:
        return '请传入学生性别'
    return True


def get_user_by_id(student_id):
    return students.get(student_id)


def search_student(**kwargs):
    values = list(students.values())
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
        if user[key] == value:
            search_result.append(user)
    return search_result


delete_student(1)
add_student(name='moyila', age=32, class_number='B', sex='girl')
update_student(student_id=3, name='wangmazi', age=36, class_number='B', sex='boy')
get_all_students()
print(get_user_by_id(student_id=2))
search_users = search_student(sex='girl')
print(search_users)
