# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import urllib

from itemadapter import ItemAdapter

# 如果想要使用管道，需要在settings中开启管道
class ScrapyDangdangPipeline:

    # 爬虫程序开启前就打开
    def open_spider(self,spider):
        # 因为没有关闭，所以mode='w'是可以的，一直写
        self.fp = open('book.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        # item就是yield后面的boog对象

        # 以下这种模式在开发中不常见，也不推荐，因为每传来一个对象，就打开一次文件，对文件的操作过于频繁，定义open_spider()和close_spider()
        # with open('book.json','a',encoding='utf-8') as fp:
        #     fp.write(str(item))

        # 文件打开后，进行持续写操作
        self.fp.write(str(item))

        return item

    # 爬虫程序结束后才关闭
    def close_spider(self,spider):
        self.fp.close()

# 开启多管道
    # 1 定义管道类
    # 2 在settings中开启管道
class DangDangDownloadPipeline:
    def process_item(self,item,spider):

        url = f'http:{item.get("src")}'
        filename = f'./books/{item.get("name")}.jpg'

        urllib.request.urlretrieve(url=url,filename=filename)

        return item