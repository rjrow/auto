import scrapy
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import HtmlResponse
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request
from auto_scrape.items import CraigsListPage



class AutoSpider(CrawlSpider):
		name = "auto_spider"
		allowed_domains = ["craigslist.org"]
		start_urls = ["http://phoenix.craigslist.org/cto/"]


		rules = (
			Rule(
			SgmlLinkExtractor(allow_domains=("phoenix.craigslist.org", )),
			callback = 'parse_page', follow = True
			),
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
				print 'concatenated url: %s ' % url
				print 'item link: %s ' % item['links']
				yield Request(url = url, meta = {'item': item}, callback = self.parse_item_page)


		def parse_item_page(self, response):
			item = response.meta['item']

			hxs = HtmlXPathSelector(response)
			item['description'] = hxs.select('//section[@id = "postingbody"]/text()').extract()
			# print item['description']


