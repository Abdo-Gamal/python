
name=input("enter string ")
# cnt=name.count("iti")
# print(cnt)
#second away

cnt2=0
for i,v in enumerate(name):
    if i+2==len(name) :break
    str=name[i]+name[i+1]+name[i+2]
    if str=="iti":
        cnt2+=1

print(cnt2)