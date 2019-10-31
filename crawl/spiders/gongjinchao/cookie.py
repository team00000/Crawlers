import scrapy
class PostdemoSpider(scrapy.Spider):
    name = 'postDemo'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://fanyi.baidu.com/sug']
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self, response):
        print('start_request')
        data = {'kw': 'dog'}
        for url in self.start_urls:
            yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse)
class DoubanSpider(scrapy.Spider):
    name = 'douban'
    start_urls = ['https://accounts.douban.com/j/mobile/login/basic']
    def start_requests(self):
        print('start')
        for url in self.start_urls:
            data = {
                'ck':'',
                'name':'',
                'password':'',
                'remembor':'',
                'ticket':''
            }
            yield scrapy.FormRequest(url=url,formdata=data,callback=self.parse)
    def parse(self, response):
        print('登录')
        url='https://www.douban.com/people/13382914105'
        yield scrapy.Request(url=url,callback=self.parseBySecond)
    def parseBySecond(self,response):
        print('写入')
        with open('./text.html','w',encoding='utf8') as f:
            f.write(response.text)

# import unittest
# def fun(x):
#     return x+1
# class MyTest(unittest.TestCase):
#     def test(self):
#         self.assertEqual(fun(3),4)

# class TestStringMethods(unittest.TestCase):
#     def test_upper(self):
#         self.assertEqual('foo'.upper(),'FOO')
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
#     def test_split(self):
#         s = 'hellp world'
#         self.assertEqual(s.split(),['hello','word'])
#         with self.assertRaises(TypeError):
#             s.split(2)
# if __name__ == '__main__':
#     unittest.main()

