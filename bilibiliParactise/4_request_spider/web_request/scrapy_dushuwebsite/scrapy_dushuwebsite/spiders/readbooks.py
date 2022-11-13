import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_dushuwebsite.items import ScrapyDushuwebsiteItem


class ReadbooksSpider(CrawlSpider):
    name = 'readbooks'
    allowed_domains = ['www.dushu.com']
    # ☆☆☆☆☆这个首页的url中，没有正则匹配对应的数字，所以首页匹配不上，不会爬取到数据
    # ☆☆☆☆☆解决方式：改为带数字，可以匹配正则的
    # start_urls = ['https://www.dushu.com/book/1188.html']
    start_urls = ['https://www.dushu.com/book/1188_1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/book/1188_\d+\.html'),
             callback='parse_item',
             # follow=True),
             follow=False),
    )

    def parse_item(self, response):

        # 每条数据都重复爬取，是这个原因吗？
        # item = {}

        # 如下3行是默认的模板
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()

        img_list = response.xpath('//div[@class="bookslist"]//img')

        for img in img_list:
            name = img.xpath('./@alt').extract_first()
            src = img.xpath('./@data-original').extract_first()

            book = ScrapyDushuwebsiteItem(name=name,src=src)

            yield book

        # 原默认模板 return
        # return item
