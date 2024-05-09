#This will not run on online IDE 
import requests 
from bs4 import BeautifulSoup 

URL = "https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/" 
r = requests.get(URL) 

soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 
print(soup.prettify()) 
