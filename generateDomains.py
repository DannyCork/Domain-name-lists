from itertools import product
from string import ascii_lowercase


def domains_by_size (size, tld):
	keywords = [''.join(i) for i in product(ascii_lowercase, repeat = size)]
	count = 0
 
	for entry in keywords:
		count = count+1
		print (entry + tld)
	print (count)


domains_by_size (3, '.ie')
