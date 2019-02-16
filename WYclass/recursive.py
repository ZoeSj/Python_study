# @File    : recursive.py
# @Date    : 2019-02-15
# @Author  : shengjia
def recursive(number):
    if number <= 1:
        return 1
    else:
        return number * recursive(number - 1)
    print(number)
