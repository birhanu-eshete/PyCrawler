import urllib
from bs4 import BeautifulSoup 
from urlparse import urlparse
from urlparse import urljoin

class Crawler:

	# Initialize the crawler
	def __init__(self,index_file):
		self.index=index_file
	
	# Index a URL if it is not already indexed
	def add_to_url_list(self,url):
		if not self.is_in_url_list(url):
			out=open(self.index,'a')
			out.write(url+'\n')
			out.close()	

	# Return true if this url is already indexed
	def is_in_url_list(self,url):
		already_indexed=False
		index_content=open(self.index,'r')
		url_list=index_content.readlines()
		
		for page in url_list:
			#print "page", page
			#print "url", url
			#if page==url:
			#	already_indexed=True
        		#	break
			if url in url_list:
				already_indexed=True
				break	
		#print already_indexed
		return already_indexed
	
	
	# Start with the seed, perform a breadth first search to the given depth,indexing pages on the way 
	def crawl(self,seed,depth):
		index_file=self.index

		for level in range(depth):
			print "At Level: %s" % level
			newpages=set()
			print len(seed), "URLs to crawl"
			for page in seed:
				try:
					c=urllib.urlopen(page) # get the URL resource object
					u=urlparse(page)
					#print c
				except:
					print "Could not open %s" % page
					continue
				soup=BeautifulSoup(c.read( )) # parse the URL resource object
				#print soup
				self.add_to_url_list(page)
				links=soup.find_all('a') # filter all anchors
				#print links
				for link in links:
					if ('href' in dict(link.attrs)):
						#print "the link", link['href']
						url=urljoin(page,link['href']) # build absolute URL	
			      		        if url.find("'")!=-1:continue
						url=url.split('#')[0] # remove location portion
						if url[0:4]=='http' and not self.is_in_url_list(url):
							newpages.add(url)
						print url 
				seed=newpages # re-define the seed for next level of crawl
		
