from scrapy import cmdline
# cmdline.execute('scrapy crawl shian --nolog'.split())
# cmdline.execute('scrapy crawl maidanglao --nolog'.split())
# cmdline.execute('scrapy crawl play --nolog'.split())
cmdline.execute('scrapy crawl 36kr --nolog'.split())
# cmdline.execute('scrapy crawl 3Dhu --nolog'.split())
# cmdline.execute('scrapy crawl shian'.split())
# sel = Selector(response)
#         ul = sel.css('ul.assort_ul')
#         for i in ul:
#             link = i.css('li div.dybk_div a::attr(href)').extract()
#             print(link)