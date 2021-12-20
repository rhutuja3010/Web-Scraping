
import json
import random
import time
from Task4 import scrap_movies_details
from Task1 import scrapped
import os
def text_file():
    for i in range(10):
        url_name=scrapped[i]["url"]
        # print(url_name)
        url=scrapped[i]["url"][33:]
        # print(movie_name)
        # NAME=scrapped[i]["name"]
        # URL="/home/rhutujapatil/Desktop/Web Scaping/"+url+".json"
        URL="/home/rhutujapatil/Desktop/Web Scaping/"+url+".json"
        file =os.path.exists(URL)
        if file ==True:
            with open (file,"r") as f:
                var=json.load(f)
                # print(var)
        else:
            print("file is doesnt exist ")
            information=scrap_movies_details(url_name)
            rd=random.randint(1,3)
            time.sleep(rd)
            with open(URL,"a") as file :
                json.dump(information,file,indent=4)
          
text_file()