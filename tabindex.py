from bs4 import BeautifulSoup
import requests
import argparse
import streamlit as st

parser = argparse.ArgumentParser(description = 'Check for Null tab index')
parser.add_argument('--link', type=str)
args = parser.parse_args()
url = args.link

# print('Verifying SSL certificate details........\n')
# time.sleep(2)

def check_tab(url):
    # url=input()
    st.write('----------------------Null tab index reports------------------------')
    html = requests.get(url).content
    c=0
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all():
        
        try:
            if len(tag['tabindex']) >0:
                attr=tag['tabindex']
                
                if int(attr)==0:
                    c=1
                    st.write("Null Tabindex found at :")
                    st.write(str(tag))
                    st.write("\n")
        except:
            continue
    if(c==0):
         st.write("No null tabindex found")
