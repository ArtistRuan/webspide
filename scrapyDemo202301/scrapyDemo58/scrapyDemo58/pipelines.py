# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Scrapydemo58Pipeline:

    # 爬虫程序开启前就打开
    def open_spider(self, spider):
        # 因为没有关闭，所以mode='w'是可以的，一直写
        self.fp = open('houses.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):

        # 文件打开后，进行持续写操作
        self.fp.write(str(item))

        return item

    # 爬虫程序结束后才关闭
    def close_spider(self, spider):
        self.fp.close()

# 保存到EXCEL或者数据库
class Scrapy58Download:
    def process_item(self,item,spider):
        pass
        return item