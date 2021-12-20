import json
import requests
from bs4 import BeautifulSoup
from Task1 import scrapped
# with open("Task1.json", "r") as file:
    # data=json.load(file)


def scrape_movie_cast(url1):
    list1=[]
    req=requests.get(url1)
    # print(req)
    soup=BeautifulSoup(req.text,"html.parser")
    table=soup.find("div",class_="castSection")
    tr=table.find_all("div",class_="cast-item media inlineBlock")

    for i in tr[1:]:
        url=i.find("a",class_="unstyled articleLink")
        link1=url.get_text()
        link=url["href"]
        name=i.find("span").get_text().strip()
        dict1={}
        dict1["url"]=link
        dict1["name_of_actor"]=name
        list1.append(dict1)
    with open("Task12_scrape_movie_cast.json","w") as f:
        json.dump(list1,f,indent=4)
url1=scrapped[0]["url"]
scrape_movie_cast(url1)



