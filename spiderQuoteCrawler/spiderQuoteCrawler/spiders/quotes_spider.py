import scrapy
from scrapy import Spider
from scrapy.http import FormRequest




class QuotesSpider(Spider):
    name = "quotes"
    def start_requests(self):
        login_url = 'http://quotes.toscrape.com/login'
        yield scrapy.Request(login_url, callback=self.login)
    
    def login(self, response):
        token = response.css("form input[name=csrf_token]::attr(value)").extract_first()
        return FormRequest.from_response(response,
                                         formdata={'csrf_token': token,
                                                   'password': 'senha',
                                                   'username': 'usuario'},
                                         callback=self.parse)

    def parse(self, response):
        
        for quote in response.css("div.quote"):
            if ("truth" in quote.css("span.text::text").get()) or ("Mark Twain" in  quote.css("span small::text").get() and "life" in quote.css("div.tags a.tag::text").getall()):
                yield {
                    "text": quote.css("span.text::text").get(),
                    "author": quote.css("span small::text").get(),
                    "tags": quote.css("div.tags a.tag::text").getall(),
                }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)