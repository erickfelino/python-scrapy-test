import scrapy
from scrapy import Spider
from scrapy.http import FormRequest


# Classe base para a execução da spider

class QuotesSpider(Spider):
    name = "quotes"

    #A primeira URl a ser conduzida é da tela de login, para realizar a autênticação no site e seguir com o web crawling
    def start_requests(self):
        login_url = 'http://quotes.toscrape.com/login'
        yield scrapy.Request(login_url, callback=self.login)
    
    #Função para a efetuar o login via token, inserindo password e username nos campos, retornando a página principal
    def login(self, response):
        token = response.css("form input[name=csrf_token]::attr(value)").extract_first()
        return FormRequest.from_response(response,
                                         formdata={'csrf_token': token,
                                                   'password': 'senha',
                                                   'username': 'usuario'},
                                         callback=self.parse)

    #Função parse para manipulação, apuração e registro das informações coletadas no site
    def parse(self, response):
        
        for quote in response.css("div.quote"):
            #filtro para as quotes
            if ("truth" in quote.css("span.text::text").get()) or ("Mark Twain" in  quote.css("span small::text").get() and "life" in quote.css("div.tags a.tag::text").getall()):
                yield {
                    "text": quote.css("span.text::text").get(),
                    "author": quote.css("span small::text").get(),
                    "tags": quote.css("div.tags a.tag::text").getall(),
                    "pageNumber": response.url.split("/")[-2],
                }

        #Verifica se há página seguinte para continuar 
        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)