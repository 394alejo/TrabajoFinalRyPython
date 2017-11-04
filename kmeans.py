#Carga de las librerias necesarias
import pandas as pd
import numpy as np
import os
from sklearn.cluster import KMeans


#Selección del directorio de trabajo
os.chdir('/media/agch2/Juana/Asignaturas_2017-2/Programacion_y_Analisis_Cuantitativo_en_R/R/Trabajo_Final-Paquete')

#Carga del archivo en un dataframe
df = pd.read_table("datos.csv",sep=",")

#Selección de variables independientes y dependiente (la última no es usada para calibrar el modelo sino solo para ver que tal pronostica, ya que es un algoritmo no supervisado)
indep=df.iloc[:,range(10)]
depend=np.array(df.loc[:,"class"], dtype=int)

#Ajuste del modelo:
kmeans = KMeans(n_clusters=3, random_state=0).fit(indep)
kmeans.labels_
kmeans.cluster_centers_
kmeans_predict=kmeans.predict(indep)
kmeans_predict

kmeans_predict[kmeans_predict==2]=[3]
kmeans_predict[kmeans_predict==0]=[4]
kmeans_predict[kmeans_predict==1]=[5]
kmeans_predict=kmeans_predict-2
kmeans_predict

#Rendimiento del modelo:
rend_Km=np.mean(depend==kmeans_predict)
rend_Km

#Conversion a json
df=pd.DataFrame(df).to_json(orient='split')
indep=pd.DataFrame(indep).to_json(orient='split')
depend=pd.DataFrame(depend).to_json(orient='split')
kmeans_predict=pd.DataFrame(kmeans_predict).to_json(orient='split')

