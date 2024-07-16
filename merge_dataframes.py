import pandas as pd

# MERGE DATAFRAMES
# ALL DATAFRAMES MUST BE OF THE SAME LENGTH

df_cars_one = pd.DataFrame({
    'AUTOS': ['Nissan', 'Ford', 'Audi'],
    'COLOR': ['Blanco', 'Azul', 'Rojo']
})

df_cars_two = pd.DataFrame({
    'AUTOS': ['Toyota', 'Ford', 'Audi'],
    'MODELO': [2018, 2020, 2022]
})

df_merge_cars = pd.merge(df_cars_one, df_cars_two, on='AUTOS', how='inner')

print(df_merge_cars)
