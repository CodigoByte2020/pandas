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
# print('*******************************************')
# dataframe_two = dataframe_two.drop(index=[0, 1])
# print(dataframe_two)

# FILTER ROWS OF A DATAFRAME
print(dataframe_two[(dataframe_two['AGE'] >= 18) & (dataframe_two['GENDER'] == 'M')])
print(dataframe_two[(dataframe_two['NAME'].apply(lambda x: len(str(x)) >= 7)) & (dataframe_two['GENDER'] == 'M')])

print(dataframe_two.sort_values(['NAME'], key=lambda x: x.str.len()))  # x ---> It's a pandas series
# print(dataframe_two.sort_values(['NAME'], key=lambda x: len(str(x))))  # ---> ERROR


def convert_to_str(series):
    return pd.Series([(len(str(x))) for x in series])


print(dataframe_two.sort_values(['NAME'], key=lambda series: convert_to_str(series)))
# print(dataframe_two.sort_values(['NAME'], key=lambda series: pd.Series([(len(str(x))) for x in series])))
