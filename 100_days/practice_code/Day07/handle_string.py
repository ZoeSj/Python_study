# @File    : handle_string.py
# @Date    : 2020-08-31
# @Author  : shengjia

str1 = 'hello, world!'

# calculate the length of string
print(len(str1))

# get a copy of the first letter of the string
print(str1.capitalize())

# get a capitalized copy of each world in the string
print(str1.title())

# get all string change capitalized
print(str1.upper())

# find substring location from string
print(str1.find('or'))

# check the string is start with the appointed letter.
print(str1.startswith('h'))
print(str1.startswith('H'))

# check the string is end with the appointed letter.
print(str1.endswith('H'))

# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))

# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))
str2 = 'abc123456'

# 检查字符串是否由数字构成
print(str2.isdigit())  # False

# 检查字符串是否以字母构成
print(str2.isalpha())  # False

# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True
str3 = '  jackfrued@126.com '
print(str3)

# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())

a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))

a, b = 5, 10
print('{0} * {1} = {2}'.format(a, b, a * b))

a, b = 5, 10
print(f'{a} * {b} = {a * b}')