from temperatura_db import temperatura_db
import datetime


db = temperatura_db()

#Insertamos un dato
fecha = "07/08/2002"
fecha2 = "07/08/2009"
db.guardar_temperatura(24.3,"22/08/2002")
db.guardar_temperatura(30.3,"07/08/2002")
db.guardar_temperatura(24.3,"03/08/2002")
db.guardar_temperatura(30.3,"04/08/2002")
db.guardar_temperatura(40.3,"07/08/2009")
db.guardar_temperatura(12.3,"17/08/2007")
db.guardar_temperatura(27.3,"07/08/2006")
db.guardar_temperatura(35.3,"27/08/2005")
db.guardar_temperatura(23.3,"07/08/2004")
db.guardar_temperatura(13.3,"07/09/2003")

#Buscamos 
temperatura_buscada = db.devolver_temperatura(fecha)
temperatura_buscada2 = db.devolver_temperatura(fecha2)
print (temperatura_buscada)
print (temperatura_buscada2)


print ("La temperatura maxima")
temperatura_max = db.max_temp_rango(fecha, fecha2)
print (temperatura_max)

print ("La temperatura minima:")
temperatura_min = db.min_temp_rango(fecha, fecha2)
print(temperatura_min)

print ("La temperatura maxima y minima")
temperatua_maxima,temperatura_minima = db.temp_extremos_rango(fecha,fecha2)
print (temperatua_maxima)
print(temperatura_minima)

#Probamos eliminar
print (db.borrar_temperatura(fecha2))
temperatura_max = db.max_temp_rango(fecha, fecha2)
print("La nueva temperatura maxima es:")
print (temperatura_max)
