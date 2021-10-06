def leap_year(year):
    return (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0


leap_years = [year for year in range(1900, 2001) if leap_year(year)]

leap_years_alt = []
for year in range(1900, 2001):
    if leap_year(year):
        leap_years_alt.append(year)

for year in reversed(leap_years):
    print(year)
