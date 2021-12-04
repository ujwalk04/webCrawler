# WebCrawler
***

## Contributed by:
***
* [Shivam Mishra](https://github.com/7shivamx)
* [Suryansh](https://github.com/0Suryansh)
* [Ujwal Kumar](https://github.com/ujwalk04)
* [Rajarshi Dutta](https://github.com/Rajarshi1001)
***

## Problem Statement
***
We had to develop a web crawler which would identify the following key components :
* **SSL certificate compliance** – Check all links in the site for URL validation of SSL (all
hyperlinks should be https://), and verify the validity of the SSL certificate.
* **Cookie checker** – Verify cookies being used by the website, the cookie checker will scan
the cookies on the website, and cookie consent verification links.
* **ADA compliance**
    * Alt text in all images.
    * Color contrast for the site as per w3.org guidelines.
    * Accessibility issues to check the site markup for null tab index
   
## Approach
***
* Note to be taken that you are in the correct directorty before running the program
* Here you can run the program individually for each type of problem
* Here we have used streamlit to render the results in a web-interface instead of displaying it in the terminal. The __SSL Certificate__ details (if enabled) of the website and the info regarding null tab index and the __image tags__ without __alt text__ are displayed in a local URL.
* We have also used streamlit to display information regarding the __cookies__ present in a website.

## Libraries used :
***
```
ssl
socket
prettytable
streamlit
beautifulsoup
requests
optparse
urllib
xml
datetime
```

## Usage

* Clone the repository  `git clone https://github.com/Rajarshi1001/webCrawler.git`
* Install the requirements `pip install -r requirements.txt`
* ```py pip install streamlit ```
Specify the url using --link option while executing the script.

#### This Script displays the ssl details , img tags without alt-text, null tab index.(e.g = https://github.com)
#### Run the following command 
```py
py -m streamlit run script.py -- --link https://github.com
```

#### This Script shows the details about the __cookies__ present in the site (e.g = https://github.com)
#### Run the following command 
```py
py -m streamlit run cookies.py -- -u https://github.com -f json
```
<!-- #### For SSL-Certificate compilance test:
```
python3 check.py
```
#### For Cookie- test:
```
python3 cookies.py
``` -->
#### For Alt-text :
Firstly head to the correct directory `cd .\webCralTF\webCralTF\` (yes twice) then run
```
scrapy crawl spidey
```
#### For color-contast :
Firstly head to the correct directory then run
```
python colContr.py
```
<!-- #### For tab-Index navigation :
```
python3 tabindex.py
``` -->
