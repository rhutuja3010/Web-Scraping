
import json
def analyse_movies_directors():
    list1=[]
    with open("Task5.json","r") as f:
        directors=json.load(f)
    # print(directors)
    for i in directors:
        # print(i)
        if i["Director:"] not in list1:
            # print(i["Director:"])
            list1.append(i["Director:"]) 
    # print(list1) 
    mydict={}  
    for j in list1:
        # print(j) 
        count=1
        i=1
        while i<len(directors):
            
            if j==directors[i]["Director:"]:
                count+=1
            i+=1
        mydict.update({j:count}) 
    with open("task7 directors_analysis.json","w") as f:
        json.dump(mydict,f,indent=3)
analyse_movies_directors()



