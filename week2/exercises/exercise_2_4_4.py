
def chinese_zodiac(year):
    index_in_zodiac = year % 12
    if index_in_zodiac == 0:
        return "monkey"
    elif index_in_zodiac == 1:
        return "rooster"
    elif index_in_zodiac == 2:
        return "dog"
    elif index_in_zodiac == 3:
        return "pig"
    elif index_in_zodiac == 4:
        return "rat"
    elif index_in_zodiac == 5:
        return "ox"
    elif index_in_zodiac == 6:
        return "tiger"
    elif index_in_zodiac == 7:
        return "rabbit"
    elif index_in_zodiac == 8:
        return "dragon"
    elif index_in_zodiac == 9:
        return "snake"
    elif index_in_zodiac == 10:
        return "horse"
    else:
        return "sheep"


print(chinese_zodiac(1900))
print(chinese_zodiac(1963))
print(chinese_zodiac(1988))
