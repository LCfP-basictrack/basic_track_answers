beatles = ["John", "Paul", "Ringo", "George"]
instruments = ["Guitar", "Guitar", "Drums", "Bass"]

for beatle, whatever in zip(beatles, instruments):
    print(beatle, "plays", whatever)

for index, beatle in enumerate(beatles):
    print(index, beatle, instruments[index])

for number in range(10, 20, 3):
    print(number)
