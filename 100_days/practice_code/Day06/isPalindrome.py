# @File    : isPalindrome.py
# @Date    : 2020-08-11
# @Author  : shengjia

def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = temp * 10 + temp % 10
        temp //= 10
    return total == num


# print(is_palindrome(1000))
