import pandas as pd

numbers_serie = pd.Series([0, 2, 4, 6, 8])
fruits_serie = pd.Series({'apples': 10, 'cherrys': 8, 'bananas': 4})

# print(numbers_serie)
# print(fruits_serie)
#
# PROPERTIES MORE COMMONS
# print(numbers_serie.size)  # ---> Total of elements
# print(numbers_serie.index)  # ---> Indexs
# print(numbers_serie.dtype)  # ---> Type of data stored

# METHODS MORE COMMMONS
print(numbers_serie.sum())
print(numbers_serie.min())
print(numbers_serie.max())
print(numbers_serie.describe())  # ---> General description of the serie

# ACCESSING TO THE SERIES
# print(numbers_serie[0])  # ---> Accediendo a una serie
# print(numbers_serie[:2])  # ---> Accediendo a una serie, a partir de 2 elementos es una serie
# print(fruits_serie['apples'])  # ---> Accediendo a una serie
# print(fruits_serie[['apples', 'cherrys']])  # ---> Accediendo a una serie
