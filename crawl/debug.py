from scrapy import cmdline
cmdline.execute('scrapy crawl qianbiao'.split())

# from selenium import webdriver
# browser=webdriver.Chrome()
# print(type(browser))

# a = [1,2,3]
# b = [4,5,6]
# c = zip(a,b)  #c = [(1,4),(2,5),(3,6)]
# print(list(c))
# list_new = [row[i] for i in range(len(0)) for row in c]

# import re
# a = '''<ul class="renzheng1">
#         	<li><a href="javascript:openwin('http://www.ndrc.gov.cn/');"  target="_blank" rel="nofollow">中华人民共和国发改委</a></li>
#         </ul>'''
# result = re.sub(r'[a-zA-Z]+="(.*?)"|[  ]+', '', a)
# print(result)

