# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class Hw2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class QuoteItem(Item):
    item_mhz = Field()
    url = Field()
    price_rub = Field()
    ecname = Field()
    visited_at = Field()
    ssd = Field()
    ram = Field()