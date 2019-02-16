# @File    : recursive.py
# @Date    : 2019-02-15
# @Author  : shengjia
# returns the factorial of the argument number
def factorial(number):
    product = 1
    for i in range(number):
        product = product * (i + 1)
    return product

num = 5
factorial_of_user_input = factorial(num)
print(factorial_of_user_input)
