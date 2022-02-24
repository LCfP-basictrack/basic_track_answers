beatles = ["John", "Paul", "Ringo", "George"]

stones = list()
stones.append("Mick")
stones.append("Charlie")
stones.append("Ronnie")
stones.append("Keith")

for beatle in beatles:
    print(beatle)

for _ in range(2):
    print("Programming is great!")


for index, beatle in enumerate(reversed(beatles)):
    pass
