from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    sender = 'shengjiamo@163.com'
    receivers = ['shengjia@shopex.cn', '1368329355@qq.com']
    message = MIMEText('用python发送邮件的示例代码', 'plain', 'utf-8')
    message['from'] = Header('zoe', 'utf-8')
    message['to'] = Header('John', 'utf-8')
    message['subject'] = Header('示例代码邮件', 'utf-8')
    smtper = SMTP('smtp.126.com')
    smtper.login(sender, 'secretpass')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成')


if __name__ == '__main__':
    main()
