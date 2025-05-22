from temperatura_db import temperatura_db
import datetime


db = temperatura_db()

#Insertamos un dato
fecha = "07/08/2002"
fecha2 = "07/08/2003"
db.guardar_temperatura(24.3,fecha)
db.guardar_temperatura(30.3,fecha2)

#Buscamos 
temperatura_buscada = db.devolver_temperatura(fecha)
temperatura_buscada2 = db.devolver_temperatura(fecha2)
print (temperatura_buscada)
print (temperatura_buscada2)
