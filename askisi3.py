from bs4 import BeautifulSoup, SoupStrainer
import requests
from bs4 import *
from urllib import request

url = input("Γραψτε τη σελίδα url που θέλετε να αναζητείσεται:")

page = requests.get(url)    
data = page.text
soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))