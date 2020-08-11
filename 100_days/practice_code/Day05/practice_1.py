# @File    : practice_1.py
# @Date    : 2020-08-11
# @Author  : shengjia
# Generate the first 20 numbers of the Fibonacci sequence
from __future__ import print_function

count = 0
num = [1, 1]
while count < 18:
    length = len(num)
    new_num = num[length - 1] + num[length - 2]
    num.append(new_num)
    count += 1
print(num)

a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')
