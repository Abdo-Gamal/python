#/////////////////////////////////////////////////////////lamda
check_division=lambda num:num%3==0

# print(check_division(3))
#/////////////////////////////////////////////////////////filter

my_list=[1,2,3,4,5,6,8,9]
# for i in filter(check_division,my_list):
#     print(i,end=", ")
#/////////////////////////////////////////////////////////map
output=map(lambda num:num**2,my_list)

# print(list(output))
#///////////////////////////////////////////////////////// list comprhntion

my_output=[]
for i in my_list :
    if i%2==0:
        my_output.append(i**2)

#//equlivent

my_output=[i**2 for i in my_list if i%2==0]
print(my_output)
#///////////////////////////////////////////////////////// dic comprhntion

my_output_dic={ i:i**2 for i in my_list if i % 2==0}
print(my_output_dic)


