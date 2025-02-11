from bs4 import BeautifulSoup
import requests
import argparse
import streamlit as st

parser = argparse.ArgumentParser(description = 'Check for images without Alt text')
parser.add_argument('--link', type=str)
args = parser.parse_args()
url = args.link

def check_alttxt(url):
    st.write('-----------------Images without Alt text reports-----------------')
    html = requests.get(url).content
    c=0
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all("img"):
        #print(tag)
        try:
            if len(tag['alt']) >0:
                continue
        except:
            st.write("No alt text found at :")
            st.write(str(tag))
            st.write("/n")
            c=c+1
    if(c==0):
        st.write("Every image has an alt text")