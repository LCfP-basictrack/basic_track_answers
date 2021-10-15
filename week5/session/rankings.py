import pandas as pd

pd.set_option("max_columns", 8)

restaurants = pd.read_csv("groningenRestaurants.csv")
rankings = pd.read_excel("rankingsRaw.xlsx")

rankings['restaurant'] = rankings['name']
del(rankings['name'])

restaurant_rankings = restaurants.merge(rankings, how="inner", on="restaurant")

# print(rankings.head(5))
# print(restaurants.head(5))
print(restaurant_rankings.head(5))
