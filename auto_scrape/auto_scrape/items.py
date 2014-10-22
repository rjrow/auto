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

	odometer	= Field()
	color		= Field()
	fuel		= Field()
	Transm		= Field()
	tStatus		= Field()
	condition 	= Field()
	size		= Field()
	type		= Field()
	drive		= Field()
	cylinders 	= Field()



class AutoNowPage(Item):
	title       = Field()
	description = Field()
	links 		= Field()
	price		= Field()

	Transm		= Field()
	Engine		= Field()
	Stock		= Field()





