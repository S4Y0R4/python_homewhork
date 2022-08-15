def IMT(weight: float, growth: float) -> float:
    imt = weight / (growth / 100 * growth / 100)
    if imt < 16:
        print("Great lack of weight")
    elif imt < 18.5:
        print("Underweight")
    elif imt < 24:
        print("Underweight")
    elif imt < 30:
        print("Overweight (preobesity)")
    elif imt < 35:
        print("Obesity I degree")
    elif imt < 40:
        print("Obesity II degree")
    else:
        return print("Obesity III degree")


weight = float(input("Your weight in kg: "))
growth = float(input("Your growth in sm: "))
IMT(weight, growth)


def test_IMT():
    assert IMT(64, 178) == "Underweight"
