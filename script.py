import argparse
import time
from check import check_ssl
from tabindex import check_tab
from alttext import check_alttxt
import streamlit as st 
from bs4 import BeautifulSoup
from optparse import OptionParser, OptionGroup
from urllib.parse import urlparse
import sys
import xml.etree.ElementTree as ET
import requests
import json
import datetime
import re

user_agent = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0' }
requests.packages.urllib3.disable_warnings()

white = "\033[0m"
blue = "\033[94m"
green = "\033[0;32m"
red = "\033[91m"

def headersURL(line, info, nocolor, formatoutput, delay, timeout):
    """ page load and print data"""
    url = line.strip()
    if (urlparse(url).scheme == ''):
        url = 'http://%s'%url
    try:
        time.sleep(delay)
        r = requests.get(url, verify=False, allow_redirects=False, timeout=timeout)
        if (r.status_code == 302) and (len(r.cookies) == 0):
            r = requests.get(url, verify=False, allow_redirects=True, timeout=timeout)
        if (formatoutput == "normal"):
            printJson(line, r.cookies, info)
        elif (formatoutput == "xml"):
            printXML(line, r.cookies, info)
        elif (formatoutput == "csv"):
            if 1:
                st.write("url,cookie name,secure,httponly,value,path,expires")
            else:
                st.write("url,cookie name,secure,httponly")
            printCsv(line, r.cookies, info)
        elif (formatoutput == "grepable"):
            printGrepable(line, r.cookies, info)
    except:
        if (formatoutput == "normal"):
            st.write("[ERR] %s - Connection failed." % url)
        else:
            pass


def readFile(filename, info, nocolor, formatoutput, delay, timeout):
    """ Read file with the url list """
    try:
        with open(filename, "r") as f:
            for line in f:
                headersURL(line, info, nocolor, formatoutput, delay, timeout)
    except FileNotFoundError:
        st.write("[ERR] File not found.")


def printNormal(line, cookies, nocolor, info):
    if nocolor:
        color_blue = white
        color_red = white
        color_green = white
    else:
        color_blue = blue
        color_red = red
        color_green = green
    st.write("%s[*] URL: %s%s"%(color_blue,line.strip(),white))
    for cookie in cookies:
        name = cookie.name
        secure = cookie.secure
        httponly = cookie.has_nonstandard_attr("HttpOnly")
        if not httponly:
            httponlyResult = '%sHttpOnly: %s%s' % (color_red, str(httponly), white)
        else:
            httponlyResult = '%sHttpOnly: %s%s' % (color_green, str(httponly), white)
        if not secure:
            secureResult = '%ssecure: %s%s' % (color_red, str(secure), white)
        else:
            secureResult = '%sSecure: %s' % (color_green, str(secure))
        st.write("%s[*] Name: %s\n\t%s\n\t%s%s%s" % (white, name, secureResult, white, httponlyResult, white))
        if info:
            if cookie.expires is not None:
                expires = datetime.datetime.fromtimestamp(cookie.expires).strftime('%Y-%m-%d %H:%M:%S')
            else:
                expires = "Never"
            st.write("\tValue: %s\n\tPath: %s\n\tExpire: %s" % (cookie.value, cookie.path, expires))


def printGrepable(line, cookies, info):
    for cookie in cookies:
        name = cookie.name
        secure = cookie.secure
        httponly = cookie.has_nonstandard_attr("HttpOnly")
        if not httponly:
            httponlyResult = "NO"
        else:
            httponlyResult = "YES"
        if not secure:
            secureResult = "NO"
        else:
            secureResult = "YES"
        if info:
            if cookie.expires is not None:
                expires = datetime.datetime.fromtimestamp(cookie.expires).strftime('%Y-%m-%d %H:%M:%S')
            else:
                expires = "Never"
            st.write("URL: %s: Cookie: %s : Secure: %s : Httponly: %s : value: %s : path: %s : expires: %s" % (line.strip(), name, secureResult, httponlyResult, cookie.value, cookie.path, expires))
        else:
            st.write("URL: %s: Cookie: %s : Secure: %s : Httponly: %s" % (line.strip(), name, secureResult, httponlyResult))


def indent(elem, level=0):
    """ XML pretty print"""
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def printXML(line, cookies, info):
    allxml = ET.Element('url', {'site': line.strip()})
    for cookie in cookies:
        child = ET.SubElement(allxml, 'cookie')
        secure = cookie.secure
        httponly = cookie.has_nonstandard_attr("HttpOnly")
        if not httponly:
            httponlyResult = "NO"
        else:
            httponlyResult = "YES"
        if not secure:
            secureResult = "NO"
        else:
            secureResult = "YES"
        ET.SubElement(child, 'name').text = cookie.name
        ET.SubElement(child, 'secure').text = secureResult
        ET.SubElement(child, 'httponly').text = httponlyResult
        if info:
            if cookie.expires is not None:
                expires = datetime.datetime.fromtimestamp(cookie.expires).strftime('%Y-%m-%d %H:%M:%S')
            else:
                expires = "Never"
            ET.SubElement(child, 'value').text = cookie.value
            ET.SubElement(child, 'path').text = cookie.path
            ET.SubElement(child, 'expires').text = expires
    indent(allxml)
    ET.dump(allxml)


