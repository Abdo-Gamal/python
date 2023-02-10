import pandas as pd
# from pandas import *


# my_list=[
#     [1,2,3],
#     [2,5,2],
#      [1,2,3]
# ]

# my_list2=[
#     [1,2,3],[1,2,3],
#     [2,5,2], [1,2,3],
#     [2,5,2],[1,2,3]
# ]
# clum=['one', 'two', 'three']
# indx=['a', 'b', 'c', 'd','e', 'f']
# # df=pd.DataFrame(my_list,columns=clum)
# # df=pd.DataFrame(my_list2,columns=clum)
# df=pd.DataFrame(my_list2,index=indx,columns=clum)
# print(df)


########################################
w=pd.Series({'a':1,'b':2,'c':3,'d':4,'e':5})
x=pd.Series({'a':2,'b':3,'c':3,'d':4,'e':5})
y=pd.Series({'a':3,'b':4,'c':7,'d':4,'e':5})


grad=pd.DataFrame({"math":w,'pythics':x,'franch':y})
# print(grad)
# print(grad["math"])

# print(grad["math"].describe())
# print(grad["math"].head(2))
# print(grad["math"].tail(2))

# print(grad.T)
# print(grad.keys())
# print(grad.values)


# print('math' in grad.keys())
# print('Math' in grad.keys())
# print(1 in grad.values)
# print( 2 in grad.values)

# print(grad.iloc[0:2,]) 
# print(grad.iloc[0:2,0:1]) 
print(grad.loc['a':'b',]) 
print(grad.loc['a':'c',"math":]) 





