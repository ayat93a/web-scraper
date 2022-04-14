import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/History_of_Mexico  '

res = requests.get(URL)
soup = BeautifulSoup(res.content, "html.parser")

def get_citations_needed_count(URL):
    pass

def get_citations_needed_report(URL):
    pass