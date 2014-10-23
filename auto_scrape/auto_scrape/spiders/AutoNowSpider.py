import scrapy
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import HtmlResponse
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request
from auto_scrape.items import AutoNowPage



class AutoSpider(CrawlSpider):
		name = "autonow_spider"
		allowed_domains = ["liftedtrucks.com"]
		start_urls = ["http://www.liftedtrucks.com/vehicles"]

		rules = (
			Rule (SgmlLinkExtractor(allow=("vehicle", ), 
									deny = ("/trucks", "/all/", "/suvs", "/cars", "/Featured",
									"/diesel", "/lifted", "/stock", "/form", "page", "/category"),),
    		callback='parse_page', follow= True),
		)

		def parse_page(self, response):
			response = HtmlXPathSelector(response)

			item = AutoNowPage()

			#link = row.select('.//div[contains(@class, "phpcode")]/a')

			field_content = "span[@class = 'field-content']/text()"

			rows = response.select('//li[contains(@class, "views-row")]')

			for row in rows:

		def parse_item_page(self, response):
			item = response.meta['item']

			response = HtmlXPathSelector(response)
			item['description'] = response.select('//div[@id = "vehicle-attributes"]/div/text()').extract()
			return item



