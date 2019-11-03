from newspaper import Article
url = 'https://www.81uav.cn/uav-news/'
news = Article(url,language='zh')
news.download()
news.parse()
a = news.imgs
for i in a:
    print(i)





