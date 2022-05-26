# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 14:05:20 2022

@author: NITISHARIHARAN K S
"""

import pandas as pd
data=pd.read_excel("D:/dataminigfiles/assignment file/K assign/Datasets_Kmeans/EastWestAirlines (1).xlsx",sheet_name='data')
data.info()
data.describe()
data.head()
#checking duplicate value
data.duplicated().sum()  #duplicate is present

#missing value

data.isna().sum()

data.columns.values

#zero variance checking

data.var()==0

#checking outliers

'''In this data outlier calculating will not make sense because some will have more balanc
e and number of miles counted will be differ to every Id one is selected and other is not
 selected so it represent in large value'''
 
 
 # doing normalisation
def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x 

df_norm=norm_func(data.iloc[:,1:])



#measure of central tendency
df_norm.mean()


#measure of spread or dispersion
df_norm.var()

#measure of skewness
df_norm.skew()

#measure of kurtosis
df_norm.kurt()



#doing  clustering

from scipy.cluster.hierarchy import linkage,dendrogram

#importing linkage,dendrogram fron scipy.cluster.hierachy package
z=linkage(df_norm,method='complete',metric='euclidean')
plt.figure(figsize=(15,8));plt.title('Hierarchial clustering Dendrogram');plt.xlabel('Index');plt.ylabel('Distance')
dendrogram(z,leaf_rotation=0,leaf_font_size=10)

from sklearn.cluster import AgglomerativeClustering

h=AgglomerativeClustering(n_clusters=4,linkage='complete',affinity='euclidean').fit(df_norm)
h.labels_

cluster_labels=pd.Series(h.labels_)
data['cluster_labels']=cluster_labels

data=data.iloc[:,[12,0,1,2,3,4,5,6,7,8,9,10,11]]
data.iloc[:,:].groupby(data.cluster_labels).mean()



data.to_csv('Airlines',encoding='utf-8')
import os
os.getcwd() 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
