# @File    : practice.py
# @Date    : 2020-08-11
# @Author  : shengjia
from math import sqrt


def is_leap_year():
    year = int(input('please input the year:'))
    if year % 4 == 0 and year % 100 != 0 or \
            year % 400 == 0:
        print('this year %d is leap year!' % year)
    else:
        print('this year is not!')


def get_prime_number():
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


get_prime_number()
