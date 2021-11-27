import requests
import json
from bs4 import BeautifulSoup
req=requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/")
htmlcontent=req.content
soup=BeautifulSoup(htmlcontent,"html.parser")

def srape_top_list():

    tabletag=soup.find("table" ,class_="table")
    # print(tabletag)
    table_td=tabletag.find_all("tr")
    # print(table_td)
    list1=[]
    year_release=[]
    for i in table_td[1:]:
        rank=i.find("td",class_="bold").get_text()
        # print(rank.get_text())
        rating=i.find("span",class_="tMeterScore").get_text()
        # print(rating.get_text().strip())
        title=i.find("a",class_="unstyled articleLink")
        a=(title.get_text().strip())
        # print(a)
        # break
        year=a[-5:-1]
        name=a[:-7]

        
        reviews=i.find("td",class_="right hidden-xs").get_text()
        # print(reviews.get_text())
        link=i.find("a",class_="unstyled articleLink")["href"]
        link1=("https://www.rottentomatoes.com")
        link3=link+link1
        # print(link1+link)
        # title=i.find("a",class_="unstyled articleLink").text.strip()
        movie_dict={}
        movie_dict['rank']=rank
        movie_dict['rating']=rating
        movie_dict['name']=name
        movie_dict['year']=year
        movie_dict['reviews']=reviews
        movie_dict['link3']=link3
        list1.append(movie_dict)
        # print(list1)

    with open("movies_deatials.json","w") as file:
        json.dump(list1,file,indent=4)
srape_top_list()


    