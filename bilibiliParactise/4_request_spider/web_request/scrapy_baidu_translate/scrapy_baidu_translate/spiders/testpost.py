import json
import scrapy

class TestpostSpider(scrapy.Spider):
    name = 'testpost'
    allowed_domains = ['fanyi.baidu.com']

    # 对于post请求需要携带参数的，这个起始url和parse不管用
    # start_urls = ['https://fanyi.baidu.com/sug']
    #
    # def parse(self, response):
    #     pass

    # post请求需要用
    def start_requests(self):
        # 起始url
        url = 'https://fanyi.baidu.com/sug'

        data = {
            'kw': 'final'
        }

        yield scrapy.FormRequest(url=url,formdata=data,callback=self.parse_second)

    def parse_second(self,response):

        content = response.text
        obj = json.loads(content,encoding='utf-8')
        print(obj)