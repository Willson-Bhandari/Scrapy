import scrapy


class HdlSpider(scrapy.Spider):
    name = "hdl"
    allowed_domains = ["sharesansar.com"]
    start_urls = ["https://sharesansar.com"]

    def parse(self, response):
        pass
