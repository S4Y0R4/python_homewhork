from random import randint

a = randint(0, 999)
i = 1000
while i != a:
    i = int(input("Ur num: "))
    if i == a:
        print("Congratulations!")
    else:
        if i > a:
            print("Your number is more than expected")
        else:
            print("Your number is less than expected")