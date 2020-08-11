# @File    : practice_2.py
# @Date    : 2020-08-11
# @Author  : shengjia
# Find the perfect number within 10000
import math

for num in range(1, 10000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            if 1 < factor != num // factor:
                result += num // factor
    if result == num:
        print(num)
