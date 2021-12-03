# WebCrawler

Submitted by Team 217164.

## Description

Here we have covered the SSL certificate compliance,cookie-checker and ADA compilance covering alt text detection from the images and checking the color contrast and the presence of the null tab index in the website.

## Libraries to be installed
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

## How to run the program
Starting from cloning the repo in your machine by running command
`git clone https://github.com/Rajarshi1001/webCrawler.git`
then install all the libraries used, mentioned in the 'requirements.txt'

### Installing Libraries

* To install all the libraries just run `pip install -r requirements.txt` in the terminal

### Executing program

* Note to be taken that you are in the correct directorty before running the program
* Here you can run the program individually for each type of problem
* Here we have used streamlit to render the results in a web-interface instead of displaying it in the terminal. The __SSL Certificate__ details (if enabled) of the website and the info regarding null tab index and the __image tags__ without __alt text__ are displayed in a local URL.
* We have also used streamlit to display information regarding the cookies present in a website.
#### Install streamlit using the following command

```py
pip install streamlit 
```

Specify the url using --link option while executing the script.

#### This scriipt displays the ssl details , img tags without alt-text, null tab index.(e.g = https://github.com)
#### Script 
```py
py -m streamlit run script.py -- --link https://github.com
```

#### This script shows the details about the cookies present in the site (e.g = https://github.com)
#### Script
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
