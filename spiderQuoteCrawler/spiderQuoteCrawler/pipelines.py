# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pathlib import Path


class SpiderquotecrawlerPipeline:
    def process_item(self, item, spider):

        title = item['text'].replace('"', "")
        title = title.split("“")
        title = item['text'].replace('“', "")
        all_words = title.split()

        filename = f"{all_words[0] + all_words[1]}" + " - " + f"{item['author']}.txt"
        Path("./quotes/" + filename).write_text(item['text'])

        return item
