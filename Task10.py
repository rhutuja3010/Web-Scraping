



import json 

with open("Task5.json", "r") as file:
    data=json.load(file)

def analysis_of_director_language(all_movie):
    d={}
    for i in range(len(all_movie)):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

        count=0
        for j in range(len(all_movie)):
            if all_movie[i]["Director:"]==all_movie[j]["Director:"]:
                if all_movie[i]["Original Language:"]==all_movie[j]["Original Language:"] or all_movie[i]["Original Language:"] !=all_movie[i]["Original Language:"]:
                    count+=1
                # else:
                    # pass
            d.update({all_movie[i]["Director:"]:{all_movie[i]["Original Language:"]:count}})
            # printJ(d)
    with open ("Task10_analysis_of_language_and_director.json","w") as f:
        json.dump(d,f,indent=4)
    return d
analysis_of_director_language(data)

