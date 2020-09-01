# @File    : YH_triangle.py
# @Date    : 2020-09-01
# @Author  : shengjia

def main(num):
    # num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


def triangles():
    L = [1]
    while True:
        yield L
        L = [sum(i) for i in zip([0] + L, L + [0])]


def triangles_another():
    L = [1]
    S = []
    while True:
        yield L
        L = [1] + S + [1]
        S = []
        for i in range(len(L) - 1):
            S.append(L[i] + L[i + 1])


def YangHui(num=10):
    LL = [[1]]
    for i in range(1, num):
        LL.append(
            [(0 if j == 0 else LL[i - 1][j - 1]) + (0 if j == len(LL[i - 1]) else LL[i - 1][j]) for j in range(i + 1)])
    print(LL)
    return LL


if __name__ == '__main__':
    main(4)
