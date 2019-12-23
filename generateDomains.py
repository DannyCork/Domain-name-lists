#/usr/bin/python3

import click
from itertools import product
from string import ascii_lowercase, digits

@click.command()
@click.option('-tld', prompt='tld', help='tld.')
@click.option('-size', prompt='size to generate', help='size of domain names to generate.')

def domains_by_size (size, tld):
    letters_and_digits = ascii_lowercase+digits

    print(all)

    keywords = [''.join(i) for i in product(letters_and_digits, repeat = int(size))]
    count = 0
 
    print('Generated {} {} domain names'.format(len(keywords), tld))
    input('continue?')

    for entry in keywords:
        count = count+1
        print (entry + tld)
    print (count)

if __name__ == '__main__':
    domains_by_size ()

