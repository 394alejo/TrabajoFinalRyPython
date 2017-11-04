Sys.setenv(PATH=paste("/home/agch2/anaconda3/bin/",
                      Sys.getenv("PATH"), sep=":"))
Sys.getenv("PATH")
system("python --version")
#install.packages("rPython",lib= "/home/agch2/R/x86_64-pc-linux-gnu-library/3.4", configure.vars= "RPYTHON_PYTHON_VERSION=3")


library(rPython)
library(jsonlite)

setwd("/media/agch2/Juana/Asignaturas_2017-2/Programacion_y_Analisis_Cuantitativo_en_R/R/Trabajo_Final-Paquete")
python.load("kmeans.py")

# Get the variable

df<- python.get("df")
indep<- python.get("indep")
depend<- python.get("depend")
kmeans_predict<- python.get("kmeans_predict")
rend_Km<- python.get("rend_Km")

df
indep
depend
kmeans_predict
rend_Km

df <- fromJSON(df)
indep <- fromJSON(indep)
depend <- fromJSON(depend)
kmeans_predict <- fromJSON(kmeans_predict)

df
indep
depend
kmeans_predict
rend_Km






