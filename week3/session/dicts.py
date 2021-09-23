capitals = {"The Netherlands": "Amsterdam", "France": "Paris"}

capitals["Japan"] = "Tokyo"

for country in reversed(sorted(capitals)):
    print(country, capitals[country])

fruit_basket = {"Apple": 3}

fruit_to_add = input("Which fruit to add? ")

fruit_basket[fruit_to_add] = fruit_basket.get(fruit_to_add, 0) + 1

print(fruit_basket)
