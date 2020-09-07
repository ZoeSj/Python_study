# @File    : download_noprocess.py
# @Date    : 2020-09-07
# @Author  : shengjia
from random import randint
from time import time, sleep


def download_task(filename):
    print('start downloading...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s complete download,used %.2fs' % (filename, time_to_download))


def main():
    start = time()
    download_task('Python从入门到住院.pdf')
    download_task('Peking Hot.avi')
    end = time()
    print('all used %.2fs.' % (end - start))


if __name__ == '__main__':
    main()
