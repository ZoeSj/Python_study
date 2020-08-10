# @File    : convert_fahrenheit_to_celsius.py
# @Date    : 2020-08-05
# @Author  : shengjia
# Convert Fahrenheit to Celsius

f = float(input("please input fahrenheit:"))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')
