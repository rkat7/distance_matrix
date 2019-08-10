from sklearn import datasets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

d=datasets.load_iris()
df=pd.DataFrame(data=d['data'])
scat_dataset=np.zeros((150,2))

for i in range(len(df)):
    scat_dataset[i][0]=df[0][i]
    scat_dataset[i][1]=df[1][i]

for i in range(len(df)):
    wq=plt.scatter(scat_dataset[i][0],scat_dataset[i][1])
print(wq)
