# @File    : prime_numbers.py
# @Date    : 2020-08-11
# @Author  : shengjia
from math import sqrt

all_nums = []
for i in range(101):
    is_prime = True
    end = int(sqrt(i))
    for x in range(2, end + 1):
        if i % x == 0:
            is_prime = False
            break
    if is_prime and i != 1:
        all_nums.append(i)

print(all_nums)
