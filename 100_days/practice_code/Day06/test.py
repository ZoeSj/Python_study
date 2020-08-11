# coding=utf-8
# @File    : test.py
# @Date    : 2020-08-11
# @Author  : shengjia
import isPalindrome as ipl
import isPrime as ipm

if __name__ == '__main__':
    num = int(input('please input number:'))
    if ipl.is_palindrome(num) and ipm.is_prime(num):
        print('%d是回文素数' % num)
    else:
        print('%d不是回文素数' % num)
