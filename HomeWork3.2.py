months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month = input().capitalize()

def count_of_days(month):
    if month == months[0] or month == months[2] or month == months[4] or month == months[6] or month == months[7] or month == months[9] or month == months[11]:
        print("31!")
    elif month == months[1]:
        year = int(input("Year? "))
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print("29!")
        else:
            print("28!")
    elif month == months[3] or month == months[5] or month == months[8] or month == months[10]:
        print("30!")
    else:
        return print("??")

count_of_days(month)
