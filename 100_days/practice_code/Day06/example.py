# coding=utf-8
# @File    : example.py
# @Date    : 2020-08-11
# @Author  : shengjia
from random import randint


def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a + b + c


# If no parameters are specified,then use the default values ​​to shake two dice
print(roll_dice())
# Shake three dice
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# When passing parameters, you can pass them out of the set order
print(add(c=50, a=100, b=200))


# 在参数名前面的*表示args是一个可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total


# 在调用add函数时可以传入0个或多个参数
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))

# 将求阶乘的功能封装成一个函数
def factorial(n):
    result = 1
    for num in range(1, n + 1):
        result *= num
    return result


print(factorial(7) // factorial(3) // factorial(4))
