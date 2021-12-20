import requests
import json
from bs4 import BeautifulSoup
from Task4 import scrap_movies_details
from Task1 import scrapped
import os
def making_file(URL):
    for i in scrapped:
        if i["url"]==URL:
        # print(i)
            url1=i["url"][33:]
            # print(url1)
            NAME=i["name"]
            # print(name)
            file=os.path.exists("/home/rhutujapatil/Desktop/Web Scaping/"+url1 +".json")
            if file==True:
                with open(file,"r") as f:
                    v=json.load(f)
                    # print(v)
            else:
                print("file is doesnt exist")
                info=scrap_movies_details(i["url"])
                with open("Task8,url1.json","w")as fi:
                  json.dump(info,fi,indent=3)

                return info
url=scrapped[0]["url"]  
making_file(url) 



