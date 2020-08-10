# @File    : is_bissextile.py
# @Date    : 2020-08-05
# @Author  : shengjia

year = float(input('plaese input year:'))
is_leap = year % 4 == 0 and year % 100 != 0 or \
          year % 400 == 0
print(is_leap)
