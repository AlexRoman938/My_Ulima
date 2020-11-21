# Líbrerias a usar

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


#Datos ( Ingresos anuales y Score Gastos )
#Se usa numpy para crear un array con los datos

data = np.array([[15,39] , [15,81] , [16,6] , [16,77] , [17,40] , [17,76] , 
                [18,6] , [18,94] , [19,3] , [19,72] , [19,14] , [19,99] ,
                [20,15] , [20,77] , [20,13] , [20,79] , [21,35] , [21,66], 
                [23,29] , [23,98]])


# ## Cargar a un dataframe con pandas

data_df = pd.DataFrame(data , columns=['Ingresos Anuales' , 'Score Gasto'])
data_df


#Aplicando K MEANS con sklearn

clustering = KMeans(n_clusters=3 , max_iter=300) #Usando K Means de la libreria sklearn
clustering.fit(data_df)

centroids = clustering.cluster_centers_  #Método sirve para encontrar la  coordenada de los  centroides


#Gráfica con matplotlib sobre los puntos y los centroides 
#Los puntos Rojos son los centroides
#Los demás puntos , sin incluir los rojos , algunos son de igual color , esto significa que pertenecen a la misma agrupación

plt.scatter(data_df['Ingresos Anuales' ] , data_df['Score Gasto'] , c= clustering.labels_.astype(float) , s=50 , alpha = 0.5 )
plt.scatter(centroids[:,0] , centroids[:,1] , c = 'red' , s = 50 )
plt.title('Clustering K MEANS')
plt.xlabel('Ingresos Anuales')
plt.ylabel('Score Gasto')
plt.show()


#  Tabla Agregando a que centroide pertenece cada punto
data_df['Centroide'] = clustering.labels_
print(data_df)





