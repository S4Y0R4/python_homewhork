def calculation_of_products(product_name: str, product_count: float, product_price: float) -> float:
    total = product_price * product_count
    print(f"You will pay {round(total, 2)} pln for {product_name}, which you want to buy! ")
    return 0


product_name = input("What do you want to buy? ").lower()
product_count = float(input("Ok, and how much you want to buy? "))
product_price = float(input("How much does it costs? "))
calculation_of_products(product_name, product_count, product_price)
