# @File    : requires.py
# @Date    : 2020-09-09
# @Author  : shengjia

from time import time
from threading import Thread

import requests


class DownloadHanlder(Thread):
    def __init__(self, url):
        super().__init__()
        self._url = url

    def run(self):
        filename = self._url[self._url.rfind('/') + 1:]
        resp = requests.get(self._url)
        with open('/user/' + filename, 'wb') as f:
            f.write(resp.content)


"""
    通过requires的get获取网络资源
    下面的代码中使用了天行数据接口提供的网络API
    要使用该数据接口需要在天行数据的网站上注册
    然后用自己的Key替换掉下面代码的中APIKey即可
"""


def main():
    resp = requests.get(
        'http://api.tianapi.com/meinv/?key=APIKey&num=10')
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
    # 通过多线程的方式实现图片下载
    DownloadHanlder(url).start()


if __name__ == '__main__':
    main()
