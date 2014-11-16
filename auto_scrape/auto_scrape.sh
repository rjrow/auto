cd /vagrant/auto_scrape


now=$(date +"%m_%d_%Y_%H_%M_%S")
_file="data/items_$now.csv"


echo "Filename: $_file"
scrapy crawl cl_auto_spider -o $_file -s DEPTH_LIMIT=15





