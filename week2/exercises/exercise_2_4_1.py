def interest(principle, interest_rate, time):
    return round(principle * (1 + interest_rate) ** time, 2)


principle_amount = float(input("What is the initial amount in the account? "))
interest_per_year = float(input("What is the interest rate (in percent) per year ")) / 100.0
number_of_years = int(input("How many years will you not touch the account? "))

print(interest(principle_amount, interest_per_year, number_of_years))
