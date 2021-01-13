# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxyScraperItem(scrapy.Item):
    """
    yield {
        'scheme': scheme,
        'proxy': proxy,
        'port': port        
        }
    """    
    _id = scrapy.Field()
    scheme = scrapy.Field()
    proxy =scrapy.Field()
    port=scrapy.Field()