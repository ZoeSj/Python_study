# @File    : nester.py
# @Date    : 2020-05-26
# @Author  : shengjia
import sys


def print_lol(the_list, indent=False, level=0, fn=sys.stdout):
    for name in the_list:
        if isinstance(name, list):
            print_lol(name, indent, level + 1, fn)

        else:
            if indent:
                for tab_stop in range(level):
                    print("\t")
                print(name)
