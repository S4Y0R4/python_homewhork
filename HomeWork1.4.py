def ticket_price_calculation(count: int) -> float:
    i = 1
    total = 0
    while i <= count:
        i += 1
        age = int(input("Age: "))
        if age <= 6:
            ticket_price = 0
        elif age <= 17:
            ticket_price = 2.28
        elif age <= 64:
            ticket_price = 3.8
        else:
            ticket_price = 1.9
        total += ticket_price
    print(f"Total price is {round(total, 2)} pln")
    return 0


count = int(input("How many tickets you want to buy? "))
ticket_price_calculation(count)


def test_ticket_price_calculation():
    assert ticket_price_calculation(0) == "Then why did you come?"
