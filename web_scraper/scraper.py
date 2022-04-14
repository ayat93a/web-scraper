import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/History_of_Mexico  '

res = requests.get(URL)
soup = BeautifulSoup(res.content, "html.parser")

def get_citations_needed_count(URL):
    count = 1
    for cite in soup.find("div", class_="").find_all(""):
        for i in cite.find_all('', title=""):
            count += 1
    return count

def get_citations_needed_report(URL):
    pass