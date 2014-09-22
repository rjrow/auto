# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field
import scrapy

class CraigsListPage(Item):
	title 	 	= Field()
	links  	 	= Field()
	price 	 	= Field()
	location 	= Field()
	description = Field()
