# -*- coding: UTF-8 -*-
# @File    : 003.py
# @Date    : 2020-05-18
# @Author  : shengjia

# 在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
# 正常解法：
# 循环查找

def find(array, value):
    # 判断数组是否为空
    if not array:
        return False
    # 获取横纵数组的长度
    rawNum = len(array)
    colNum = len([0])

    # 判断非法输入
    # 可以换成 isinstance(value, (int, float)) 进行判断
    if type(value) == float and type(array[0][0]) == int:
        if int(value) == value:
            print('no')
            return False
        value = int(value)
    elif type(value) == int and type(array[0][0]) == float:
        value = float(value)
    elif type(value) != type(array[0][0]):
        return False

    i = colNum - 1
    j = 0

    while i >= 0 and j < rawNum:
        if array[i][j] < value:
            j += 1
            print(array[i][j])
        elif array[i][j] > value:
            i -= 1
            # print(array[i][j])
        else:
            print('yeah!')
            return True


def find_integer(matrix, num):
    """
    :param matrix: [[]]
    :param num: int
    :return: bool
    """
    if not matrix:
        return False
    rows, cols = len(matrix), len(matrix[0])
    row, col = rows - 1, 0
    while row >= 0 and col <= cols - 1:
        if matrix[row][col] == num:
            return True
        elif matrix[row][col] > num:
            row -= 1
        else:
            col += 1
    return False


array = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]]

find_integer(array, 11)
