# @File    : practice.py
# @Date    : 2020-08-05
# @Author  : shengjia

a = 131
b = 12
c = 1 + 5j
print(a + b)
print(a - b)
print(type(a * b))
print(type(a / b))
print(type(a % b))
print(type(c))

flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)

print(flag0)
print(flag1)
print(flag2)
print(flag3)
print(flag4)
print(flag5)
