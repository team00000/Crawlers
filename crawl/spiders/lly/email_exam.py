# from crawl.spiders.lly.email_jiankong import *
from email_jiankong import *

from bs4 import BeautifulSoup

smtplib_SMTP='smtp.163.com'
fromaddr = "lly1519980488@163.com"
password = "lly314159261011"
toaddrs = ['qzj_1651@163.com']
chao=['13603217363@163.com']


a = Emailcls(smtplib_SMTP,fromaddr,password,toaddrs,chao)
a.func_email(["D:\\附件成功.jpg"],title='默认无标题',subject='这就是内容')