# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapydemo58Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    house_name = scrapy.Field()
    house_address = scrapy.Field()
    house_unit_price = scrapy.Field()

