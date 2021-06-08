import scrapy


class NewsSpiderSpider(scrapy.Spider):
    name = 'news_spider'
    allowed_domains = ['https://primorye.ldpr.ru/']
    start_urls = ['http://https://primorye.ldpr.ru//']

    def parse(self, response):
        pass
