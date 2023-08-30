# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pathlib import Path
import pandas as pd


class SpiderquotecrawlerPipeline:
    def process_item(self, item, spider):

        title = item['text'].split("“")
        title = item['text'].replace('“', "")
        all_words = title.split()
        all_words[0] = all_words[0].replace('"', "")
        all_words[1] = all_words[1].replace('"', "")

        filename = f"{all_words[0] + all_words[1]}" + " - " + f"{item['author']}.txt"
        Path("./quotes/" + filename).write_text(item['text'])

        print('/'.join(item['tags']))


        data = {
            'Autor': [item['author']],
            'Tags': ['/'.join(item['tags'])],
            'pageNumber': [item['pageNumber']],
            'arquiveName': [filename],
        }
        
        # Make data frame of above data
        df = pd.DataFrame(data)
        
        # append data frame to CSV file
        df.to_csv('./CSV/quotesInfo.csv', encoding='utf_8_sig', sep=';', mode='a', index=False, header=False)
        
        # print message
        print("Data appended successfully.")

        return item
