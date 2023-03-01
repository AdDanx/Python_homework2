import scrapy
from scrapy.spiders import CrawlSpider, Spider
import re
from datetime import datetime
from HW2.items import QuoteItem
from scrapy_selenium import SeleniumRequest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class CitilinkSpider(scrapy.Spider):
    name = "citilink"
    allowed_domains = ["citilink.ru"]
    start_urls = ["https://www.citilink.ru/catalog/noutbuki/?view_type=list"]
    pages_count = 22
    default_headers = {}
    laptops = QuoteItem()
    
    def parse(self, response):
        laptops = QuoteItem()
        
        with open('image.png', 'wb') as image_file:
                    image_file.write(response.meta['screenshot'])
                    
        for card in response.xpath(".//div[@class='e12wdlvo0 app-catalog-1bogmvw e1loosed0']"):
            
            laptops['item_mhz'] = float(re.findall(r'[0-9]+\.[0-9]+', str(card.xpath(".//ul[@class='app-catalog-q1moq7 e4qu3683']/li[2]/text()").extract()))[0])*1000
            laptops['url'] = 'https://www.citilink.ru'+str(card.xpath(".//a[@class='app-catalog-9gnskf e1259i3g0']").attrib.get("href"))
            laptops['price_rub'] = card.xpath(".//span[@data-meta-price]").attrib.get("data-meta-price")
            laptops['ecname'] = card.xpath(".//a[@class='app-catalog-9gnskf e1259i3g0']/text()").extract()[0]
            laptops['visited_at'] = f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'
            laptops['ssd'] = re.findall(r'[0-9]+', str(card.xpath(".//ul[@class='app-catalog-q1moq7 e4qu3683']/li[5]/text()").extract()))[0]
            laptops['ram'] = re.findall(r'[0-9]+', str(card.xpath(".//ul[@class='app-catalog-q1moq7 e4qu3683']/li[4]/text()").extract()))[0]
        
            yield laptops
      

    def start_requests(self):
        for page in range(1, 1 + self.pages_count):
            
            url = f'https://www.citilink.ru/catalog/noutbuki/?p={page}&sorting=price_asc&pf=ms_action%2Cms_installment%2Cdiscount.any%2Crating.any&f=ms_action%2Cdiscount.any%2Crating.any&pprice_min=10320&price_min=10320&price_max=451180&view_type=list'

            yield SeleniumRequest(url=url, callback=self.parse, wait_time=20, screenshot=True, wait_until=EC.element_to_be_clickable((By.TAG_NAME, "button")))