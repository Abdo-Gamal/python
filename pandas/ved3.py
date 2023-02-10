import pandas as pd
import numpy as np
# from pandas import *

w=pd.Series({'a':1,'b':2,'c':3,'d':4,'e':5})
x=pd.Series({'a':2,'b':3,'c':3,'d':4,'e':5})
y=pd.Series({'a':3,'b':4,'c':7,'d':4,'e':5})


grad=pd.DataFrame({"math":w,'pythics':x,'franch':y})

########################################
# print(grad.loc[grad.math>3]) 

# print(grad.loc[grad.math>3,['math','pythics']]) 

# print(grad.columns) 
# print(grad.index) 


# print(grad.sort_values(['math',],ascending=True)) 
# print(grad.sort_values(['math',],ascending=False)) 
# print(grad.max()) 
# print(grad.min()) 
# print(grad.mean()) 
# print(grad.std()) 

# print(grad['math'].max()) 
# print(grad['math'].min()) 
# print(grad['math'].mean()) 
# print(grad['math'].std()) 


# df=pd.DataFrame(np.random.rand(5,3),columns=['a','b','c'])


# print(df)
# print(df.corr())


df=pd.DataFrame(np.random.rand(5,3),columns=['a','b','c'])
# print(df)
d=pd.DataFrame({"a":1,"b":2},{"a":4,"b":5},{"a":9,"b":4})
print(d)


