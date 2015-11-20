#scrapy crawl p2000 -o <datafile>.json

import scrapy
from p2000.items import *

class P2000Spider(scrapy.Spider):
    name = "p2000"
    allowed_domains = ["p2000-online.net"]
    start_urls = ["http://www.p2000-online.net/p2000.php?Pagina=%d&NoViewCaps=1&AutoRefresh=uit&Pagina=%d" %(n,n) for n in range(0, 10250)]

    def parse(self, response):
        for sel in response.xpath('//tr'):
            item = P2000Item()
            item['date'] = sel.xpath('td[1]/text()').extract()
            item['time'] = sel.xpath('td[2]/text()').extract()
            item['cause'] = sel.xpath('td[5]/text()').extract()
            yield item