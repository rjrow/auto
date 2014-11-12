#!/bin/sh
cd /vagrant/auto_scrape
scrapy crawl cl_auto_spider -o items.csv -s DEPTH_LIMIT=5


