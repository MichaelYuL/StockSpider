import scrapy


class A601828Spider(scrapy.Spider):
    name = "601828"
    allowed_domains = ["quote.eastmoney.com"]
    start_urls = ["http://quote.eastmoney.com/"]

    def parse(self, response):
        pass
