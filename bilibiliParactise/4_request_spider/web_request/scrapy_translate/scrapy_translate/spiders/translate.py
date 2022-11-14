import json
import os
# glob模块提供了函数用于从目录通配符搜索中生成文件列表
import glob
import scrapy


class TranslateSpider(scrapy.Spider):
    name = 'translate'
    allowed_domains = ['fanyi.baidu.com']
    # start_urls = ['https://fanyi.baidu.com/sug']
    #
    # def parse(self, response):
    #     pass

    log_path = 'log/'

    # 如果没有log目录，就创建，避免报错
    if not os.path.exists(log_path):
        os.mkdir(log_path)

    # 如果有log目录，就判断有没有文件，有log文件就删除log文件
    for infile in glob.glob(os.path.join(log_path,'*.log')):
        os.remove(infile)



    # post
    def start_requests(self):

        url = 'https://fanyi.baidu.com/sug'
        word = input("请输入要查询的内容:")

        data = {
            # 'kw':'final'
            'kw':f'{word}'
        }

        yield scrapy.FormRequest(url=url,formdata=data,callback=self.parse_second)

    def parse_second(self,response):

        content = response.text

        obj = json.loads(content)

        print(obj)