import scrapy
from scrapy.linkextractors import LinkExtractor


class MySpider(scrapy.Spider):
    name = "myp2"
    link_extractor = LinkExtractor(allow_domains = ["https://lxml.de/index.html"])
    start_urls = ["https://lxml.de/index.html"]


    def parse(self, response):
        self.log("Crawled %s" % response.url)
        links = self.link_extractor.extract_links(response)
        linkl = []
        for link in links:
            linkl.append(link)

        with open("/home/slliw/Scrapy/data/linkl.txt", "w") as f:
            for i in linkl:
                f.write(i +"\n")




