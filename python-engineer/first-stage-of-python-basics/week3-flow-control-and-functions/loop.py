# coding:utf-8

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i} x {j} = {i * j}', end='  ')
    print('')

print('')

i = 0
j = 0
while i < 9:
    i += 1
    while j < 9:
        j += 1
        print(f'{i} x {j} = {i * j}', end='  ')
        if i == j:
            j = 0
            print('')
            break
