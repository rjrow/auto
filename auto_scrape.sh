#!/bin/sh
cd /vagrant/auto_scrape
scrapy crawl auto_spider -o items.csv -s DEPTH_LIMIT=1

