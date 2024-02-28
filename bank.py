# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 15:59:14 2023

@author: hp
"""

import pandas as pd
import numpy as np
df=pd.read_csv("bank_data.csv")
df

df.shape
#(45211, 32)
##########
df.size
df
#1446752
################
df.columns
#it will start with index
####################

df.columns.values  #it will  start with array
df
###################
df.index
df
#RangeIndex(start=0, stop=45211, step=1)
######################
df.dtypes
########################
df['age']
####################
df[['age','balance']]
############################
#select certain rows
df2=df[6:]
df2
###################
#Acessing certain value from column duration
df['duration'][760]
#Substracting value  from column
df['balance']=df['balance']-600
df['balance']
#convert datatypes
df1=df.convert_dtypes()
df1.dtypes

#change all olumn in same type
df=df.astype(str)
print(df.dtypes)
#change type for one or multiple column
df=df.astype({"age":int,"balance":float})
print(df.dtypes)
############################################

#convert data type all column in list
cols=['age','balance']
df[cols]=df[cols].astype('float')
df.dtypes
##################################################
#ignore error
df=df.astype({"balance":float},errors='ignore')
df.dtypes

####################################################
#rename  the column
df.columns=['age','balance','loan']
df
df2=df.rename({'age':'C1','loan':'C2','balance':'C4'},axis=1)
df2
#####################################################
#generate error
df=df.dtype({"course":int},errors='raise')
df
#######################
#convert feed column to numeric type
df=df.astype(str)
df
#it will show 5 number summary
df.describe()
df
#####################################
#Add column and row labels to the DataFrame
column_names=["loan","age","balance"]
row_label=["a","b"]
df=pd.DataFrame(columns=column_names,index=row_label)
df
###################################################
#it show all table
df.info
df
##############################################
#select certain row and assign it to another dataframe
df2=df[5:]  #select  row from 5 to all
df2
########################################
#acessing certain  cell from column 'duration'

df['duration'][2]
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
#when you have default index for rows
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
df2=df.drop(["campaign"],axis=1)
print(df2)
###########
#Explicitly using parameter by 'label'
df2=df.drop(labels=["pdays"],axis=1)
print(df2)
###############################################
#alternatively you can also use column instead of label
df2=df.drop(columns=["default"],axis=1)
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
df2=df.drop(["poutfailure","poutother"],axis=1)
print(df2)
###########################################
#drop columns from list of columns
lisCol=["poutsuccess","poutunknown"]
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
df2=df.loc[30]#select row by index means selecting rows
df2
df2=df.loc[[45,78,90]]#select 45,78,90
df2
df2=df.loc[67:56]#select row by label
df2=df.loc[58:9:2]#select alternate row
############################
#select multiple column
df2=df.loc[:,["age","default","balance"]]
#select random column
df2=df.loc[:,["con_cellular","con_telephone","con_unknown"]]
#select columns between two column
df2=df.loc[:,"default":"balance"]
df2
#select column by range
df2=df.loc[:,'default']
#select all column by range
df2=df.loc[:,:,'duration']
df2