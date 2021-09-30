# Scrapping a Coinmarketcap.com
## Installation
If you have pip on your system, you can simply install **selenium** and **BeautidulSoup 4** using these following:
```
pip install -U selenium
```
```
pip install bs4
```
It also requires [geckodriver](https://github.com/mozilla/geckodriver/releases)
## Usage
* Import those libraries
* Open a new Firefox browser
* Load the page at the given URL
### Example 1
```
from bs4 import BeautifulSoup as soup
from selenium import webdriver

url = 'https://coinmarketcap.com/currencies/' + cryptoName + '/news/'
driver = webdriver.Firefox()
driver.get(url)
```
* Parse the web page using BeautifulSoup as soup
* Toke the news articles using findAll() method
* Print them out taking only text that is inside tags
### Example 2
```
page = driver.page_source
page_soup = soup(page, 'html.parser')
        
result = page_soup.findAll("section", "wrapper")

print(result[0].text)
```
In src.py, these are demonstrated differently, more complex.
