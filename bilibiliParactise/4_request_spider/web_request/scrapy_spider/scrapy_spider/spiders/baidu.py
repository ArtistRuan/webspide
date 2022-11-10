import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫的名字，用于运行爬虫时使用的值
    name = 'baidu'
    # 允许访问的域名
    allowed_domains = ['www.baidu.com']
    # 起始的url地址
    start_urls = ['http://www.baidu.com/']

    # 执行了start_urls之后执行的方法，方法中的response是返回的对象
    # 相当于 response = requests.get()
    #       response = urllib.request.urlopen()
    def parse(self, response):
        print('如果可以打印这句话，证明没有反爬，否则有反爬')
