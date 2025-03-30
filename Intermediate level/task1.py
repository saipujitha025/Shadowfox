#python progrma to perform web scraping
import requests
from bs4 import BeautifulSoup


#fetching the website
r=requests.get('https://www.geeksforgeeks.org/python-web-scraping-tutorial/')
print(r)


#parse the html content
soup=BeautifulSoup(r.content,'html.parser')
print(soup.prettify())

#Extracting specific elements
titles = soup.find_all('h1')
for title in titles:
    print(title.text)
