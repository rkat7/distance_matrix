x=[]
y=[]

for j in range(3):
n=int(input(&quot;enter x&quot;+str(j)+&quot;:&quot;))
x.append(n)
for i in range(3):
m=int(input(&quot;enter y&quot;+str(i)+&quot;:&quot;))
y.append(m)

def euclidean(x,y):
s=0
for i in range(3):
s+=(x[i]-y[i])**2
return(s**1/2)

def manhattan(x,y):
s=0
for i in range(3):
s+=abs(x[i]-y[i])
return(s)

def minkowski(x,y):
q=int(input(&quot;enter q:&quot;))

s=0
for i in range(3):
s+=(abs(x[i]-y[i]))**q
return(s**1/q)

#Created distance functions

#Now building the matrix

def euclidean(x,y):
s=0
for i in range(4):
s+=(x[i]-y[i])**2
return(s**1/2)

from sklearn import datasets
import numpy as np
import pandas as pd
d=datasets.load_iris()
df=pd.DataFrame(data=d[&#39;data&#39;])

distance_metric=np.zeros((len(df),2))

i=int(input(&quot;enter a no b/w 0 and 3:&quot;))
j=int(input(&quot;enter a no b/w 0 and 3:&quot;))

m1=df.loc[i]
m2=df.loc[j]

s2=0

for x in range(len(df)):
s1=0
for y in range(4):
s1+=euclidean(m1,df.loc[x])
distance_metric[x][0]=s1

for x in range(len(df)):
s2=0
for y in range(4):
s2+=euclidean(m2,df.loc[x])
distance_metric[x][1]=s2

print(distance_metric)

