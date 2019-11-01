import scrapy
from scrapy import FormRequest,Request


class MoNiDL(scrapy.Spider):
    name='mndl'
    start_urls=['http://106.13.160.14:8001/']
    login_url='http://106.13.160.14:8001/login/'

    def parse(self, response):
        print(response.text)
        # pass

    def start_requests(self):
        yield scrapy.Request(self.login_url,callback=self.login)

    def login(self,response):
        formdata={
            'username':'17606141651',
            'password':'qzj123456'
        }
        yield FormRequest.from_response(response,formdata=formdata,callback=self.parse_login)

    def parse_login(self,response):
        if 'Home' in response.text:
            yield from super().start_requests()