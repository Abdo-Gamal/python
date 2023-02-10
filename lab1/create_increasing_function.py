# start=int(input("enter st "))
# length=int(input("enter len "))
# mylist=[]
#
# for i in range(start,start+length):
#     mylist.append(i)
#
# print(mylist)

def fun(start,length):
    mylist = []
    for i in range(start, start + length):
        mylist.append(i)
    return  mylist

print(fun(5,3))






