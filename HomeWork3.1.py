import math

def stopy_na_metry(ft):
    meters = ft * 0.3048
    return round(meters, 3)


def maximum(num1, num2):
    if num1 > num2:
        print(num1)
    else:
        return num2


def mean(num1, num2):
    return (num1 + num2) / 2


def area_circle(r):
    return math.pi * (r ** 2)


def bmi(growth, weight):
    return (weight ** 2) / (growth ** 2)


def area_triangle(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return s


def km(kms):
    return kms * 0.621371


def m(ms):
    return ms / 0.621371
