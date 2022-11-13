import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_dushu.items import ScrapyDushuItem


class DushuSpider(CrawlSpider):
    name = 'dushu'
    allowed_domains = ['www.dushu.com']
    # ☆☆☆☆☆这个首页的url中，没有正则匹配对应的数字，所以首页匹配不上，不会爬取到数据
    # ☆☆☆☆☆解决方式：改为带数字，可以匹配正则的
    # start_urls = ['https://www.dushu.com/book/1188.html']
    start_urls = ['https://www.dushu.com/book/1188_1.html']

    rules = (
        # follow表示是否往后继续翻页爬取，True表示翻页爬，False表示只爬当前页看到的若干页码对应页面
        # Rule(LinkExtractor(allow=r'/book/1188_\d+\.html'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'/book/1188_\d+\.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()

        img_list = response.xpath('//div[@class="bookslist"]//img')

        for img in img_list:
            name = img.xpath('./@alt').extract_first()
            src = img.xpath('./@data-original').extract_first()

            book = ScrapyDushuItem(name=name,src=src)
            yield book

        # return item
