from matplotlib import pyplot as plt
import numpy as np
#                                                       color 
# plt.style.use('bmh')
# plt.style.use('classic')
# plt.style.use('dark_background')
# plt.style.use('fivethirtyeight')

#                                                       Plot  
# yy=[1,5,6,8,9,10]
# plt.plot(yy)
# # plt.show()


# plt.style.use('classic')

# x=[1,5,6,8,9,10]
# y=[1,5,6,8,9,10]
# plt.plot(x,y)
# plt.show()

# x=np.linspace(0,10)
# y=np.sin(x)
# y2=np.cos(x)
# plt.plot(x,y)
# plt.plot(x,y2)
# plt.show()

#                                       label
a=(1,2,3,4,8)
b=(1,4,5,7,9)

# plt.xlabel("time")
# plt.ylabel("work")
# plt.plot(a,b)
# plt.show()
#                                            second away
# ax=plt.axes()
# ax.set_xlabel("time")
# ax.set_ylabel("work")
# plt.plot(a,b)
# plt.show()
#                                            third

# ax=plt.axes()
# ax.set(xlabel="time",ylabel="work" )
# plt.plot(a,b)
# plt.show()

#                                            marker

ax=plt.axes()
ax.set(xlabel="time",ylabel="work" )
plt.plot(a,b,marker='o')
plt.show()