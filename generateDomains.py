#/usr/bin/python3

import click
from itertools import product
from string import ascii_lowercase, digits

@click.command()
@click.option('-tld', prompt='tld', help='tld.')
@click.option('-size', prompt='size to generate', help='size of domain names to generate.')

def domains_by_size (size, tld):
    letters_and_digits = ascii_lowercase+digits
    filename = '{}_character_{}_domains.txt'.format(size, tld)

    keywords = [''.join(i) for i in product(letters_and_digits, repeat = int(size))]
    print('Generated {} {} domain names'.format(len(keywords), tld))

    with open(filename, 'w') as file:
        for entry in keywords:
            domain_name = entry + tld
            file.write (domain_name + '\n')

if __name__ == '__main__':
    domains_by_size ()

