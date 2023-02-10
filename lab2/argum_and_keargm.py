# make  function take an known of argument

# def my_sum(*args):
#     print(args)
#     return
#
# my_sum(1,2,3,5,4,-1)

# def my_sum(x,*args):
#     print(args)
#     return
#
# my_sum(1,2,3,5,4,-1)

#name paramter

# def my_sum(x,y,z):
#     print(x)
#     print(y)
#     print(z)
#     return
#
# my_sum(y=1,z=2,x=3)


# unknown number of pramter name paramter
#
# def my_sum(x,y,**kwargs):
#     print(x)
#     print(y)
#     return
#
# my_sum(1,2,w=3,e=3,z=9,r=6)




# argum befor kwargs

def my_sum(x,y,*args ,**kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)
    return

my_sum(1,2,5,5,w=3,e=3,z=9,r=6)