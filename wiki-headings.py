from bs4 import BeautifulSoup
import requests

source=requests.get("https://en.wikipedia.org/wiki/Machine_learning").text
soup=BeautifulSoup(source,'lxml')

for headline in soup.find_all(class_="mw-headline"):
    print(headline.text)

print(" ")
print(" ")

#for printing all the headings of table of content(if any)

var=soup.find(class_="toc").text
print(var)
