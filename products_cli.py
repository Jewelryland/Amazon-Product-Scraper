import argparse
from productscrape import AmazonDesc

parser = argparse.ArgumentParser(description='Return the product info for an Amazon page in JSON format')



parser.add_argument('--url', type=str, help= 'An amazon product page url')

parser.add_argument('--useragent', type=str, help='A browser user agent for the request to the amazon product page. If none is supplied a random one  will be selected. This argument must be enclosed within quotes')

args = parser.parse_args()


if args.useragent == None:
	
	product = AmazonDesc(args.url)

else:
	product = AmazonDesc(args.url,argus.useragent)
	
	
print(product.scrape())
