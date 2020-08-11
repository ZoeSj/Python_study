# @File    : examples.py
# @Date    : 2020-08-11
# @Author  : shengjia
from random import randint

# Find the number of daffodils
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)

# Reverse of positive integer
num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)

# 100 for 100 chicken
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + y * 3 + z * 1 / 3 == 100:
            print('should buy %d rooster, %d hen ,%d chick' % (x, y, z))

# CRAPS game
money = 1000
while money > 0:
    print('your total assets is:%d' % money)
    need_go_on = False
    while True:
        debt = int(input('please bet:'))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('player shakes %d points' % first)
    if first == 7 or first == 11:
        print('player win!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('banker win!')
        money -= debt
    else:
        need_go_on = True
    while need_go_on:
        current = randint(1, 6) + randint(1, 6)
        if current == 7:
            print('banker win!')
            money -= debt
        elif current == first:
            print('player win!')
            money += debt
        else:
            need_go_on = True
    print('you have break out!')
