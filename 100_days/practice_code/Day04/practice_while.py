# @File    : practice_while.py
# @Date    : 2020-08-06
# @Author  : shengjia

import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('please input:'))
    if number < answer:
        print('bigger')
    elif number > answer:
        print('smaller')
    else:
        print('surprise! you are right!')
        break
print('you use %d times to guess!' % counter)
if counter > 7:
    print('fool')


for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()