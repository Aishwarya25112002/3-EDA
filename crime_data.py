# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 13:57:28 2023

@author: hp
"""

import pandas as pd
import numpy as np

df=pd.read_csv("crime_data.csv")
df

df.shape
##########
df.size
df
################
df.columns
####################
df.columns.values
df
###################
df.index
df
######################
df.dtypes
########################
df['Assault']
####################
df[['Assault','Murder']]
############################
#select certain rows
df2=df[6:]
df2
#################################
df['Assault']=df['Assault']-600
df['Assault']
#convert datatypes
df1=df.convert_dtypes()
df1.dtypes

##################################
df=df.astype(str)
print(df.dtypes)
###############################
df=df.astype({"Assault":int,"UrbanPop":float})
print(df.dtypes)
############################################

#convert data type all column in list
cols=['UrbanPop','Assault']
df[cols]=df[cols].astype('float')
df.dtypes
##################################################
#ignore error
df=df.astype({"Assault":float},errors='ignore')
df.dtypes

####################################################
#rename  the column
df.columns=['Assault','UrbanPop','Murder']
df
df2=df.rename({'Murder':'C1','Assault':'C2','UrbanPop':'C4'},axis=1)
df2
#####################################################
#generate error
df=df.dtype({"UrbanPop":int},errors='raise')
df
#######################
#convert feed column to numeric type
df=df.astype(str)
df
##########################################
df.describe()
df
#####################################
#Add column and row labels to the DataFrame
column_names=["UrbanPop","Assault","Murder"]
row_label=["a","b"]
df=pd.DataFrame(columns=column_names,index=row_label)
df
###################################################
df.describe()
df
#####################################
df.info
df
##############################################
#select certain row and assign it to another dataframe
df2=df[5:]  #select  row from 5 to all
df2
########################################
#acessing certain  cell from column 'duration'

df['Murder'][2]
##################################
#Drop row by label
df1=df.drop([1,2])
df1
#Delete row by position/index
df1=df.drop(df.index[1])
df1
#multiple index 
df1=df.drop(df.index[[1,2]])
df1
#delete rows by index range
df1=df.drop(df.index[2:])#delete 0 and 1 row
df1
###################################
######when you have default index for rows
df1=df.drop(0)
df1
################

df1=df.drop([0,3])#it will delete row0 and row3
df1
###########################################
df1=df.drop(range(0,2))#it will delete 0 and 1
df1
#################################################
#drop column by name
df2=df.drop(["Rape"],axis=1)
print(df2)
###########
#Explicitly using parameter by 'label'
df2=df.drop(labels=["Murder"],axis=1)
print(df2)
###############################################
#alternatively you can also use column instead of label
df2=df.drop(columns=["UrbanPop"],axis=1)
print(df2)
###########################################
#drop column by index
print(df.drop(df.columns[1],axis=1))
df
#####################################################
#using inplace=True
df.drop(df.columns[2],axis=1,inplace=True) #drop column  index 2
print(df)
#############################
#drop two or more column by label name
df2=df.drop(["UrbanPop","Murder"],axis=1)
print(df2)
###########################################
#drop columns from list of columns
lisCol=["Murder","Assault"]
df2=df.drop(lisCol,axis=1)
print(df2)
#############################################
df2=df.iloc[:,0:2]#this lines uses the slicing operator to get dataframe
df2
###################################################
df2=df.iloc[0:2,:]
df2
#slicing specifies rows and columns using iloc
df3=df.iloc[1:2,1:3]
df3
######################################################
df3=df.iloc[:,1:3]
df3
################################################
df2=df.iloc[[2,3,4]]#select row by index
df2
df2=df.iloc[1:5]#select row by integer index
df2
df2=df.iloc[:1]#select first row

df2=df.iloc[:3]#select first 3 row
df2=df.iloc[-1:]#select last row
df2=df.iloc[-3:]#select last 3 row
df2=df.iloc[::2]#select alternate rows
df2
##################################################
#select row by index
df2=df.loc[30]#select row by indexmeans selecting rows
df2
df2=df.loc[[5,8,12]]#select 45,78,90
df2
df2=df.loc[46:50]#select row by label
df2=df.loc[5:9:2]#select alternate row
############################
#select multiple column
df2=df.loc[:,["Assault","Murder","UrbanPop"]]
#select random column
df2=df.loc[:,["Murder","Assault","UrbanPop"]]
#select columns between two column
df2=df.loc[:,"Assault":"UrbanPop"]
df2
#select column by range
df2=df.loc[:,'UrbanPop']
#select all column by range
df2=df.loc[::,'Assault']
df2