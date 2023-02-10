def calculate_area(reduis):
    pi=2.14
    return reduis*reduis*pi

def calculate_circumference(reduis):
    pi=2.14
    return 2*reduis*pi

reduis=int(input("enter  reduis "))
print(f"my area {calculate_area(reduis)}\n")

print(f"my area {calculate_circumference(reduis)}\n")