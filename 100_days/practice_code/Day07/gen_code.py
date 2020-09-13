# 设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
"""
生成指定长度的验证码

:param code_len: 验证码的长度(默认4个字符)

:return: 由大小写英文字母和数字构成的随机验证码
"""
import random


def generate_code(code_length=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_post = len(all_chars) - 1
    code = ''
    for _ in range(code_length):
        index = random.randint(0, last_post)
        code += all_chars[index]
    print(code)


if __name__ == '__main__':
    generate_code()
