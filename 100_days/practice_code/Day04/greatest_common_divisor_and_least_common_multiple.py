# @File    : greatest_common_divisor_and_least_common_multiple.py
# @Date    : 2020-08-11
# @Author  : shengjia

x = int(input('please input x:'))
y = int(input('please input y:'))
if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('the greatest common divisor of %d and %d is %d' % (x, y, factor))
        print('the least common multiple of %d and %d is %d' % (x, y, x * y // factor))
        break
