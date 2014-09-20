import scrapy
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import HtmlResponse


class AutoSpider(BaseSpider):
		name = "auto_spider"
		allowed_domains = ["craigslist.org"]
		start_urls = ["http://phoenix.craigslist.org/cto/"]


		def parse(self, response):
			response = HtmlXPathSelector(response)
			titles = response.select('//span[@class = "price"]/text()').extract()
			for title in titles:
				print title