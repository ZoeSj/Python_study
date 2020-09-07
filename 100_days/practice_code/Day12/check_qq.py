# @File    : check_qq.py
# @Date    : 2020-09-07
# @Author  : shengjia
"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""
import re


def main():
    try:
        username = print(input('please input your name:'))
        qq = print(input('please input your qq:'))
        m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
        if not m1:
            print('请输入有效的用户名.')
        m2 = re.match(r'^[1-9]\d{4,11}$', qq)
        if not m2:
            print('请输入有效的QQ号.')
        if m1 and m2:
            print('你输入的信息是有效的!')
    except TypeError:
        print('类型错误')


if __name__ == '__main__':
    main()
