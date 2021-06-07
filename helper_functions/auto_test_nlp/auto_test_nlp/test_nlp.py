#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import requests
import pprint
import urllib

with open("automated_test.txt", encoding="utf8") as f_test:
    test_auto = f_test.readlines()
f_intent = open('automated_fail_intent.txt','w')
f_tag = open('automated_fail_tag.txt','w')
f_gnj_place = open('automated_fail_gnj_place.txt','w')
count=0
count_intent=0
count_tag=0
count_gnj_place=0
for sentence in test_auto:
    clean_sentence=sentence.split("\n")[0]
    url="http://testgnjnlp.herokuapp.com/api/chunks/vi/"+ urllib.parse.quote_plus(clean_sentence.split(";")[0])
    print(url)
    url=url.replace("+","%20")
    response2  = requests.get(url)
    count+= 1
    print('Testing case #'+str(count)+": "+clean_sentence.split(";")[0])
    valid_intent=clean_sentence.split(";")[1]    
    if (clean_sentence.split(";")[2]=='null'):
        valid_tag=[]
    else:
        valid_tag=clean_sentence.split(";")[2].split(",")    
    if (clean_sentence.split(";")[3]=='null'):
        valid_gnj_place=[]
    else:
        valid_gnj_place=clean_sentence.split(";")[3].split(",")
    predict_intent=response2.json()['entities']['intent'][0]['value']
    predict_tag=[]
    for tag in response2.json()['entities']['tag']:
        predict_tag.append(tag['value'])
    predict_gnj=[]
    for gnj in response2.json()['entities']['gnj_place']:
        predict_gnj.append(gnj['value'])
    valid_tag.sort()
    predict_tag.sort()
    valid_gnj_place.sort()
    predict_gnj.sort()
    correct_tag=True
    correct_gnj=True
    correct_intent=True
    if (predict_intent!=valid_intent):
        correct_intent=False
    if (len(valid_tag)!=len(predict_tag)):
        correct_tag=False
    else:
        for i in range(0,len(valid_tag)):
            if(valid_tag[i]!=predict_tag[i]):
                correct_tag=False
                break
    if (len(valid_gnj_place)!=len(predict_gnj)):
        correct_gnj=False
    else:
        for i in range(0,len(valid_gnj_place)):
            if(valid_gnj_place[i]!=predict_gnj[i]):
                correct_gnj=False
                break
    if(correct_intent):
        count_intent +=1
    else:
        f_intent.write(clean_sentence.split(";")[0]+":"+valid_intent+"<===>"+predict_intent.encode('utf-8')+"\n")
    if(correct_tag):
        count_tag +=1
    else:
        f_tag.write(clean_sentence.split(";")[0]+":"+','.join(valid_tag)+"<===>"+','.join(predict_tag).encode('utf-8')+"\n")
    if(correct_gnj):
        count_gnj_place +=1
    else:
        f_gnj_place.write(clean_sentence.split(";")[0]+":"+','.join(valid_gnj_place)+"<===>"+','.join(predict_gnj).encode('utf-8')+"\n")

print("Correct Intent: "+str(count_intent)+"/"+str(count))    
print("Correct Tag: "+str(count_tag)+"/"+str(count))
print("Correct Gnj Place: "+str(count_gnj_place)+"/"+str(count))

    


#result["entities"]["gnj_place"].sort(key=lambda x: x['confidence'], reverse=True)
    
