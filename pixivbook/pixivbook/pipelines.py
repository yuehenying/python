# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from scrapy.exceptions import DropItem
import os

class PixivbookPipeline(object):
    def process_item(self, item, spider):
        return item

class DownloadImagesPipeline(ImagesPipeline):

    def get_media_requests(self,item,info):
        for image_url in item['url']:
            yield Request(image_url,cookies = {'PHPSESSID':'24852177_bcc2ed6f442483e5f786e1e8b3735302','device_token':'448025596537b642fafde0298d16a070','login_ever':'yes'},meta={'name': item['name']})

    def file_path(self,request,response=None,info=None):
        name = request.meta['name'] + '.jpg'
        return name