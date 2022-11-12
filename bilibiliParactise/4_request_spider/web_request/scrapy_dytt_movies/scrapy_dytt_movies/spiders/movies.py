import scrapy
from scrapy_dytt_movies.items import ScrapyDyttMoviesItem

"""
@autho:ruanshikao
@time:2022-11-12 22:10
"""

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['www.dygod.net']
    # start_urls = ['http://www.dygod.net']
    start_urls = ['https://www.dygod.net/html/gndy/dyzz']

    def parse(self, response):

        # //*[@id="header"]/div/div[3]/div[4]/div[2]/div[2]/div[2]//td[2]//a/@href
        # //*[@id="header"]/div/div[3]/div[4]/div[2]/div[2]/div[2]//td[2]//a/text()

        a_list = response.xpath('//*[@id="header"]/div/div[3]/div[4]/div[2]/div[2]/div[2]//td[2]//a')

        for a in a_list:
            href = a.xpath('./@href').extract_first()
            name = a.xpath('./text()').extract_first()
            # print(name,href)

            # 内页地址
            url = 'https://www.dygod.net' + href
            # print(f'url={url}')

            # 对内页发起请求（因上述第一页的逻辑与内页逻辑不一样，所以callback的方法不能用上面的parse，需要模拟自定义一个
            # 并且传入meta参数，将name传给内页的处理逻辑中
            yield scrapy.Request(url=url,callback=self.parse_second,meta={"name":name})

    def parse_second(self,response):
        src = response.xpath('//*[@id="Zoom"]/img[1]/@src').extract_first()
        print(f'https://www.dygod.net/{src}')

        # 接受上一步请求的meta参数
        name = response.meta["name"]

        # 拿到数据后，传递给item
        movie = ScrapyDyttMoviesItem(name=name,src=src)

        # 将movie返回给管道
        yield movie
