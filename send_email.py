import smtplib
from email.mime.text import MIMEText
from threading import Thread
from time import sleep


class EmailThread(Thread):
    def __init__(self):
        super().__init__()

    def run(self, delay=0.1):
        while True:
            for i in ['-', '\\', '|', '/']:
                print("\b%s" % i, end='', flush=True)
                sleep(delay)


class Email(object):
    def __init__(self, sender=None, receivers=None):
        self._sender = sender
        self._receivers = receivers
        self._message = None
        self._subject = None
        self._host = None
        self._user = None
        self._password = None

    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, sender):
        """设置发送人"""
        self._sender = sender

    @property
    def receivers(self):
        return self._receivers

    @receivers.setter
    def receivers(self, receivers):
        """设置接受人，应该为列表，但是一次发多个又出现问题"""
        self._receivers = [receivers,]

    def setMessage(self, message=None):
        """设置发送信息"""
        self._message = message

    def setSubject(self, subject="No Subject"):
        """设置邮件主题"""
        self._subject = subject

    def setHost(self, host="smtp.126.com"):
        """设置服务器"""
        self._host = host

    def setAccount(self, user, password):
        """设置账户密码"""
        self._user = user
        self._password = password

    def send(self, text_format='plain', encoding='utf-8'):
        """发送邮件"""
        print("正在发送邮件 ", end='')
        prompt = EmailThread()
        prompt.setDaemon(True)
        prompt.start()
        message = MIMEText(self._message, text_format, encoding)

        message["From"] = self._sender
        message["To"] = self._receivers[0]
        message["Subject"] = self._subject

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self._host, 25)
            smtpObj.login(self._user, self._password)
            smtpObj.sendmail(self._sender, self._receivers, message.as_string())
            print("\b\n邮件发送成功")
        except smtplib.SMTPException:
            print("\b\nError: 发送邮件失败")


if __name__ == '__main__':
    email = Email()
    email.sender = 'cyberist@126.com'
    email.receivers = '201648748@qq.com'
    email.setAccount("cyberist@126.com", "cyberist123")  # 开启授权时，使用授权码
    email.setSubject("This is a test")
    email.setHost()
    email.setMessage("Hello, this is just a test")
    email.send()


