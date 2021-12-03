from bs4 import BeautifulSoup
import requests
import argparse

parser = argparse.ArgumentParser(description = 'Check for Null tab index')
parser.add_argument('--link', type=str)
args = parser.parse_args()
url = args.link

# print('Verifying SSL certificate details........\n')
# time.sleep(2)

def check_tab(url):
    # url=input()
    html = requests.get(url).content
    c=0
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all():
        
        try:
            if len(tag['tabindex']) >0:
                attr=tag['tabindex']
                
                if int(attr)==0:
                    c=1
                    print("Null Tabindex found at :")
                    print(tag)
                    print("\n")
        except:
            continue
    if(c==0):
        print("No null tabindex found")

# check_tab(url)