# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import datetime
from scrapy.exceptions import DropItem

class EngoPipeline:
    def process_item(self, item, spider):
        if type(item['date']) is not type(datetime.date):
            raise DropItem('This is not a python date!!!!')
        return item