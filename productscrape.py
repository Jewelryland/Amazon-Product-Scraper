import random
import requests
import json
from bs4 import BeautifulSoup

class AmazonDesc():
	"""
	Returns the description of an Amazon product page in JSON format
	"""
	def __init__(self, url, useragent = None):
		self.url = url
		self.useragent = useragent

        def rand_uagent(self):
		uagents = [
	
		"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
		"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36"
		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0",
		"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0"
		]
		
		return random.choice(uagents)

	def build_json(self, domcoll, dict_):
		for coll in domcoll:
			li = coll.find_all("li")
			
			for item in li:
				field = item.text
				field = field.rstrip().replace('\n','')
				
				if ":" in field:
					info = field.split(":")
					dict_[info[0]] = info[1]

		return json.dumps(dict_)

		
		
	def scrape(self):
		
		if self.useragent == None:
			self.useragent = self.rand_uagent()
		
		headers = {'user-agent': self.useragent}
		
		link = requests.get(self.url, headers=headers).text
		
		soup = BeautifulSoup(link,'html.parser')
		content = soup.find_all(attrs={"class": "content"})

		product_info = {} 

		return self.build_json(content,product_info)
