
from modules.temperatura_db import temperatura_db
import datetime
import random

db = temperatura_db()
#VARIABLES A CONFIGURAR

fecha_inicial = datetime.date(2023, 8, 1)
num_dias_a_generar = 15
#Esto es simplemente con el fin de probar el algoritmo en si, normalmente se guardaria la fecha y su temperatura con el metodo correspondiente
temperaturas_a_guardar = [round(random.uniform(15.0, 35.0), 1) for _ in range(num_dias_a_generar)] #Genero una temperatura random entre 15 y 35 para las pruebas

# --- PRUEBAS ---

print("--- 1. Guardando Temperaturas Secuenciales ---")
for i in range(num_dias_a_generar):
    fecha_actual = fecha_inicial + datetime.timedelta(days=i)
    fecha_str = fecha_actual.strftime("%d/%m/%Y")
    temperatura = temperaturas_a_guardar[i]
    db.guardar_temperatura(temperatura, fecha_str)
print("-" * 30)


print("\n--- 2. Devolviendo Temperaturas Específicas ---")
# Seleccionamos algunas fechas que sabemos que existen
fecha_test1 = (fecha_inicial + datetime.timedelta(days=3)).strftime("%d/%m/%Y")
fecha_test2 = (fecha_inicial + datetime.timedelta(days=10)).strftime("%d/%m/%Y")
fecha_no_existente = "01/01/2000"

temp1 = db.devolver_temperatura(fecha_test1)
print(f"Temperatura para {fecha_test1}: {temp1}°C" if temp1 is not None else f"No se encontró temperatura para {fecha_test1}")

temp2 = db.devolver_temperatura(fecha_test2)
print(f"Temperatura para {fecha_test2}: {temp2}°C" if temp2 is not None else f"No se encontró temperatura para {fecha_test2}")

temp_no_existente = db.devolver_temperatura(fecha_no_existente)
print(f"Temperatura para {fecha_no_existente}: {temp_no_existente}°C" if temp_no_existente is not None else f"No se encontró temperatura para {fecha_no_existente}")
print("-" * 30)


print("\n--- 3. Temperaturas en Rango ---")
# Definimos un rango dentro de nuestras fechas generadas
rango_fecha_inicio = (fecha_inicial + datetime.timedelta(days=2)).strftime("%d/%m/%Y")
rango_fecha_fin = (fecha_inicial + datetime.timedelta(days=8)).strftime("%d/%m/%Y")

max_rango = db.max_temp_rango(rango_fecha_inicio, rango_fecha_fin)
print(f"Temperatura máxima en rango [{rango_fecha_inicio} - {rango_fecha_fin}]: {max_rango}°C" if max_rango is not None else "No hay datos en el rango.")

min_rango = db.min_temp_rango(rango_fecha_inicio, rango_fecha_fin)
print(f"Temperatura mínima en rango [{rango_fecha_inicio} - {rango_fecha_fin}]: {min_rango}°C" if min_rango is not None else "No hay datos en el rango.")

min_ext, max_ext = db.temp_extremos_rango(rango_fecha_inicio, rango_fecha_fin)
if min_ext is not None and max_ext is not None:
    print(f"Extremos (min, max) en rango [{rango_fecha_inicio} - {rango_fecha_fin}]: ({min_ext}°C, {max_ext}°C)")
else:
    print(f"No hay datos suficientes para extremos en el rango [{rango_fecha_inicio} - {rango_fecha_fin}].")
print("-" * 30)


print("\n--- 4. Devolver Listado de Temperaturas en Rango ---")
print(f"Temperaturas entre {rango_fecha_inicio} y {rango_fecha_fin} (ordenadas):")
lista_temps1 = db.devolver_temperaturas(rango_fecha_inicio, rango_fecha_fin)
if lista_temps1:
    for item in lista_temps1:
        print(item)
print("-" * 30)


print("\n--- 5. Cantidad de Muestras ---")
total_muestras_antes_borrado = db.cantidad_muestras()
print(f"Cantidad total de muestras antes del borrado: {total_muestras_antes_borrado}")
print("-" * 30)


print("\n--- 6. Borrando Temperaturas ---")
# Borramos una fecha del medio del rango
fecha_a_borrar = (fecha_inicial + datetime.timedelta(days=7)).strftime("%d/%m/%Y")
print(f"Intentando borrar temperatura de la fecha: {fecha_a_borrar}")
resultado_borrado = db.borrar_temperatura(fecha_a_borrar)
print(f"Resultado del borrado: {'Exitoso' if resultado_borrado else 'Fallido o no encontrado'}")

temp_despues_borrar = db.devolver_temperatura(fecha_a_borrar)
print(f"Verificación: Temperatura para {fecha_a_borrar} después del borrado: {temp_despues_borrar}°C" if temp_despues_borrar is not None else f"Verificación: No se encontró temperatura para {fecha_a_borrar} (borrado correcto).")
print("-" * 30)


print("\n--- 7. Cantidad de Muestras Después del Borrado ---")
total_muestras_despues_borrado = db.cantidad_muestras()
print(f"Cantidad total de muestras después del borrado: {total_muestras_despues_borrado}")

if total_muestras_antes_borrado - 1 == total_muestras_despues_borrado:
    print("Verificación de cantidad de muestras: Correcto.")
else:
    print("Verificación de cantidad de muestras: Incorrecto.")
print("-" * 30)


print("\n--- 8. Prueba de Guardar Temperatura Duplicada (Actualización) ---")
# Elegimos una fecha para actualizar
fecha_duplicada = (fecha_inicial + datetime.timedelta(days=5)).strftime("%d/%m/%Y")
temp_original = db.devolver_temperatura(fecha_duplicada)
print(f"Temperatura original para {fecha_duplicada}: {temp_original}°C")

db.guardar_temperatura(99.9, fecha_duplicada) # Actualizamos con una nueva temperatura
temp_actualizada = db.devolver_temperatura(fecha_duplicada)
print(f"Temperatura actualizada para {fecha_duplicada}: {temp_actualizada}°C")

if temp_actualizada == 99.9:
    print("Verificación de actualización: Correcto.")
else:
    print("Verificación de actualización: Incorrecto.")
print("-" * 30)

print("\nFIN DE LAS PRUEBAS")