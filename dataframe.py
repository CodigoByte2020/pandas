import pandas as pd

indexes = [11, 12, 13]
# DATAFRAME FROM LIST OF LISTS
df_one = pd.DataFrame(data=[['language', 10], ['history', 15], ['education', 12]], columns=['course', 'nota'],
                      index=indexes)
# print(df_one)

# DATAFRAME FROM DICTIONARIES
df_two = pd.DataFrame(data={'course': ['language', 'history', 'education'], 'nota': [10, 15, 12]}, index=indexes)
# print(df_two)

# DATASET: CONJUNTO DE DATOS ESTRUCTURADOS Y TABULADOS
df_csv = pd.read_csv('modalidad_virtual.csv')
# print(df_csv['time'])
# print(df_csv['time'][18])  # WE ACCESS TO A ELEMENT FROM IT COLUMN AND INDEX

print(df_csv['edad'] > 45)  # EVALUATE EACH ROW WITH THE CONDITION
print(df_csv['edad'][df_csv['edad'] > 45])  # APPLY THE CONDITION TO EACH ROW

filter_method = df_csv['edad'] > 45
print(df_csv[filter_method])  # APPLY THE CONDITION TO EACH ROW

print(df_csv.head(3))  # FIRST THREE RECORDS
print(df_csv.tail(3))  # LAST THREE RECORDS
