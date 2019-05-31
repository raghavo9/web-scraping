from bs4 import BeautifulSoup
import requests

# (we are scraping the links from the wikipedia url="https://en.wikipedia.org/wiki/Machine_learning")

source=requests.get("https://en.wikipedia.org/wiki/Machine_learning").text
soup=BeautifulSoup(source,'lxml')



counter=0                  #counter variable declared to count total number of links printed
#for grabbing all the links in the site
for link in soup.find_all("a",href=True):
    #print(link['href'])
    txt=link['href']        #here we used link['href'] so as to ensure that link should contain the href value also
    
    if (txt[0]=='#' or txt[0:2]=='//'):
        pass
    elif (txt[0:4]=="http"):
        print(txt)
        counter+=1
    else:
        string=("https://en.wikipedia.org{}".format(txt))
        print(string)
        counter+=1
print(" ")
print("total number of links printed are :",counter)
