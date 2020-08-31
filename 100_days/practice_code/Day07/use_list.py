# @File    : use_list.py
# @Date    : 2020-08-31
# @Author  : shengjia

'''
不知道大家是否注意到，刚才我们讲到的字符串类型（str）和之前我们讲到的数值类型（int和float）有一些区别。数值类型是标量类型，也就是说这种类型的对象没有可以访问的内部结构；而字符串类型是一种结构化的、非标量类型，所以才会有一系列的属性和方法。接下来我们要介绍的列表（list），也是一种结构化的、非标量类型，它是值的有序序列，每个值都可以通过索引进行标识，定义列表可以将列表的元素放在[]中，多个元素用,进行分隔，可以使用for循环对列表元素进行遍历，也可以使用[]或[:]运算符取出列表中的一个或多个元素。
'''

list1 = [1, 3, 4, 20, 33, 22.4, 555]

# duplicate num after * for list
print(list1 * 3)

# calculate the length of list
print(len(list1))

# get value in list
print(list1[4])

# 通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index])

# 通过for循环遍历列表元素
for elem in list1:
    print(elem)

# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)

# 添加元素
list1.append(200)
list1.insert(1, 400)

# 合并两个列表
# list1.extend([1000, 2000])
list1 += [1000, 2000]
print(list1)  # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
print(len(list1))  # 9

# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list1:
    list1.remove(3)
if 1234 in list1:
    list1.remove(1234)

print(list1)  # [1, 400, 5, 7, 100, 200, 1000, 2000]

# 从指定的位置删除元素
list1.pop(0)
list1.pop(len(list1) - 1)
print(list1)  # [400, 5, 7, 100, 200, 1000]

# 清空列表元素
list1.clear()
print(list1)  # []

# 和字符串一样，列表也可以做切片操作，通过切片操作我们可以实现对列表的复制或者将列表中的一部分取出来创建出新的列表
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
print(fruits)

# list slice
fruits2 = fruits[1:4]
print(fruits2)

# The list can be copied by a full slice operation
fruits3 = fruits[:]
print(fruits3)  # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
fruits4 = fruits[-3:-1]
print(fruits4)

# You can get a copy of the inverted list through the reverse slicing operation
fruits5 = fruits[::-1]
print(fruits5)  # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']


