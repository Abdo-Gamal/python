
#key must be string or any imutable type
my_deic={

    "abdo":"4",
    "ahmed":3,
    "saad":4.4,
}
my_deic2={

    "abdo":"4",
    "ahmed":3,
    "email":["bgmai@gmail.com"],
    "adress":{
        "street":1,
        "city":"assuit",
    }
}
#access dictionary

# print(my_deic2["abdo"])
# print(my_deic2["email"][0])
# print(my_deic2["adress"]["city"])

#loop on dictionary

# for key in my_deic2:
#     print(my_deic2[key])
#
# for key in my_deic2.keys():
#     print(my_deic2[key])

# for val in my_deic2.values():
#     print(val)
# for key,val in my_deic2.items():
#     print(key,val)


# search in  directory
#
# if "abdo1" in my_deic:
#     print("found")

# if  3 in my_deic.values():
#     print("found")

#return value if exist and return none if not exist
# print(my_deic.get("abdo"))


#add and update item in  dectionary

my_deic.update(
    {"tt":"ss","rr":4}
)
my_deic["abdo"]="4"
print(my_deic["tt"])
print(my_deic["abdo"])