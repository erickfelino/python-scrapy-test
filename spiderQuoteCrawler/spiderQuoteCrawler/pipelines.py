# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pathlib import Path
import pandas as pd

#pipeline base para o tratamento de dados e salvamento do database
class SpiderquotecrawlerPipeline:
    def process_item(self, item, spider):

        #Tratamento das palavras do nome do arquivo para não gerar erro ao salvar o .txt
        title = item['text'].split("“")
        title = item['text'].replace('“', "")
        all_words = title.split()
        all_words[0] = all_words[0].replace('"', "")
        all_words[1] = all_words[1].replace('"', "")

        #salvando o nome, conteúdo e caminho do txt
        filename = f"{all_words[0] + all_words[1]}" + " - " + f"{item['author']}.txt"
        Path("./quotes/" + filename).write_text(item['text'])

        #criando data para o DataFrame do Pandas e salvar no CSV destino
        data = {
            'Autor': [item['author']],
            'Tags': ['/'.join(item['tags'])],
            'pageNumber': [item['pageNumber']],
            'arquiveName': [filename],
        }
        
        # criando data frame
        df = pd.DataFrame(data)
        
        # dando append na informação
        df.to_csv('./CSV/quotesInfo.csv', encoding='utf_8_sig', sep=';', mode='a', index=False, header=False)

        return item
