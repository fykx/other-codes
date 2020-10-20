# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from fykx.items import FykxItem
from lxml import etree

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['www.dili360.com']
    start_urls = ['http://www.dili360.com/gallery']

    def __init__(self):
        super().__init__()
        self.url_0 = 'http://www.dili360.com'

    '''获取左侧标签栏各类别链接并返回请求'''
    def parse(self, response):
        tables = response.xpath("//ul[@class='gallery-cate-list']/li")
        for table in tables:
            if table.xpath(".//a/text()").get() != '画廊':
                href = table.xpath(".//a/@href").get()
                url = self.url_0 + href
                request = scrapy.Request(url=url, callback=self.parse_1)
                yield request

    '''将Selenium和chromedriver集成到scrapy当中，
    获取网页下方小图标列表栏所有标签链接（第一页、第二页......）,并返回请求'''
    def parse_1(self, response):
        tables = response.xpath("//ul[@class='gallery-block-small']/li")
        for table in tables:
            href = table.xpath(".//a/@href").get()
            url = self.url_0 + href
            # title = table.xpath(".//a/@title").get()
            request = scrapy.Request(url=url, callback=self.parse_2)
            yield request

        driver = webdriver.Chrome(executable_path=r'D:\chromedriver.exe')
        driver.get(response.url)
        driver.implicitly_wait(10)
        try:
            while True:
                next_page = driver.find_element_by_xpath("//li[@class='next']")
                if next_page:
                    next_page.click()
                    driver.implicitly_wait(10)
                    source = driver.page_source
                    html = etree.HTML(source)
                    tables_1 = html.xpath("//ul[@class='gallery-block-small']/li")
                    for table_1 in tables_1:
                        href_1 = table_1.xpath(".//a/@href")[0]
                        url_1 = self.url_0 + href_1
                        request_1 = scrapy.Request(url=url_1, callback=self.parse_2)
                        yield request_1
                else:
                    break
        except:
            pass
        driver.quit()

    '''获取小图标列表栏中某一标签名称以及其包含的所有图片链接，构建item并返回'''
    def parse_2(self, response):
        tables = response.xpath("//ul[@class='slider']/li")
        image_urls = []
        for table in tables:
            image_url = table.xpath(".//img/@src").get().replace('rw3', 'rw17')
            image_urls.append(image_url)
        title = response.xpath("//div[@class='title']/span/text()").get().replace(" ", "")
        item = FykxItem(title=title, image_urls=image_urls)
        yield item