def printJson(line, cookies, info):
    cookies_output = []
    for cookie in cookies:
        secure = cookie.secure
        httponly = cookie.has_nonstandard_attr("HttpOnly")
        if not httponly:
            httponlyResult = "NO"
        else:
            httponlyResult = "YES"
        if not secure:
            secureResult = "NO"
        else:
            secureResult = "YES"
        data = {
            'name': cookie.name,
            'secure': secureResult,
            'httponly': httponlyResult
        }
        cookies_output.append(data)
        if info:
            if cookie.expires is not None:
                expires = datetime.datetime.fromtimestamp(cookie.expires).strftime('%Y-%m-%d %H:%M:%S')
            else:
                expires = "Never"
            data['value'] = cookie.value
            data['path'] = cookie.path
            data['expire'] = expires
    json_output = {
            'url': line.strip(),
            'cookies': cookies_output
        }
    st.json(json.dumps(json_output, indent=4, separators=(',', ': ')))


def printCsv(line, cookies, info):
    for cookie in cookies:
        name = cookie.name
        secure = cookie.secure
        httponly = cookie.has_nonstandard_attr("HttpOnly")
        if not httponly:
            httponlyResult = "NO"
        else:
            httponlyResult = "YES"
        if not secure:
            secureResult = "NO"
        else:
            secureResult = "YES"
        # If info option entered, print all
        if info:
            if cookie.expires is not None:
                expires = datetime.datetime.fromtimestamp(cookie.expires).strftime('%Y-%m-%d %H:%M:%S')
            else:
                expires = "Never"
            st.write("%s,\"%s\",%s,%s,\"%s\",%s,%s" % (line.strip(), name, secureResult, httponlyResult, cookie.value, cookie.path, expires))
        else:
            st.write("%s,\"%s\",%s,%s" % (line.strip(), name, secureResult, httponlyResult))


def googleSearch(domain, info, nocolor, formatoutput, delay, timeout):
    """ Google search, find subdomains and load pages"""
    
    g_url = "http://www.google.com/search?hl=es&q=site:%s&btnG=Google+Search" % domain
    r = requests.get(g_url, verify=False, headers=user_agent)
    soup = BeautifulSoup(r.text, "html.parser")
    domains = []
    g_pages = []
    top = soup.find('tr', attrs={'valign': 'top'})
    for page in top.find_all('a', attrs={'class': 'fl'}):
        g_pages.append('https://www.google.com%s'% page.get('href'))
    for site in soup.find_all('cite'):
        if re.match('^([a-z0-9]*)(.?)%s$' % domain, urlparse('//%s'% site.text).netloc) is not None:
            domains.append(urlparse('//%s' % site.text).netloc)
    for sites in g_pages:
            r = requests.get(sites, verify=False, headers=user_agent)
            soup2 = BeautifulSoup(r.text, "html.parser")
            for site in soup2.find_all('cite'):
                if re.match('^([a-z0-9]*)(.?)%s$' % domain, urlparse('//%s'% site.text).netloc) is not None:
                    domains.append(urlparse('//%s' % site.text).netloc)
    for url in set(domains):
        headersURL(url, info, nocolor, formatoutput, delay, timeout)



def opciones():
        st.write('----------------------Cookie Details------------------------')
        parser = OptionParser("usage: %prog [options] \nExample: ./%prog -i ips.txt")
        parser.add_option("-i", "--input",
                  action="store", type="string", dest="input", help="File input with the list of webservers")
        parser.add_option("-l", "--link",
                  action="store", type="string", dest="url", help="URL")
        parser.add_option("-f", "--format",
                  action="store", type="string", dest="format", default="normal", help="Output format (json, xml, csv, normal, grepable)")
        parser.add_option("-g", "--google",
                  action="store", dest="google", help="Search in google by domain")
        parser.add_option("--nocolor",
                  action="store_true", dest="nocolor", default=False, help="Disable color output")
        parser.add_option("-n", "--info",
                  action="store_true", dest="info", default=False, help="Information")
        group = OptionGroup(parser, "Performance")
        group.add_option("-t", type="float", dest="timeout", default=1.0, help="Response Timeout")
        group.add_option("-d", type="float", dest="delay", default=0.0, help="Delay between requests")
        parser.add_option_group(group)
        (options, args) = parser.parse_args()
        if (len(sys.argv) == 1):
            parser.print_help()
        elif (options.input is not None):
            readFile(options.input, options.info, options.nocolor, options.format, options.delay, options.timeout)
        elif (options.url is not None):
            headersURL(options.url, options.info, options.nocolor, options.format, options.delay, options.timeout)
        elif (options.google is not None):
            googleSearch(options.google, options.info, options.nocolor, options.format, options.delay, options.timeout)


# if __name__ == "__main__":
    

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
time.sleep(2)
opciones()
