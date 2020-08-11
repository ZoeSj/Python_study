# @File    : 99table.py
# @Date    : 2020-08-10
# @Author  : shengjia
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()
