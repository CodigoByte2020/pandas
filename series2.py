import pandas as pd

years = pd.Series([10, 15, 8, 25, 40, 21])
notes = pd.Series({'mathematics': 15, 'language': 13, 'history': 10})

# print(years[years > 20])  # ---> Filtering elements of a serie
# print(notes[notes > 11])

# print(years.sort_values(ascending=True))
# print(notes.sort_index(ascending=True))

# CREATING SERIES WITH DEFAULT VALUES AND INDEX
data = 20
index = [1, 2, 3, 4]
data_serie_one = pd.Series(data=data, index=index)
print(data_serie_one)

players = ['Lionel Messi', 'Luka Modric', 'Kilian Mbapé']
teams = ['Inter Miami', 'Real Madrid', 'PSG']
player_serie = pd.Series(data=players, index=teams)
print(player_serie)
