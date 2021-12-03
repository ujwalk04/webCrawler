import argparse
import time
from check import check_ssl
from tabindex import check_tab
from alttext import check_alttxt
import streamlit as st 

parser = argparse.ArgumentParser(description = 'Check SSL certificate and null tab index')
parser.add_argument('--link', type=str)
args = parser.parse_args()
hostname = args.link.split('://')[1]
print('Checking for Null Tab Index.........\n')
time.sleep(2)
check_tab(args.link)
print('Checking for image tags without alt text.......\n')
time.sleep(2)
check_alttxt(args.link)

print('Verifying SSL certificate details........\n')
time.sleep(2)

check_ssl(hostname)
