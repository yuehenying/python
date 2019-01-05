# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from pixivbook.items import PixivbookItem
# import re

class PixivSpider(scrapy.Spider):
    name = 'pixiv'
    allowed_domains = ['www.pixiv.net']

    def start_requests(self):
        start_urls = 'https://www.pixiv.net/bookmark.php'
        yield Request(url = start_urls,cookies = {'PHPSESSID':'24852177_bcc2ed6f442483e5f786e1e8b3735302','device_token':'448025596537b642fafde0298d16a070','login_ever':'yes'},callback=self.parse)

    def parse(self, response):
        picture_list =  response.xpath("//div[@class='display_editable_works']//li[@class='image-item']")
        for i_item in picture_list:
            pixiv_item = PixivbookItem()
            pixiv_item['name'] = i_item.xpath(".//a[2]/h1[@class='title']/text()").extract_first().replace('\\','')
            pixiv_item['url'] = [i_item.xpath(".//div[@class='_layout-thumbnail']/img[@class='ui-scroll-view']/@data-src").extract_first().replace('c/150x150/','')]
            yield pixiv_item
    
        next_link = response.xpath("//div[@class='pager-container']/span[@class='next']/a[@class='_button']")
        if next_link:
            next_link = next_link[0].xpath("./@href").extract_first()
            yield scrapy.Request('https://www.pixiv.net/bookmark.php'+next_link,callback=self.parse)