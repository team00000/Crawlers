import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


# 设置服务器信息
fromaddr = "wsl15651190407@163.com"
password = "15651190407wang" # 邮箱授权码
toaddrs = ['18662760855@126.com']

# 邮件内容
# 邮件内容设置
message = MIMEText('hello,wsl','plain','utf-8')
# 邮箱主题
message['Subject'] = 'wsl text email'
# 发送方信息
message['From'] = fromaddr
# 接受方信息
message['To'] = toaddrs
try:
    server = smtplib.SMTP('smtp.163.com')
    server.login(fromaddr, password)
    server.sendmail(fromaddr, toaddrs, message.as_string())
    print("Scuuess")
    server.quit()
except smtplib.SMTPException as e:
    print(e)