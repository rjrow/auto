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

			item = AutoNowPage()

			#link = row.select('.//div[contains(@class, "phpcode")]/a')

			field_content = "span[@class = 'field-content']/text()"

			rows = response.select('//li[contains(@class, "views-row")]')

			for row in rows:
				item['price'] = response.select('./div[@class = "views-field-field-price-value"]/' + field_content).extract()
				item['links'] = response.select('./div[@class = "views-field-phpcode"]/' + \
					"span[@class = 'field-content']" + '/a/@href').extract()
				item['title'] = response.select('./div[@class = "views-field-phpcode"]/' + \
					"span[@class = 'field-content']" + '/a/text()').extract()
				print item

				for link in item['links']:
					url = "http://www.liftedtrucks.com" + link
					yield Request(url = url, meta = {'item': item}, callback = self.parse_item_page)


			# item['links']  = link.select("@href").extract()

			# item['price'] = row.select('.//span[@class = "l2"]/span[@class = "price"]/text()').extract()
			# item['location'] = row.select('.//span[@class = "pnr"]/small/text()').extract()

			# url = 'http://phoenix.craigslist.org{}'.format(''.join(item['links']))
			# print url
			# print 'item link: %s ' % item['links']
			# yield Request(url = url, meta = {'item': item}, callback = self.parse_item_page)

		def parse_item_page(self, response):
			item = response.meta['item']

			response = HtmlXPathSelector(response)
			item['description'] = response.select('//div[@id = "vehicle-attributes"]/div/text()').extract()
			return item



