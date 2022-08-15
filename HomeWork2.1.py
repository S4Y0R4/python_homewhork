import random
def nums(first_num, second_num):
    sum = first_num + second_num
    while True:
        answer = int(input(f"How much will {first_num} + {second_num}: "))
        if answer == sum:
            print("Success!")
            break
    return 0


first_num = random.randint(0, 99)
second_num = random.randint(0, 99)
answer = 0
nums(first_num, second_num)
