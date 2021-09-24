import requests
from bs4 import BeautifulSoup

def makearequest():
    URL = "https://www.thesun.co.uk/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="main-content")
    block_element = results.find_all("div", class_="teaser-item teaser__large")
    titles = []
    for element in block_element:
        title = element.find("p", class_="teaser__subdeck")
        titles.append(title.contents[0])
    return titles
