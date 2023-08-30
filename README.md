# Web Crawling de Quotes - README

Este é um projeto de web crawling desenvolvido para extrair quotes do website http://quotes.toscrape.com/. O programa foi construído utilizando a biblioteca Scrapy e tem como objetivo realizar a extração das citações (quotes) presentes no site e salvar essas informações em arquivos CSV. Abaixo estão as instruções de como executar o programa e uma breve descrição das alterações feitas na pipeline do projeto.

## Instruções de Execução

Siga as etapas abaixo para executar o programa e realizar a extração das quotes:

1. Certifique-se de ter o Python instalado em sua máquina.

2. Clone ou faça o download do repositório para sua máquina local.

3. Abra o terminal e navegue até o diretório principal do projeto (`spiderQuoteCrawler`).

4. Execute o seguinte comando para iniciar a extração das quotes:
   
   ```
   scrapy crawl quotes
   ```

5. O programa irá iniciar o web crawling no site http://quotes.toscrape.com/ e irá extrair as informações das quotes. Os dados extraídos serão salvos em arquivos txt na pasta quotes.

6. Após a conclusão da extração, você encontrará os arquivos CSV no diretório especificado para armazenamento, como CSV.

## Alterações na Pipeline

Para atender às necessidades do projeto e permitir a alteração e manipulação dos dados extraídos, foram feitas algumas alterações na pipeline do Scrapy:

1. **Extração de Dados:** O spider foi configurado para extrair as informações relevantes das quotes, incluindo o texto da citação e o autor.

2. **Transformação de Dados:** Foram aplicadas transformações nos dados extraídos, como limpeza de espaços em branco extras e formatação adequada dos valores.

3. **Armazenamento em TXT:** As quotes são armazenadas em arquivos TXT. Cada linha do TXT representa uma quote, com as colunas correspondendo aos texto da citação.

4. **Armazenamento em CSV:** As informações das quotes são armazenadas em arquivos CSV. Cada linha do CSV representa uma quote, com as colunas correspondendo ao author, tagas, número da página e nome do arquivo em que foi salva a informação
