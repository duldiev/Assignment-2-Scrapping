from bs4 import BeautifulSoup as soup
from selenium import webdriver

class Scrapper:
    def getArticles(self, cryptoName):
        url = 'https://coinmarketcap.com/currencies/' + cryptoName + '/news/'

        driver = webdriver.Firefox()
        driver.get(url)

        page = driver.page_source
        page_soup = soup(page, 'html.parser')

        headers = page_soup.findAll("h3", {"class": "sc-1q9q90x-0", "class": "gEZmSc"})
        paragraphs = page_soup.findAll("p", {"class": "sc-1eb5slv-0", "class": "svowul-3", "class": "ddtKCV"})

        print('Latest news about', cryptoName.capitalize(), end=':')
        print()
        for i in range(0, min(len(headers), len(paragraphs))):
            print('Article', (i + 1), end=':')
            print()
            print(headers[i].text.strip(), '\n', 'More:', paragraphs[i].text.strip(), '\n')