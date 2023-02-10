import pandas as pd
import numpy as np
# from pandas import *

f=pd.read_csv("iris.csv")# f is dataframe
# print(f.head())  # head print firs 5 row 
# print(f.head(10))

f=pd.read_csv("iris.csv",index_col=0)#make clum 0  to be index  # f is dataframe
# print(f.head())

#                                                                    save in file 

w=pd.Series({'a':1,'b':2,'c':3,'d':4,'e':5})
x=pd.Series({'a':2,'b':3,'c':3,'d':4,'e':5})
y=pd.Series({'a':3,'b':4,'c':7,'d':4,'e':5})
grad=pd.DataFrame({"math":w,'pythics':x,'franch':y})
# print(grad)
grad.to_csv('3.csv')# will be create  file with names 2.csv and save Df in it 
# grad.to_excel('3.xlwt',sheet_name='sheet 1')# not work

#                                                                    read form csv and excle  in file 
# grad1=pd.read_csv("2.csv")
# # grad2=pd.read_excel("3.xls")
# print(grad1)
# # print(grad2)


grad1=pd.read_csv("2.csv",names=['a','b','c'])
print(grad1)

#stop in middle of vedio


