import requests
from bs4 import BeautifulSoup

def makearequest():
    URL = "https://www.ft.com/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="site-content")
    block_element = results.find("div", class_="o-grid-row o-teaser-collection top-stories__freeform-row js-track-scroll-event")
    print(block_element)
    story_elements = block_element.find_all("div", class_="o-teaser__heading")
    titles = []
    for element in story_elements:
        title = element.find("a", class_="js-teaser-heading-link")

        print(title['href'])
        titles.append(title.contents[0])
    return titles


