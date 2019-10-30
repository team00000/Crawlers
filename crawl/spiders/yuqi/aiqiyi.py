import  scrapy
from scrapy import  Spider,Request

from urllib.parse import urlencode

import  json
class lovemovieSpider(Spider):
    name = 'lovemovie'
    allowed_domains = []
    start_urls = ['https://list.iqiyi.com/']

    def start_requests(self):
        base_url = 'https://pcw-api.iqiyi.com/search/video/videolists?'
        for page in range(1, self.settings.get('PAGE') + 1):
            params = {
                'access_play_control_platform': '14',
                'channel_id': '1',
                'data_type': '1',
                'from': 'pcw_list',
                'mode': '11',
                'pageNum': page,
                'pageSize': '48',
                'site': 'iqiyi',
                'three_category_id': '6;must',
                'without_qipu': '1'
            }
            url = base_url + urlencode(params)
            yield Request(url, callback=self.parse)  # 迭代器的作用是可以实现翻页

            def parse(self, response):

                result = json.loads(response.text)
                if result.get('data').get('list'):  # 开始解析
                    items = result.get('data').get('list')
                    aiqiyifilm_info = AiqiyiItem()  # 首先实例化item.py 模块
                    for item in items:
                        aiqiyifilm_info['film_description'] = item.get('description')
                        aiqiyifilm_info['full_time'] = item.get('duration')
                        aiqiyifilm_info['formatperiod'] = item.get('formatPeriod')
                        aiqiyifilm_info['film_name'] = item.get('name')

                        yield aiqiyifilm_info


