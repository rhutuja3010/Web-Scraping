import json
# from Task1 import *
# scrapped=scrape_top_list()
# # movies=scrape_top_list()
# # print(movies)
# # break   
# def group_by_year(movies):
#     year1=[]
#     for i in movies:
#         print(i)
#         year=i["year"]
#         # print(year)
#         if year not in year1:
#             year1.append(year)
#             # print(year)
#     dict_of_movies={i:[] for i in year1}
#     # print(dict_of_movies)
#     for i in movies:
#         # print(i)
#         year=i["year"]
#         # print(year)
#         for j in dict_of_movies:
#             # print(j)
#             if str(j)==str(year):
#                 dict_of_movies[j].append(i)
#     #             # print(dict_of_movies[j])
#     with open("movies_release_year.json","w") as file:
#         json.dump(dict_of_movies,file,indent=2)
#     return dict_of_movies
# # print(group_by_year(movies))
# group_by_year(scrapped)


import json
from Task1 import scrapped
# scrapped=scrape_top_list()

def group_by_year(movies):
    year1=[]
    for i in movies:
        # print(i)
        if i["year"] not in year1:
            year1.append(i["year"])
            # print(year1)
    dict_of_movies={}
    for y in year1:
        # print(y)
        list_of_movies=[]
        for j in movies:
            # print(j)
            if j["year"]==y:
                list_of_movies.append(j)
                # print(list_of_movies)
        dict_of_movies.update({y:list_of_movies})
        # print(dict_of_movies )
    with open("movies_release_year.json","w") as file:
        json.dump(dict_of_movies,file,indent=2)
    return dict_of_movies
# print(group_by_year(scrapped)
decade1=group_by_year(scrapped)

# print(dec_arg)

