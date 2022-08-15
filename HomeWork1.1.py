cost = input("How much is a kilo of potatoes? ")
print(f"Result = {float(cost) * 5}")

cost = input("How much is a kilo of potatoes? ")
count = input("How much do you want to buy? ")
print(f"Resul =  {round(float(cost) * float(count), 2)} ")

b_cost = 2.3
p_cost = 1.5
b_count = input("How many kilograms of bananas do you want to buy? ")
p_count = input("How many kilograms of potatoes do you want to buy? ")
if (float(b_count) * float(b_cost)) > (float(p_count) * float(p_cost)):
    print("You have to pay more for bananas")
else:
    print("You have to pay more for potato")
print(f"Result = {round(float(b_count) * float(b_cost) + float(p_count) * float(p_cost), 2)}")