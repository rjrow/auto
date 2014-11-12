import scrapy
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import HtmlResponse
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request
from auto_scrape.items import CraigsListPage



class AutoSpider(CrawlSpider):
		name = "cl_auto_spider"
		allowed_domains = ["craigslist.org"]
		start_urls = ["http://phoenix.craigslist.org/search/cto/"]

		rules = (
			# Rule(
			# SgmlLinkExtractor(allow_domains=("phoenix.craigslist.org", )),
			# callback = '', follow = True
			# ),
			Rule (SgmlLinkExtractor(allow=("cto", )),
    		callback='parse_page', follow= True),
		)

		def parse_page(self, response):
			response = HtmlXPathSelector(response)

			rows = response.select('//div[@class = "content"]/p[@class = "row"]')
			for row in rows:
				item = CraigsListPage()
				link = row.select('.//span[@class = "pl"]/a')
				item['title']  = link.select('text()').extract()
				item['links']  = link.select("@href").extract()

				item['price'] = row.select('.//span[@class = "l2"]/span[@class = "price"]/text()').extract()
				item['location'] = row.select('.//span[@class = "pnr"]/small/text()').extract()

				url = 'http://phoenix.craigslist.org{}'.format(''.join(item['links']))
				print url
				print 'item link: %s ' % item['links']
				yield Request(url = url, meta = {'item': item}, callback = self.parse_item_page)

		def parse_item_page(self, response):
			item = response.meta['item']

			hxs = HtmlXPathSelector(response)
			item['description'] = hxs.select('//section[@id = "postingbody"]/text()').extract()
			item['cylinders'] = hxs.select('//p[@class = "attrgroup"]//span[contains(text(), "cylinders")]/b/text()').extract()
			item['odometer'] = hxs.select('//p[@class = "attrgroup"]//span[contains(text(), "odometer")]/b/text()').extract()
			item['color'] = hxs.select('//p[@class = "attrgroup"]//span[contains(text(), "color")]/b/text()').extract()
			item['fuel'] = hxs.select('//p[@class = "attrgroup"]//span[contains(text(), "fuel")]/b/text()').extract()
			item['Transm'] = hxs.select('//p[@class = "attrgroup"]//span[contains(text(), "Transm")]/b/text()').extract()
			item['tStatus'] = hxs.select('//p[@class = "attrgroup"]//span[contains(text(), "tStatus")]/b/text()').extract()
			item['condition'] = hxs.select('//p[@class = "attrgroup"]//span[contains(text(), "condition")]/b/text()').extract()
			item['size'] = hxs.select('//p[@class = "attrgroup"]//span[contains(text(), "size")]/b/text()').extract()
			item['type'] = hxs.select('//p[@class = "attrgroup"]//span[contains(text(), "type")]/b/text()').extract()
			item['drive'] = hxs.select('//p[@class = "attrgroup"]//span[contains(text(), "drive")]/b/text()').extract()
#			item['date']  = hxs.select('//p[@class = "postinginfo]//time[')
#			item['pid']


			#item['odometer'] = attrs.select("attrgroup[contains(text(), 'odometer')]/text()").extract()
			return item
			#response.xpath('//p[@class = "attrgroup"]//span[contains(text(), "cylinders")]')



