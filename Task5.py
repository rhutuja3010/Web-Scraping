import requests
import json
from bs4 import BeautifulSoup
from Task1 import *
from Task4 import scrap_movies_details
scrapped=scrape_top_list()

def get_movie_details(all_movies):
    i=0
    list1=[]
    while i<100:
        # print(i)
        url_of_movies=all_movies[i]['url']
        # print(url_of_movies)
        
        data=scrap_movies_details(url_of_movies)
        list1.append(data)
        print(list1)
        i+=1
    with open("Task5.json","w") as file:
        json.dump(list1,file,indent=4)
    # return list1
all=get_movie_details(scrapped)