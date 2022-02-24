capitals = {"The Netherlands": "Amsterdam", "France": " Paris"}
capitals["Japan"] = "Tokyo"

for country in capitals:
    print("The capital of {} is {}".format(country, capitals[country]))

# When we buy a fruit basket from AH it always comes with three apples
fruit_basket = {"Apple": 3}

fruit_to_add = input("What fruit would you like to add? ")
# if fruit_to_add in fruit_basket:
#     fruit_basket[fruit_to_add] += 1
# else:
#     fruit_basket[fruit_to_add] = 1

fruit_basket[fruit_to_add] = fruit_basket.get(fruit_to_add, 0) + 1

print(fruit_basket)
