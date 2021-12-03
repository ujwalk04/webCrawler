# WebCrawler

Submitted by Team 217164.

## Description

Here we have covered the SSL certificate compliance,cookie-checker and ADA compilance covering alt text detection from the images and checking the color contrast and the presence of the null tab index in the website.

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

### Install streamlit using the following command

```py
pip install streamlit 
```

Specify the url using --link option while executing the script.

#### Script for streamlit
```py
py -m streamlit run script.py -- --link <url>
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
