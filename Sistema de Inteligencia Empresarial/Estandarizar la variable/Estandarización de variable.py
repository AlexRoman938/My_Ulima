
#Importamos las librerias que usaremos para la estandarizacion de variables
import numpy as np
import pandas as pd


#Escribimos manualmente todos los datos en un array usando la libreria numpy
data = np.array([19,
21,
20,
23,
31,
22,
35,
23,
64,
30,
67,
35,
58,
24,
37,
22,
35,
20,
52,
35
])

#Una vez que los datos esten en el arreglo , usamos la libreria pandas para que esten en un DataFrame
data_df = pd.DataFrame(data , columns=['Edad'])

#Se usa la fórmula para estandarizar ( convertir en intervalos entre 0 y 1 ) y lo ponemos a otra nueva variable
#(Valor que se quiere estandarizar - Valor minimo del conjunto de datos) / (Valor máximo del conjunto de datos - Valor minimo del conjunto de datos)
data_estandarizada = (data_df - data_df.min()) / (data_df.max() - data_df.min())

#Imprimimos el dataframe con los valores estandarizados
print(data_estandarizada)


