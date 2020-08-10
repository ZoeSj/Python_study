# @File    : handle_data.py
# @Date    : 2020-05-28
# @Author  : shengjia
def singleNumber(A):
    for i in A :
        # print(A.count(i))
        if A.count(i)!=2:
            print(A.count(i))
            return A[i]

list = [1,1,2,2,3,4,4]
singleNumber(list)
