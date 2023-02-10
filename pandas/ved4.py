import pandas as pd
import numpy as np
# from pandas import *

w=pd.Series({'a':1,'b':2,'c':3,'d':4,'e':5})
x=pd.Series({'a':2,'b':3,'c':3,'d':4,'e':5})
y=pd.Series({'a':3,'b':4,'c':7,'d':4,'e':5})


# grad=pd.DataFrame({"math":w,'pythics':x,'franch':y})
# grad["total"]=(grad['math']+grad["pythics"]+grad["franch"])/100
# print(grad)

# df=pd.DataFrame(np.random.rand(5,3),columns=['a','b','c'])
# print(df)
# q=df.query("a<.5 and  b<.5 ")
# q2=df[(df.a<.5)&(df.b<.5)]
# print(q2)

def make_df(col,ind):
    data={c:[c+str(i) for i in ind] for c in col}
    return pd.DataFrame(data,ind)

print(make_df("abd",range(3)))
