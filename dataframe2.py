import pandas as pd

dataframe = pd.read_csv('modalidad_virtual.csv', sep=',')
# print(dataframe)

# I WILL ACCESS ALL ELEMENTS OF THE DATAFRAME

# 1. THROUGH POSITIONS
# print(dataframe.iloc[0, 0])
# print(dataframe.iloc[0, 1])
# print(dataframe.iloc[:2, 1:3])
# print(dataframe.iloc[:2, ::3])

# 2. THROUGH NAMES
# print(dataframe.loc[11, 'carrera'])
# print(dataframe.loc[[11, 12], ['time', 'carrera']])

# HE HAS ADDED COLUMNS A ONE DATAFRAME AND AFTER DELETE THEY
dataframe_two = pd.DataFrame(data={
    'NAME': ['Gianmarco', 'Danna', 'Miguel', 'Xiomara', 'Roxana'],
    'AGE': [10, 25, 18, 8, 21],
    'GENDER': ['M', 'F', 'M', 'F', 'F']
})
# dataframe_two['HOBBY'] = pd.Series(data=['soccer', 'basketball', 'soccer', 'tennis', 'box'])
# print(dataframe_two)
#
# dataframe_two.pop(item='HOBBY')
# print(dataframe_two)

# ROWS
new_rows = pd.DataFrame(data={
    'NAME': ['Carlos', 'Roberto'],
    'AGE': [7, 31],
    'GENDER': ['M', 'M']
})

dataframe_two = pd.concat(objs=[dataframe_two, new_rows], ignore_index=True)
print(dataframe_two)

dataframe_two = dataframe_two.drop(index=[0, 1])
print(dataframe_two)

# FILTER ROWS OF A DATAFRAME
pass
