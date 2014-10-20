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
			Rule (SgmlLinkExtractor(allow=("all", )),
    		callback='parse_page', follow= True),
		)

		def parse_page(self, response):
			response = HtmlXPathSelector(response)

			rows = response.select('//li[contains(@class, "views-row")]')

			for row in rows:

				item = AutoNowPage()

				#link = row.select('.//div[contains(@class, "phpcode")]/a')
				
				print row.select('//div[@class = "views-field-field-price-value"]')
				# item['links']  = link.select("@href").extract()

				# item['price'] = row.select('.//span[@class = "l2"]/span[@class = "price"]/text()').extract()
				# item['location'] = row.select('.//span[@class = "pnr"]/small/text()').extract()

				# url = 'http://phoenix.craigslist.org{}'.format(''.join(item['links']))
				# print url
				# print 'item link: %s ' % item['links']
				# yield Request(url = url, meta = {'item': item}, callback = self.parse_item_page)

		def parse_item_page(self, response):
			item = response.meta['item']

			hxs = HtmlXPathSelector(response)
			item['description'] = hxs.select('//section[@id = "postingbody"]/text()').extract()
			print item['description']
			return item



