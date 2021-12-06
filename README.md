# WebCrawler

Submission of Team MA-217164
## Contributed by:
* [Shivam Mishra](https://github.com/7shivamx)
* [Suryansh](https://github.com/0Suryansh)
* [Ujwal Kumar](https://github.com/ujwalk04)
* [Rajarshi Dutta](https://github.com/Rajarshi1001)
***

## Problem Statement
We had to develop a web crawler which would identify the following key components :
* __SSL certificate compliance__ – Check all links in the site for URL validation of SSL (all
hyperlinks should be https://), and verify the validity of the SSL certificate.
* __Cookie checker__ – Verify cookies being used by the website, the cookie checker will scan
the cookies on the website, and cookie consent verification links.
* __ADA compliance__
    * Alt text in all images.
    * Color contrast for the site as per w3.org guidelines.
    * Accessibility issues to check the site markup for null tab index
***
## Approach

* The user can run the program individually for each type of problem. There is also a combined script for all executing all tasks.
* We have used streamlit to render the results in a web-interface instead of displaying it in the terminal. The __SSL Certificate__ details (if enabled), __cookies__ present, verification attribute, info regarding __null tab index__ and the __image tags__ without __alt text__ of a website are displayed in a local URL.

***
## Libraries used :

```
ssl
socket
prettytable
streamlit
beautifulsoup
requests
urllib
```
***
## Usage

* Clone the repository  `git clone https://github.com/Rajarshi1001/webCrawler.git`
* Install the requirements `pip install -r requirements.txt`
* ```py pip install streamlit ```
Specify the url using --link option while executing the script.

#### This Script displays the ssl details, verification & details about the cookies being used by the website, img tags without alt-text and null tab index. (e.g = https://github.com)

#### Run the following command 
```py
py -m streamlit run script.py -- --link https://github.com
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
Firstly head to `cd .\webCralTF\webCralTF\` (yes twice) then run
```
scrapy crawl spidey
```
#### For color-contast :
Now head to the correct directory then run
```
python colContr.py
```
<!-- #### For tab-Index navigation :
```
python3 tabindex.py
``` -->
