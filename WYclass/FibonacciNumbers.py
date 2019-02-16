# @File    : FibonacciNumbers.py
# @Date    : 2019-02-16
# @Author  : shengjia
def fibonacci(number):
    print("fibonacci"+str(number))
    # if number == 0:
    #     return 0
    # elif number == 1:
    #     return 1
    if number < 2:
        return number
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


def fibonacciTwo(n):
    print("fibonacci" + str(n))
    terms = [0, 1]
    i = 2
    while i <= n:
        terms.append(terms[i - 1] + terms[i - 2])
        i = i + 1
    return terms[n]


fibonacciNumber = fibonacci(9)
# fibonacci execute 108
# fibonacciTwo execute 1
print(fibonacciNumber)
