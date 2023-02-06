import scrapy

from scrapyDemo58.items import Scrapydemo58Item


class Example58Spider(scrapy.Spider):
    name = 'example58'
    allowed_domains = ['sz.58.com']
    start_urls = ['https://sz.58.com/ershoufang']

    def parse(self, response):

        print("执行了这里")

        house_name_list = response.xpath('//*[@id="esfMain"]/section/section[3]/section[1]/section[2]//@title').extract()
        house_address_list = response.xpath('//*[@id="esfMain"]//section/div[2]/p[2]//text()').extract()
        house_unit_price_list = response.xpath('//*[@id="esfMain"]/section//a/div[2]/div[2]/p[2]//text()').extract()
        # house_name_list = response.xpath('//*[@id="esfMain"]/section/section[3]/section[1]/section[2]//@title').extract_first()
        # house_name_list = response.xpath('//*[@id="esfMain"]/section/section[3]/section[1]/section[2]/div[1]/a/div[2]/div[1]/div[1]/h3/@title').extract()

        # print("类型", type(house_name_list))
        # print("获取到的楼名",house_name_list)
        # print("获取到的地址",house_address_list)
        # print("获取到的总价",house_unit_price_list)
        for i in range(len(house_name_list)):
            print(i, house_name_list[i],house_address_list[i],house_unit_price_list[i])

            houses = Scrapydemo58Item(
                house_name=house_name_list[i],
                house_address=house_address_list[i],
                house_unit_price = house_unit_price_list[i]
            )

            yield houses



