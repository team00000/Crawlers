import requests
from lxml import etree
import pymongo
db = pymongo.MongoClient()['ku']['biao']

class Login(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'Host': '106.13.160.14:8001'
        }
        self.login_url = 'http://106.13.160.14:8001/login/'
        self.session = requests.Session()

    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        token = selector.xpath('//div[@class="card-body"]/form/input[1]/@value')
        return token

    def login(self, username, password):
        data = {
            'csrfmiddlewaretoken': self.token(),
            'next': '',
            'password': password,
            'username': username
        }
        response = self.session.post(self.login_url, data=data, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)

    def profile(self, html):
        selector = etree.HTML(html)
        # company = selector.xpath('//table[@class="table"]/tbody/tr[1]/td//text()')
        tdlist = selector.xpath('//table[@class="table"]/tbody/tr')
        for tdli in tdlist:
            company = tdli.xpath('td//text()')
            print(company)
            dd = {'title':company}
            db.insert(dd)


if __name__ == '__main__':
    login = Login()
    login.login('wsl15651190407', 'qweASDzxc')
