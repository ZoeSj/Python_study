from socket import socket
from json import loads
from base64 import b64decode


def main():
    client = socket()
    client.connect('192.168.1.2', 5566)
    # 定义一个保存二进制数据的对象
    in_data = bytes()
    # 不知道发送数据大小，所以每次接收1024字节
    data = client.recv(1024)
    while data:
        # 将接收的数据拼接起来
        in_data += data
        data = client.recv(1024)
    # 将收到的二进制数据解码成JSON字符串并转成字典
    # loads函数的作用就是将json数据转换成字典对象
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    file_data = my_dict['file_data'].encode('utf-8')
    # 将base64格式的数据解码二进制数据并写入文件
    with open('/chengjia/' + filename, 'wb') as f:
        f.write(b64decode(file_data))
    print('图片已保存。')


if __name__ == '__main__':
    main()
