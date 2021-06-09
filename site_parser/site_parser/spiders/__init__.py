# This package will contain the spiders of your Scrapy project
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
import json
from datetime import date, timedelta
from ..util import str_to_date, clean_title, clean_text
from ..items import SiteParserItem


class NewsSpiderSpider(scrapy.Spider):
    name = 'news_spider'
    page_number = 2
    start_urls = ['https://primorye.ldpr.ru/api/pb/articles?site_key=primorye&aggregate=full&limit=12&page=1']
    how_many_days = date.today() - timedelta(days=30)
    simple_flag = True
    info_flag = True

    def parse(self, response):
        items = SiteParserItem()
        data = json.loads(response.body)
        # API сайта может содержать новости в json по двум ключам: 'simple' и 'info'
        try:
            for item in data.get('simple'):
                # проверяем, что дата новости в пределах 30 дней
                if str_to_date(item.get('date')) > NewsSpiderSpider.how_many_days:
                    items['url'] = 'https://primorye.ldpr.ru/event/' + str(item.get('id'))
                    # очищаем заголовки и текст новости от html тегов и нераспознанных символов с помощью функции
                    items['title'] = clean_title(item.get('cover').get('title'))
                    items['text'] = clean_text(item.get('content'))
                    items['date'] = item.get('date')
                    yield items
                else:
                    # если более 30 дней, то меняем флаг
                    NewsSpiderSpider.simple_flag = False
        except TypeError:
            NewsSpiderSpider.simple_flag = False

        try:
            for item in data.get('info'):
                if str_to_date(item.get('date')) > NewsSpiderSpider.how_many_days:
                    items['url'] = 'https://primorye.ldpr.ru/event/' + str(item.get('id'))
                    items['title'] = clean_title(item.get('cover').get('title'))
                    items['text'] = clean_text(item.get('content'))
                    items['date'] = item.get('date')
                    yield items
                else:
                    NewsSpiderSpider.info_flag = False
        except TypeError:
            NewsSpiderSpider.info_flag = False

        # следующая страница
        next_page = 'https://primorye.ldpr.ru/api/pb/articles?site_key=primorye&aggregate=full&limit=12&page=' + \
                    str(NewsSpiderSpider.page_number)
        if NewsSpiderSpider.simple_flag or NewsSpiderSpider.info_flag:
            # если один из флагов "True", то переходим на следующую страницу и продолжаем парсинг
            NewsSpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
