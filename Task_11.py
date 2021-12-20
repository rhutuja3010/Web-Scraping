import json
# from 5 import all
with open("Task5.json", "r") as file:
    data=json.load(file)

def analyse_movies_genre():
    genre_dict={}
    list1=[]
    for i in data:
        genre=i["Genre:"].split(",")
        for j in genre:
            list1.append(j)
        # print(list1)
        count=0
        for k in list1:
            count+=1
            genre_dict.update({j:count})
        with open("11_analysis_movies_genre.json","w") as f:
            json.dump(genre_dict,f,indent=4)
analyse_movies_genre()