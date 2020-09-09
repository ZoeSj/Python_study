# @File    : threading_download_by_multi.py
# @Date    : 2020-09-09
# @Author  : shengjia
from random import randint
from threading import Thread
from time import time, sleep


def download(filename):
    print('start download%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s finished download, used %d s' % (filename, time_to_download))


def main():
    start = time()
    t1 = Thread(target=download, args=('test.pdf',)).start()
    t2 = Thread(target=download, args=('test.avi',)).start()
    t1.join()
    t2.join()
    end = time()
    print('all used %d s' % (end - start))


if __name__ == '__main__':
    main()
