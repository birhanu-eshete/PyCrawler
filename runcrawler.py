#!/usr/bin/python
import sys
import pycrawler
import time

seed_URLs =sys.argv[1]
index_file =sys.argv[2]
depth=sys.argv[3]
seed =open(seed_URLs)
page_list =seed.readlines()
crawler_object =pycrawler.Crawler(index_file)
#print page_list

started_at=time.time()
print "Crawling started"
crawler_object.crawl(page_list,int(depth))
ended_at=time.time()
duration =(ended_at - started_at)
print "Crawling finished!"
print "Time spent =",round(duration,2),"seconds." 
