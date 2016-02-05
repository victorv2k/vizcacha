# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DiscoArticle(scrapy.Item):
    id_disco = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    unit_price = scrapy.Field()
    parents = scrapy.Field()
    oferta = scrapy.Field()
    pass
