# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import mySpiderItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['meijutt.com']
    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):
        #filename = "movie.html"
        #open(filename, 'w').write(response.body)
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for each_movie in movies:
            item = MovieItem()
            item['name'] = each_movie.xpath('./h5/a/@title').extract()[0]
            yield item
