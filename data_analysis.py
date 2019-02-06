
# #%%
# import matplotlib.pyplot as plt
# import matplotlib as mpl
import numpy as np
import pandas as pd

temperature_data = pd.read_csv('data.csv',names=["temperature"])

# Imprimir los datos
#print(temperature_data)

# Seleccionar una columna en particular
#print(temperature_data.temperature)
#print(temperature_data["temperature"])

# Imprimir los primeros y los ultimos registros de los datos 
#head = temperature_data.head()
#tail = temperature_data.tail()
#print(head)

# dtypes muestra el tipo de objeto y el tipo de datos de cada columna
#print(temperature_data.dtypes)

# describe muestra un breve resumen estadístico de los datos
#print(temperature_data.describe())

# Transponer los datos
#print(temperature_data.T)

# Cortes y "rebanar" los datos
#print(temperature_data[0:3])

# Boolean Indexing
#print(temperature_data[temperature_data.temperature > 22])

# Copiado , filtrado
""" copy = temperature_data.copy().head()
copy["texto"] = ["caliente" , "templado" , "frio" , "frozen" , "hot as hell" ]
print(copy)
print("--------------------------------------")
copy = copy[copy["texto"].isin(["templado","hot as hell"])]
print(copy) """

# Revisar si los datos tienen valores na
#are_data_na = pd.isna(temperature_data)
#print(are_data_na)

# Obtener la media de los datos
#media = temperature_data.mean()
#print(media)

# Contar las veces que aparece una temperatura (Tener en cuenta el concepto de Serie)
#count = temperature_data.T.iloc[0].value_counts()
#print(count)


# Graficar el conteo
#count.plot(kind="bar")