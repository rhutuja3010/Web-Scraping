import json
def analyse_movies_language():
    list1=[]
    with open("Task5.json","r") as f:
        language=json.load(f)
    # print(language)
    for i in language:
        # print(i)    
        if i["Original Language:"] not in list1:
            # print(i)
            # print(i["Original Language:"])
            list1.append(i["Original Language:"]) 
    # # print(list1)
    #     # if i["Original Language:"] not in language:
    #         # print(i["Original Language:"])
    mydict={}  
    for j in list1:
        # print(j) 
        count=0
        i=1
        while i<len(language):
            if j==language[i]["Original Language:"]:
                count+=1
            i+=1
        mydict.update({j:count}) 

        
    with open("task6 languages_analysis.json","w") as f:
        json.dump(mydict,f,indent=3)
analyse_movies_language()




































# list1=["q","w","a","c","o","a","q","o","q","a"]
# i=0
# a=[]
# count=0
# while i<len(list1):
#     j=0
#     b=[]
#     while j<len(list1):
#         if list1[i]==list1[j]:
#             count+=1
#         j+=1
# b.append(list1[i])
# print(b)
# b.append(count)
# # print(b)
#     # if b not in a:
#         # a.append(b)
# i+=1
# # print(a) 
    

    