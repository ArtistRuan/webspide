import scrapy


class LogdemoSpider(scrapy.Spider):
    name = 'logdemo'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com']

    def parse(self, response):


        print('+++++++++++++++++++++++++')
