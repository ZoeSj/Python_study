# @File    : nester.py
# @Date    : 2020-05-26
# @Author  : shengjia

def print_lol(the_list):
    for name in the_list:
        if isinstance(name, list):
            print_lol(name)

        else:
            print(name)
