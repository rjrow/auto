# Scrapy settings for auto_scrape project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'auto_scrape'

SPIDER_MODULES = ['auto_scrape.spiders']
NEWSPIDER_MODULE = 'auto_scrape.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'auto_scrape (+http://www.yourdomain.com)'
