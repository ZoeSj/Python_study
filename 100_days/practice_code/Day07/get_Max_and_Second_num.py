# @File    : get_Max_and_Second_num.py
# @Date    : 2020-08-31
# @Author  : shengjia

def get_max_and_second_num(list):
    m1, m2 = (list[0], list[1]) if list[0] > list[1] else (list[1], list[0])
    for i in range(2, len(list)):
        if list[i] > m1:
            m2 = m1
            m1 = list[i]
        elif list[i] > m2:
            m2 = list[i]
    print(m1)
    print(m2)
    return m1, m2


if __name__ == '__main__':
    list = [1, 3, 4, 2, 100, 29]
    get_max_and_second_num(list)
