import scrapy
from scrapy.spiders import CrawlSpider, Spider
import re
from datetime import datetime
from HW2.items import QuoteItem 

class ComputersSpider(CrawlSpider):
    name = 'computers'
    allowed_domains = ['notik.ru']
    start_urls = ["https://www.notik.ru/index/notebooks.htm?srch=true&full=&f31=20008.19262.20159.19151&page=1", "https://www.notik.ru/index/notebooks.htm?srch=true&full=&f31=20008.19262.20159.19151&page=2", "https://www.notik.ru/index/notebooks.htm?srch=true&full=&f31=20008.19262.20159.19151&page=3", "https://www.notik.ru/index/notebooks.htm?srch=true&full=&f31=20008.19262.20159.19151&page=4", "https://www.notik.ru/index/notebooks.htm?srch=true&full=&f31=20008.19262.20159.19151&page=5", "https://www.notik.ru/index/notebooks.htm?srch=true&full=&f31=20008.19262.20159.19151&page=6", "https://www.notik.ru/index/notebooks.htm?srch=true&full=&f31=20008.19262.20159.19151&page=7"]
    pages_count = 16
    default_headers = {}
    laptops = QuoteItem()
    def scrap_computers(self, response):
        laptops = QuoteItem()
        for card in response.xpath("//tr[@class='goods-list-table']"):
            name_price = card.xpath(".//td[@class='glt-cell gltc-cart']")
            laptops['item_mhz'] = re.findall(r'[0-9]+', str(card.xpath(".//td[@class='glt-cell w4'][1]/text()").extract()[2]))[0]
            laptops['url'] = 'https://www.notik.ru'+str(card.xpath(".//td[@class='glt-cell gltc-title show-mob hide-desktop']/a").attrib.get("href"))
            laptops['price_rub'] = name_price.xpath(".//a").attrib.get("ecprice")
            laptops['ecname'] = name_price.xpath(".//a").attrib.get("ecname")
            laptops['visited_at'] = f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'
            laptops['ssd'] = re.findall(r'[0-9]+', str(card.xpath(".//td[@class='glt-cell w4'][2]/text()").extract()[3]))[0]
            laptops['ram'] = re.findall(r'[0-9]+', str(card.xpath(".//td[@class='glt-cell w4']/strong/text()").extract()[2]))[0]
            yield laptops
          
    def start_requests(self):
        for page in range(1, 1 + self.pages_count):   
            url = f'https://www.notik.ru/index/notebooks.htm?srch=true&full=&f31=20008.19262.20159.19151&page={page}'
            yield scrapy.Request(url, callback=self.scrap_computers)