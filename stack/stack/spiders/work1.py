# -*- coding: utf-8 -*-
import scrapy


class Work1Spider(scrapy.Spider):
    name = 'work1'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['https://stackoverflow.com/questions/tagged/python?page=1&sort=newest&pagesize=50',
    'https://stackoverflow.com/questions/tagged/python?page=2&sort=newest&pagesize=50',
    'https://stackoverflow.com/questions/tagged/python?page=3&sort=newest&pagesize=50']

    def parse(self, response):
        questions=response.css('div.summary')
        for i in questions:        	
            yield {
                'question': i.css('h3 a.question-hyperlink::text').extract_first(),
                'link':'https://stackoverflow.com'+str(i.css('h3 a.question-hyperlink::attr(href)').extract_first())
                  }
