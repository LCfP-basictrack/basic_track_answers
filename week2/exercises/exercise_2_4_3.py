def leap_year(year):
    return (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0


print(leap_year(1900))
print(leap_year(1999))
print(leap_year(2000))
print(leap_year(2004))
