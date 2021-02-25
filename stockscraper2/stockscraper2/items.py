# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Stockscraper2Item(scrapy.Item):
    read_time = scrapy.Field()
    stock_volume = scrapy.Field()
    now_price = scrapy.Field()
    max_price = scrapy.Field()
    min_price = scrapy.Field()
    stock_code = scrapy.Field()
