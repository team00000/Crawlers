# import requests
#
#
# ssion=requests.session()
# headers={
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
# }
#
# data={'login_field':'13603217363@163.com','password':'chenmoshijin5418'}
#
#
# print(ssion.post('https://github.com/session',data=data,verify = False).text)
#
#
#


# https://www.cnblogs.com/wintest/p/11183744.html

import requests
import re
import urllib3
urllib3.disable_warnings()

class Github_Login():

    def __init__(self):
        # 设置Session
        self.s = requests.session()
        # 设置请求头
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
        }
        # 在使用Fiddler时进行请求，通过该代码忽略SSLError错误
        self.s.verify = False

    # 获取 authenticity_token
    def get_authenticity_token(self):
        login_url = "https://github.com/login"
        r = self.s.get(login_url, headers = self.headers)
        authenticity_token = re.findall('<input type="hidden" name="authenticity_token" value="(.+?)" />', r.text)
        print("authenticity_token：{}".format(authenticity_token))
        return authenticity_token[0]

    # 模拟登录，并返回 title
    def github_login(self, authenticity_token, username, password):
        session_url = "https://github.com/session"
        body = {
            "authenticity_token":authenticity_token,
            "commit":"Sign in",
            "login":username,
            "password":password,
            "utf8":"✓",
            "webauthn-support":"unknown",
            "webauthn - iuvpaa - support": "supported",

        }
        r = self.s.post(session_url, headers = self.headers, data = body)
        title = re.findall('<title>(.+?)</title>',r.text)
        print("title：%s" %title[0])
        return title[0]

    # 通过 title 判断是否登录成功
    def is_login_success(self, title):
        if "GitHub" == title:
            return True
        else:
            return False

if __name__ == '__main__':
    github = Github_Login()
    authenticity_token = github.get_authenticity_token()
    title = github.github_login(authenticity_token, username="13603217363@163.com", password="chenmoshijin5418")
    login_result = github.is_login_success(title)
    print(login_result)