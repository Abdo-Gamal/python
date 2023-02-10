
mylist=[]
def inter_array_element(len):
    for i in range(len):
        num = int(input(f"enter {i + 1} for list "))
        mylist.append(num)

def sort_array_element(mylist,len):
    for i,v in enumerate(mylist):
        j=i+1
        while j<len:
            if mylist[i]>=mylist[j]:
                temp=mylist[i]
                mylist[i]=mylist[j]
                mylist[j]=temp
            j+=1


#                                              enter array element
inter_array_element(5)
print("\n")
print(mylist)
print("\n")

#                                                first away

sort_array_element(mylist,5)
print(mylist)
#                                                second away
# sorted_mylist=mylist[:]
# sorted_mylist.sort()
# print(sorted_mylist)
# print("\n")
# sorted_mylist.reverse()
# print(sorted_mylist)
# print("\n")