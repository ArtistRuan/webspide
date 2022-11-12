from datetime import date

import scrapy
# 导包，将爬取到的数据进行保存
from scrapy_dangdang.items import ScrapyDangdangItem


class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['category.dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.47.11.00.00.00.html']

    page = 1
    base_url = 'http://category.dangdang.com/pg'

    def parse(self, response):
        # pipelines 下载数据
        # items 定义下载数据
        # src = //*[@id="component_59"]/li//img/@src
        # alt = //*[@id="component_59"]/li//img/@alt
        # price = //*[@id="component_59"]/li//span[@class="search_now_price"]/text()

        print('======================')
        # 所有seletor对象，都可以再次调用xpath方法
        # 由于上述几个属性数据都在li下，所以先解析li
        li_list = response.xpath('//*[@id="component_59"]/li')
        # li_list = response.xpath('//ul[@id="component_59"]/li')

        # print(f'li_list={li_list}')
        # 循环li下面数据
        for li in li_list:
            # 因为懒加载，src属性正确对应data-orginal
            # src = li.xpath('.//img/@src').extract_first()
            src = li.xpath('.//img/@data-original').extract_first()
            # 对于第一个没有懒加载的标签，是没有data-original的，只有src，所以判断处理
            if src:
                pass
            else:
                src = li.xpath('.//img/@src').extract_first()
            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//span[@class="search_now_price"]/text()').extract_first()
            # 打印数据，查看数据情况
            print(src,name,price)

            """ 查看这几条打印的数据来看，图片的url都是一样的，分析原因是反爬“懒加载”
            images/model/guan/url_none.png  肖秀荣2023考研政治 肖秀荣考研政治2023 知识点精讲精练+肖秀荣1000题+肖四肖八 全套8本 101思想政治理论 ¥167.00
            images/model/guan/url_none.png  备考2023 一级建造师2022教材建筑 一建2022建筑实务教材官方 一级建造师教材 一建历年真题试卷 一建考试用书全 ¥269.80
            images/model/guan/url_none.png  公务员考试用书2023 粉笔公考 粉笔行测5000题 申论100题全套14本 国考省考公务员行测题库专项模块 言语理解判 ¥379.00
            """

            """ 解决懒加载后，发现第一条数据的src是none，因为第一张图片没有data-original，原因是第一张不需要懒加载，故不需要data-original，用src即可
            None  申论的规矩2023版 粉笔公考 国考省考通用 ¥64.00
            //img3m8.ddimg.cn/46/24/11166729598-1_b_2.jpg  教师资格证2022小学 中学 高中 教师资格证考试用书 公共课全套视频+全套题库+教师资格面试相关课程 云考点网校 收到 ¥20.00
            //img3m0.ddimg.cn/12/5/11146796310-1_b_4.jpg  注册安全工程师2022教材视频 其他化工建筑施工安全 双网校:环球网校视频课程题库+嗨学网价值1000元精讲视频题库 历 ¥30.00
            """

            # 爬取到的数据，需要保存，可以使用pipelines
            # 定义一个对象（需要导包，编译报错不影响任何操作）
            book = ScrapyDangdangItem(src=src,name=name,price=price)

            # 获取到一个book就交给pilelines: yield 对象名
            yield book


            # http://category.dangdang.com/pg2-cp01.47.11.00.00.00.html
            # http://category.dangdang.com/pg3-cp01.47.11.00.00.00.html

            # 多页爬取:每一页爬取的逻辑都是一样的，所以只需要将执行的url请求再次调用parse方法即可
            if self.page < 100:
                self.page = self.page + 1

                url = self.base_url + str(self.page) + '-cp01.47.11.00.00.00.html'

                # 调用parse方法
                # scrapy.Request就是scrapy的get请求
                # url就是请求地址
                # callback是执行的函数，注意不需要加()
                yield scrapy.Request(url=url,callback=self.parse)