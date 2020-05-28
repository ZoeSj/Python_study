# @File    : nester.py
# @Date    : 2020-05-26
# @Author  : shengjia

def print_lol(the_list, level):
    for name in the_list:
        if isinstance(name, list):
            print_lol(name, level + 1)

        else:
            for tab_stop in range(level):
                print("\t")
            print(name)
