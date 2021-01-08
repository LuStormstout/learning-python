# coding: utf-8

import yaml


def read(path):
    with open(path, 'r') as f:
        data = f.read()
        result = yaml.load(data, Loader=yaml.FullLoader)
    return result


if __name__ == '__main__':
    read_result = read('muke.yaml')
    print(read_result)
