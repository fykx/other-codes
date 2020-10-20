# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request
from scrapy.pipelines.images import ImagesPipeline
from fykx import settings


class FykxPipeline(object):
    def __init__(self):
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')  # __file__表示了当前文件的绝对路径
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def process_item(self, item, spider):
        title = item['title']
        image_url = item['image_url']
        category_path = os.path.join(self.path, title)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        image_name = image_url.split('/')[-1].split('.')[0] + '.jpg'
        request.urlretrieve(image_url, os.path.join(category_path, image_name))  # 下载文件
        return item


class FykxImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        request_objs = super().get_media_requests(item, info)
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs

    def file_path(self, request, response=None, info=None):
        path = super().file_path(request, response, info)
        title = request.item.get('title')
        images_store = settings.IMAGES_STORE
        title_path = os.path.join(images_store, title)
        if not os.path.exists(title_path):
            os.mkdir(title_path)
        image_name = path.replace("full/", "")
        image_path = os.path.join(title_path, image_name)
        return image_path
