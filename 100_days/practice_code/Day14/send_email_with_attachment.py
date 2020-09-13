from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import urllib


def main():
    # 创建一个带有附件的邮件对象
    message = MIMEMultipart()

    # 创建文本内容
    text_content = MIMEText('附件中有本月数据，请查收！', 'plain', 'utf-8')
    message['subject'] = Header('本月数据', 'utf-8')
    # 将文本内容添加到邮件消息中
    message.attach(text_content)

    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('/User/chengjia/Desktop/test.txt', 'rb') as f:
        text = MIMEText(f.read(), 'base64', 'utf-8')
        text['Content-Type'] = 'text/plain'
        text['Content-Disposition'] = 'attachment; filename = text.txt'
        message.attach(text)

    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('/Users/chengjia/Desktop/汇总数据.xlsx', 'rb') as f:
        xls = MIMEText(f.read(), 'base64', 'utf-8')
        xls['Content-Type'] = 'application/vnd.ms-excel'
        xls['Content-Disposition'] = 'attachment; filename=month-data.xlsx'
        message.attach(xls)

    # 创建SMTP对象
    smtper = SMTP('smtp.126.com')
    # 开启安全连接
    # smtper.stattls()
    sender = 'shengjiamo@163.com'
    receivers = ['shengjia@shopex.cn']
    """
    登录到SMTP服务器
    请注意此处不是使用密码而是邮件客户端授权码进行登录
    对此有疑问的读者可以联系自己使用的邮件服务器客服
    """
    smtper.login(sender, 'pass')
    smtper.sendmail(sender, receivers, message.as_string())
    smtper.quit()
    print('发送完成！')


if __name__ == '__main__':
    main()
