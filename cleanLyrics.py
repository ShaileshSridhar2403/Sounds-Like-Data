#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 16:52:44 2018

@author: shailesh
"""

import pandas as pd
import enchant
import statsmodels.api as sm


d = enchant.Dict("en_US")
fp = open("/home/shailesh/Desktop/GitRepos/Sounds-Like-Data/mxm_dataset_train.txt","r");
fp2 = open("/home/shailesh/Desktop/GitRepos/Sounds-Like-Data/mxm_779k_matches.txt","r");
s = fp.readline();
s = s[1:]
lWords = s.split(',');
lWords.insert(0,"NULL")
indexList = [i for i in range(1,len(lWords)) if d.check(lWords[i])]
#l_ = [i for i in lWords if d.check(i)]
d = {}
songList = []
songVectorList =[]
tmp = fp.readline()
while tmp:
    songList.append(tmp)
    tmp = fp.readline()
counter = 0
for i in range(19):
    tmp = fp2.readline()
while(tmp):
    l = tmp.split("<SEP>")
    d[l[0]] = l[2]
    tmp = fp2.readline()
    
    
    
for i in songList[:10000]:
    print(counter)
    counter+=1
    countList = i.split(",")
    vector = [0 for i in range(len(lWords))]
    #print(i)
    for j in countList[2:]:
        vals = j.split(":")
        index = int(vals[0])
        count = int(vals[1])
        vector[index] = count;
        #print("   ",j)
    songVectorList.append((countList[0],countList[1],vector))
        
df = pd.read_csv("/home/shailesh/Desktop/GitRepos/Sounds-Like-Data/Million_Song_Subset.csv")
rows = []
y =[]
finList = []
for i in songVectorList:
  if i[0] in d.keys():
      row = df.loc[df['title'] == d[i[0]]]
      if row.shape[0] ==1:
          rows.append(row)
          finList.append((i,row['artist.hotttnesss'].iloc[0]));
          print(row)
      
x = [i[0][2] for i in finList]
y = [i[1] for i in finList]
xtrain = x[:2000]
xtest = x[2000:]
ytrain = y[:2000]
ytest = y[:2000]
model = sm.OLS(ytrain, xtrain).fit()
predictions = model.predict(xtest)