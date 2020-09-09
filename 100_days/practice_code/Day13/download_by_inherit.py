# @File    : download_by_inherit.py
# @Date    : 2020-09-09
# @Author  : shengjia

from random import randint
from threading import Thread
from time import time, sleep


class DownloadTask(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('start download %s' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s finished download,used about %d s' % (self._filename, time_to_download))


def main():
    start = time()
    t1 = DownloadTask('test.pdf')
    t1.start()
    t2 = DownloadTask('rs.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('all used about %d s' % (end - start))


if __name__ == '__main__':
    main()
