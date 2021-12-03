import argparse
import time
from check import check_ssl
from tabindex import check_tab

parser = argparse.ArgumentParser(description = 'Check SSL certificate and null tab index')
parser.add_argument('--link', type=str)
args = parser.parse_args()
hostname = args.link.split('://')[1]
print('Checking for Null Tab Index.........\n')


check_tab(args.link)
print('Verifying SSL certificate details........\n')
time.sleep(2)

check_ssl(hostname)
