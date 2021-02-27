import requests
from bs4 import BeautifulSoup

url = 'https://www.google.co.il/'
r = requests.get(url)
soup = BeautifulSoup(r.text)

for link in soup.select('a.smallheader'):
    print(link.text)