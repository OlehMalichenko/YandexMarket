import scrapy


class YmSpider(scrapy.Spider):
    name = 'ym'
    allowed_domains = ['yandex.ru']
    start_urls = ['http://yandex.ru/']

    def parse(self, response, **kwargs):
        pass
