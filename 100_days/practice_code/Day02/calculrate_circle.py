# @File    : calculrate_circle.py
# @Date    : 2020-08-05
# @Author  : shengjia

radius = float(input('please input radius:'))
girth = 2 * 3.1416 * radius
area = 3.1416 * radius * radius
print(f'周长：{girth:.2f}')
print(f'面积：{area:.2f}')

print('周长: %.2f' % girth)
print('面积: %.2f' % area)
