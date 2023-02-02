import scrapy


class Example58Spider(scrapy.Spider):
    name = 'example58'
    allowed_domains = ['sz.58.com']
    start_urls = ['https://sz.58.com/ershoufang']

    def parse(self, response):

        print("执行了这里")

        house_name_list = response.xpath('//*[@id="esfMain"]/section/section[3]/section[1]/section[2]//@title').extract()
        # house_name_list = response.xpath('//*[@id="esfMain"]/section/section[3]/section[1]/section[2]/div[1]/a/div[2]/div[1]/div[1]/h3/@title').extract()

        print("类型", type(house_name_list))
        print("获取到的数据",house_name_list)
        # for i in range(len(house_name_list)):
        #     print(i, house_name_list[i])


