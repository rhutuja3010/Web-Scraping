import json
from Task1 import *
# decade1=scrape_top_list(scrapped)
def gruop_by_decade(scrapped):
    moviesdict={}
    list2=[]
    for i in scrapped:
        # print(i)
        modulus=int(i["year"])%10
        # print(modulus)
        decade=int(i["year"])-modulus
        # print(decade)
        if decade not in list2:
            # print(decade)
            list2.append(decade)
    # print(list1)
    list2.sort()
    # print(list2)
    # moviesdict={}
    list3=[]
    for j in list2:
        # print(j)
        moviesdict[j]=[]
        print(moviesdict)
        for k in scrapped:
            # print(i)
            if int(k['year'])>=j and int(k['year'])<=j+9:
                moviesdict[j].append(k)

                
    with open ("movies_of_decane.json","w") as file:
        json.dump(moviesdict,file,indent=4) 
        # print(moviesdict)
    return moviesdict   

gruop_by_decade(scrapped)


