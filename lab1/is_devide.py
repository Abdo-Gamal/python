
def check_devide(number ):
    if number%3==0 and number%5==0:
        print("FizzBuzz")
    elif number%3==0:
        print("fizz")
    else:
        print("Buzz")


number=int(input("entuer number "))

check_devide(number)