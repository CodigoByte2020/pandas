import pandas as pd

# THE DATAFRAMES MUST HAVER SAME INDEXES
# ALL DATAFRAMES MUST BE OF THE SAME LENGTH

# CONCATENATION OF DATAFRAMES THROUGH ROWS
df_one = pd.DataFrame({
    'NOMBRE': ['Jose', 'Max'],
    'CARRERA': ['Economía', 'Arquitectura'],
    'EDAD': [23, 26]
}).set_index(keys='NOMBRE')

df_two = pd.DataFrame({
    'NOMBRE': ['Aurora', 'María'],
    'CARRERA': ['Medicina', 'Informática'],
    'EDAD': [22, 28]
}).set_index(keys='NOMBRE')

df_three = pd.concat([df_one, df_two])

print(df_one)
print('*****************************')
print(df_two)
print('*****************************')
print(df_three)
print(sep='\n\n')

# CONCATENATION OF DATAFRAMES THROUGH COLUMNS
df_four = pd.DataFrame({
    'AUTOS': ['Nissan', 'Ford', 'Audi'],
    'COLOR': ['Blanco', 'Azul', 'Rojo']
}).set_index(keys='AUTOS')

df_five = pd.DataFrame({
    'AUTOS': ['Nissan', 'Ford', 'Audi'],
    'MODELO': [2018, 2020, 2022]
}).set_index(keys='AUTOS')

df_six = pd.concat([df_four, df_five], axis=1)

print(df_four)
print('*****************************')
print(df_five)
print('*****************************')
print(df_six)
