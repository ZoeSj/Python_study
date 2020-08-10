# @File    : practice.py
# @Date    : 2020-08-05
# @Author  : shengjia

# username = input('please input your name:')
# password = input('please your password:')
#
# if username == 'admin' and password == '123456':
#     print('success!')
# else:
#     print('fail!')

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x > -1:
    y = x + 2
else:
    y = 5 * x + 3

print(f'y = {y:0.2f}')

