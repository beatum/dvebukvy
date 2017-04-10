# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import scrapy


class DataSpider(scrapy.Spider):
    name = 'dataspider'

    urls = []
    i = 0
    for i in xrange(1000):
        i += 1
        url = 'https://yandex.ru/referats/?t=astronomy&s=%d' % i
        urls.append(url)
        
    start_urls = urls

    def parse(self, response):
        x = response.css("div.referats__text")
        yield {
            'title': x.css("strong::text").extract(),
            'text': x.css("p::text").extract(),
        }

