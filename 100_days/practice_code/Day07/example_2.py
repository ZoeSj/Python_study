# @File    : example_2.py
# @Date    : 2020-08-11
# @Author  : shengjia

# 字典是另一种可变容器模型，Python中的字典跟我们生活中使用的字典是一样一样的，它可以存储任意类型对象，与列表、集合不同的是，字典的每个元素都是
# 由一个键和一个值组成的“键值对”，键和值通过冒号分开。下面的代码演示了如何定义和使用字典。
scores = {'John': 95, 'Zoe': 99, 'Mary': 98}
print(scores)

# 创建字典的构造器语法
items_one = dict(one=1, two=2, three=3, four=4)

# 通过zip函数将两个序列压成字典
items_two = dict(zip(['a', 'b', 'c'], '123'))

# 创建字典的推导式语法
items_three = {num: num ** 2 for num in range(1, 10)}

print(items_one, items_two, items_three)

# 通过键可以获取字典中对应的值

# 对字典中所有键值对进行遍历
for key in scores:
    print(f'{key}: {scores[key]}')

scores['Jack'] = 88
scores['Bella'] = 87
scores.update(冷面=67, 方启鹤=85)
print(scores)
if '武则天' in scores:
    print(scores['武则天'])
print(scores.get('武则天'))
# get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get('武则天', 60))
# 删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('骆昊', 100))
# 清空字典
scores.clear()
print(scores)
