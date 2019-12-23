# Domain-name-lists
lists upon lists of domain names


Number of possible combinations

2 letter 676 (26\*26) \
3 letter 17576 (26\*26\*26)\
4 letter 456976 (26\*26\*26\*26)\
5 letter 11,881,376 (26\*26\*26\*2\*26)\

The Moz Top 500 Websites
https://moz.com/top-500/download/?table=top500Domains


from itertools import product
from string import ascii_lowercase

keywords = [''.join(i) for i in product(ascii_lowercase, repeat = 2)]

for entry in keywords:
        print (entry+'.ie')
