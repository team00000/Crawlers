import smtplib,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

class Emailcls(object):
    def __init__(self,smtplib_SMTP,fromaddr,password,toaddrs,chao):
        self.smtplib_SMTP = smtplib_SMTP
        self.fromaddr = fromaddr
        self.password = password
        self.toaddrs = toaddrs
        self.chao = chao

    def func_email(self,path,title='无标题',subject='无内容'):
        #设置服务器信息
        fromaddr = self.fromaddr
        password = self.password
        toaddrs = self.toaddrs
        chao = self.chao


        #邮件内容
        #邮件内容设置
        message = MIMEMultipart()
        message.attach(MIMEText(subject,'plain','utf-8'))
        #邮件主题
        message['Subject'] = title
        #发送方信息
        message['From'] = self.fromaddr
        #接收方信息
        message['To'] = ';'.join(self.toaddrs)
        #抄送方信息
        message['Cc'] = ';'.join(self.chao)




        if path:
            file_name_list = path
            for file_name in file_name_list:
                attachment = MIMEBase('application', 'octet-stream')  # 参数的意义未深究
                attachment.set_payload(open(file_name, 'rb').read())
                encoders.encode_base64(attachment)
                attachment.add_header('Content-Disposition', 'attachment', filename=file_name)  # 前2个参数意义未深究
                message.attach(attachment)


        try:
            server = smtplib.SMTP(self.smtplib_SMTP)
            server.login(fromaddr,password)
            server.sendmail(fromaddr,toaddrs+self.chao,message.as_string())
            print('Success')
            server.quit()
        except smtplib.SMTPException as e:
            print(e)