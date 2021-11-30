from typing import Text
import requests
import json
from bs4 import BeautifulSoup
from Task1 import scrapped
from pprint import pprint

def scrap_movies_details(movie_url):
    page=requests.get(movie_url)
    soup=BeautifulSoup(page.text,"html.parser")
    title_div=soup.find("ul",class_="content-meta info")
    sub_title=title_div.find_all("li",class_="meta-row clearfix")
    
    movie_dict={}
    for i in sub_title:
        # print(i.get_text())
        key=i.find("div",class_="meta-label subtle").get_text()
        # print(key)

        Value=(i.find("div",class_="meta-value").text.replace(" ","").replace("\n","").strip())
        # print(Value)
        
        movie_dict.update({key:Value})
        # print(movie_dict)
        with open("movie_information.json","w") as file:
            json.dump(movie_dict,file,indent=4)
        # return movie_dict
# for i in scrapped:


scrap_movies_details("https://www.rottentomatoes.com/m/black_panther_2018")



    

