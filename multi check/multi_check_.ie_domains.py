import whois
import sys
import os
from colorama import Fore, Back, Style
import datetime

def get_list_of_domains():
    """Reads list of keywords/domains to search from file, sanitises them for subsuqient looksups."""
    filename = "domains.txt"
    
    try:
        with open(filename) as f:
            file_input = f.read().splitlines()
    except:
        sys.exit("Couldnt open domains.txt file")

    valid_domains = []

    try:
        for domain_name in file_input:
            if not domain_name.endswith(".ie"):
                domain_name = domain_name + ".ie"

            valid_domains.append(domain_name)
    except:
        sys.exit("Couldnt read files")

    return valid_domains


# --------------------------------------------------------

def check_if_registered(domains):
    """Takes list of .ie domains, outputs domains and their registration status."""

    print(f"{Fore.YELLOW}Checking {len(domains)} domains....")
    Fore.RESET
    available_domains = []

    for domain in domains:
        result = whois.query(domain)
        if result == None:
            print(f"{Fore.GREEN}\N{check mark}  {domain} available.")
            available_domains.append(domain)
        else:
            years_since_registration = (
                datetime.date.today().year - result.creation_date.year
            )
            print(
                f"{Fore.RED}\N{cross mark}  {domain} already registered ({years_since_registration} years ago {result.creation_date.year})"
            )
    
    print(f"{Fore.YELLOW}Available domains {len(available_domains)}....")
    Fore.RESET   

    for domain in available_domains:
        print(f"{Fore.GREEN}\N{check mark}  {domain} available.")

# --------------------------------------------------------

def main():
    check_if_registered(get_list_of_domains())

if __name__ == "__main__":
    main()
