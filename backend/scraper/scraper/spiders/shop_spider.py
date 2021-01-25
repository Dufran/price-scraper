import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import Item

class ShopSpider(CrawlSpider):
    name='shop'
    start_urls = ['https://www.olx.ua/list/?search%5Bad_homepage_to%3Afrom%5D=2021-01-24"&"page=1']
    
    rules = (
        Rule(LinkExtractor(allow=('page=', )), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        items=Item()
        name=response.css(".detailsLink ").css("strong ::text").extract()
        price=response.css(".price::text").extract()
        shop='olx'
        items['name']=name
        items['price']=price
        items['shop']=shop
        yield items


