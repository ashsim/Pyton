# -*- coding: utf-8 -*-
import scrapy
import json

class Work3Spider(scrapy.Spider):
    name = 'work3'
    allowed_domains = ['imdb.com']
    start_urls = []
    with open (r'C:\Users\ashot\data_scraping\imdb\imdb.json') as f:
    	movies=f.read()
    	movie=json.loads(movies)
    	for i in range(10):
    		start_urls.append(movie[i]['URL'])

    def parse(self, response):
        yield{
        "movie": response.xpath('//title/text()').extract_first(),
        "director": response.xpath('//*[contains(@class, "credit_summary_item")]/span/a/span/text()').extract_first()
        }
