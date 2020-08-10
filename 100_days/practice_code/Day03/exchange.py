# @File    : exchange.py
# @Date    : 2020-08-05
# @Author  : shengjia

value = float(input('please input length:'))
unit = input('please input unit:')
if unit == 'in' or unit == 'cm':
    print(f'{value: 0.2f} int = {value*2.54:0.2f} cm')
elif unit == 'cm':
    print(f'{value: 0.2f} cm = {value/2.54:0.2f} int')
else:
    print('please input valid unit')
