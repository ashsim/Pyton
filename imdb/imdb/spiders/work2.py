# -*- coding: utf-8 -*-
import scrapy


class Work2Spider(scrapy.Spider):
    name = 'work2'
    allowed_domains = ['imdb.com']
    start_urls = ['http://www.imdb.com/chart/top']

    def parse(self, response):
        film=response.css('tr')[1:-2]
    	avrate=[]
        for i in film:
            yield {
               'Year':i.css('td.titleColumn span::text').extract_first(),
               'URL':'http://imdb.com'+str(i.css('td.titleColumn a::attr(href)').extract_first()),
               'Rating':i.css('td strong::text').extract_first(),
               'Rank': i.css('td.titleColumn::text').re('[0-9]+')[0],
               'Title': i.css('td.titleColumn a::text').extract_first(),
                }

        for x in film:
        	Rate=x.css('td strong::text').extract_first()
        average=float(Rate)
        avrate.append(average)
        avg=sum(avrate)/len(avrate)
    	yield{
    	"Average":avg
    	}