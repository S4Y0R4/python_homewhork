def get_day_number(day_of_week, duration):
    assert duration > 0, "duration should be positive number"
    assert day_of_week > 0 and day_of_week < 8, "day_of_week can be only from 1 to 7"
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_number = (day_of_week + duration) % 7
    return days[day_number - 1]


day_of_week = int(input("Day of week: "))
duration = int(input("Duration of repair: "))
print(get_day_number(day_of_week, duration))
