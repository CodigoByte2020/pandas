import pandas as pd

# LA FORMA QUE YO PREFIERO PARA CONVERTIR ARCHIVOS ES, PRIMERO GUARDARLOS EN XLSX Y
# DESPUES GUARDAR COMO ARCHIVO CSV, ASI PUEDO TENER LOS DATOS SEPARADOS POR ","

file = pd.read_excel('op.area.course.xls')
file.to_csv('op.area.course.csv', index=False, header=True, sep=",")
