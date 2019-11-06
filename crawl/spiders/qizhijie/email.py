from youxiang import *

from bs4 import BeautifulSoup

smtplib_SMTP='smtp.163.com'
fromaddr = "qzj_1651@163.com"
password = "qzj12345"
toaddrs = ['13603217363@163.com']
chao=['13603217363@163.com','lly1519980488@163.com']


a = Emailcls(smtplib_SMTP,fromaddr,password,toaddrs,chao)
a.func_email(["D:\\12"],title='默认无标题',subject='这就是内容')
