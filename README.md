PyCrawler
==========
A basic Python crawler that harvests URLs and maintains crawl index based on a given set of URL seeds.The implementation is based on the algorithm in the book 'Programming Collective Intelligence' by Toby Segaran.

##What it Does
- Given a file with seed URLs, an index file where to save the resuts, and the crawl depth (an integer >=1), it performs the crawl
  and saves the harvested URLs in the index file. It automatically tosses out duplicate URLs which might happen during crawling. Depending on the bandwidth and crawl-depth, the crawl speed may expectedly vary.

##Requirements/Dependencies
- Python 2.7 - http://www.python.org
- Beautiful Soup Library - http://www.crummy.com/software/BeautifulSoup/
- urllib Library - http://github.com/mikemaccana/python-docx

##Plaftorms
This application is platform-agnostic as long as you have the Python interpretor.
Quick test showed that it worked fine on:
- Windows XP SP3
- MacOs 10.6.4 
- Ubuntu 12.10 LTS 

##Usage
- Prepare the file containing seed files (e.g., test_seed.txt)
- Create the index file if running for the first time (e.g., test_index.txt). You need not create the index file for the next run as the crawl output is appended to the index file. If you want to launch a new crawl task, create a new index file.
- Run the crawler: Suppose the crawl-depth is 2. So, you run the crawler as: <code>python runcrawler.py test_seed.txt test_index.txt 2 </code>


##Author
Birhanu Mekuria Eshete - birhanu.mekuria(at)gmail.com

##License 
This code is released under the [MIT License](http://opensource.org/licenses/MIT)

