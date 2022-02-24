import pandas as pd
import statistics


f1_dictionary = {
    "year": [1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959],
    "champ": ["Farina", "Fangio", "Ascari", "Ascari", "Fangio", "Fangio", "Fangio", "Fangio", "Hawthorne", "Brabham"],
    "wins": [3, 3, 6, 5, 6, 4, 3, 4, 1, 2],
    "points": [30, 31, 36, 34, 42, 40, 30, 40, 42, 31]}

genders = ["m"] * 10
f1_dictionary["gender"] = genders

print("The Formula 1 Dictionary:\n", f1_dictionary)

f1_data_frame = pd.DataFrame(f1_dictionary, columns=f1_dictionary.keys())

team_wins = ["Alfa"] * 2 + ["Ferrari"] * 2 + ["Mercedes"] * 2 + ["Ferrari", "Maserati", "Ferrari", "Cooper"]
f1_data_frame['team'] = team_wins

print("The Formula 1 Data Frame:\n", f1_data_frame)
print(statistics.mean(f1_data_frame["points"]))
