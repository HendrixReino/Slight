import scrapy
from m2_d01_Logging.items import QuestionItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class LogExampleSpider(scrapy.Spider):

    name = 'logger'
    start_urls = ['https://stackoverflow.com/questions?sort=featured']

    def parse(self,response):

        questions = response.css('div.summary')


        if len(questions)== 0:
            self.logger.error('No elements found on the current page with the selector...')

        self.logger.info('loading the items with the scraper data...')

        for question in questions:

            loader_object = ItemLoader(item=QuestionItem(), selector=question)

            loader_object.default_output_processor = TakeFirst()

            loader_object.add_css('question','h3 > a::text')
            loader_object.add_xpath('url', './h3/a/@href')

            yield loader_object.load_item()