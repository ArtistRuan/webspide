import scrapy


class Example58Spider(scrapy.Spider):
    name = 'example58'
    allowed_domains = ['sz.58.com']
    start_urls = ['http://sz.58.com/']

    def parse(self, response):
        pass
