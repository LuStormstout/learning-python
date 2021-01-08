# coding: utf-8

import json


def read(path):
    with open(path, 'r') as f:
        data = f.read()
    return json.loads(data)


def write(path, data):
    with open(path, 'w') as f:
        if isinstance(data, dict):
            _data = json.dumps(data)
            f.write(_data)
        else:
            raise TypeError('Data is dict.')
    return True


r_data = {'name': '小龙', 'age': 18, 'top': 176}

if __name__ == '__main__':
    write('test.json', r_data)
    result = read('test.json')
    # result['sex'] = 'boy'
    # write('test.json', result)
    print(result)
