# import requests
# import json
# from bs4 import BeautifulSoup
# req=requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/")
# htmlcontent=req.content
# soup=BeautifulSoup(htmlcontent,"html.parser")


import requests
import json
from Task1 import *
movies=scrape_top_list()
# movies=scrape_top_list()
# print(type(movies))
def group_by_year(m):
    year1=[]
    for i in m:
        # print(i)
        year=i["year"]
        # print(year)
        if year not in year1:
            year1.append(year)
            # print(year)
    dict_of_movies={i:[] for i in year1}
    for i in movies:
        year=i["year"]
        for j in dict_of_movies:
            if str(j)==str(year):
                dict_of_movies[j].append(i)
                # print(dict_of_movies[j])
    with open("movies_release_year.json","w") as file:
        json.dump(dict_of_movies,file,indent=2)
    return dict_of_movies
# print(group_by_year(movies))
group_by_year(movies)




