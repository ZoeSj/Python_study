# @File    : sort.py
# @Date    : 2019-02-16
# @Author  : shengjia
# https://mp.weixin.qq.com/s/vn3KiV-ez79FmbZ36SX9lg
# https://blog.csdn.net/qq_33414271/article/details/78522235

listN = [-1, 3, 1, 5, -6, 0, 1, 9, 8]


# bubbleSort
def sortList(list):
    i = 0
    for j in range(len(list)):
        while list[i] > list[j]:  # loop the number in list with all after its numbers
            list[i], list[j] = list[j], list[i]
            i = i + 1
    if list[0] > list[1]:
        sortList(list)
    return list


def insertionSort(list):
    for index in range(1, len(list)):
        value = list[index]
        i = index - 1
        while i >= 0 and (value < list[i]):
            list[i + 1] = list[i]  # shift number in slot i right to slot i+1
            list[i] = value  # shift value left into slot i
            i = i - 1
    return list


def selectionSort(list):
    for i in range(len(list) - 1):
        minIndex = i  # record the minIndex
        for j in range(i + 1, len(list)):
            if list[j] < list[minIndex]:
                minIndex = j
        if i != minIndex:  # shift i with the minIndex
            list[i], list[minIndex] = list[minIndex], list[i]
    return list


print(sortList(listN))
