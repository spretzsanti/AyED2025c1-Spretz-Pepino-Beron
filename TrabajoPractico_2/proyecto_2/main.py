# main.py
from modules.temperatura_db import temperatura_db
import datetime

# --- PRUEBAS ---
db = temperatura_db()

print("--- Guardando Temperaturas ---")
db.guardar_temperatura(24.3, "22/08/2002")
db.guardar_temperatura(30.3, "07/08/2002")
db.guardar_temperatura(24.3, "03/08/2002") # Fecha más antigua
db.guardar_temperatura(30.3, "04/08/2002")
db.guardar_temperatura(40.3, "07/08/2009") # Fecha más reciente
db.guardar_temperatura(12.3, "17/08/2007")
db.guardar_temperatura(27.3, "07/08/2006")
db.guardar_temperatura(35.3, "27/08/2005")
db.guardar_temperatura(23.3, "07/08/2004")
db.guardar_temperatura(13.3, "07/09/2003")
db.guardar_temperatura(25.0, "15/08/2002") # Otra fecha en el rango
print("-" * 30)

print("\n--- Devolviendo Temperaturas Específicas ---")
fecha_test1 = "07/08/2002"
fecha_test2 = "07/08/2009"
fecha_no_existente = "01/01/2000"

temp1 = db.devolver_temperatura(fecha_test1)
print(f"Temperatura para {fecha_test1}: {temp1}°C" if temp1 is not None else f"No se encontró temperatura para {fecha_test1}")

temp2 = db.devolver_temperatura(fecha_test2)
print(f"Temperatura para {fecha_test2}: {temp2}°C" if temp2 is not None else f"No se encontró temperatura para {fecha_test2}")

temp_no_existente = db.devolver_temperatura(fecha_no_existente)
print(f"Temperatura para {fecha_no_existente}: {temp_no_existente}°C" if temp_no_existente is not None else f"No se encontró temperatura para {fecha_no_existente}")
print("-" * 30)

print("\n--- Temperaturas en Rango ---")
rango_fecha_inicio = "01/08/2002" # Antes de la primera fecha guardada
rango_fecha_fin = "30/08/2007"   # Después de algunas fechas, antes de la última

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

print("\n--- Devolver Listado de Temperaturas en Rango (Nuevo Método) ---")
# Probamos con un rango que sabemos tiene datos
lista_temps1 = db.devolver_temperaturas(rango_fecha_inicio, rango_fecha_fin)
if lista_temps1:
    print(f"Temperaturas entre {rango_fecha_inicio} y {rango_fecha_fin} (ordenadas):")
    for item in lista_temps1:
        print(item)
else:
    print(f"No se encontraron temperaturas entre {rango_fecha_inicio} y {rango_fecha_fin}.")

# Probamos con un rango sin datos
lista_temps_vacia = db.devolver_temperaturas("01/01/1990", "31/12/1990")
if not lista_temps_vacia:
    print(f"\nCorrecto: No se encontraron temperaturas entre 01/01/1990 y 31/12/1990.")
print("-" * 30)

print("\n--- Cantidad de Muestras (Nuevo Método) ---")
total_muestras_antes_borrado = db.cantidad_muestras()
print(f"Cantidad total de muestras antes del borrado: {total_muestras_antes_borrado}")
print("-" * 30)

print("\n--- Borrando Temperaturas ---")
fecha_a_borrar = "07/08/2009" # Una fecha que existe
print(f"Intentando borrar temperatura de la fecha: {fecha_a_borrar}")
resultado_borrado = db.borrar_temperatura(fecha_a_borrar)
print(f"Resultado del borrado: {'Exitoso' if resultado_borrado else 'Fallido o no encontrado'}")

temp_despues_borrar = db.devolver_temperatura(fecha_a_borrar)
print(f"Verificación: Temperatura para {fecha_a_borrar} después del borrado: {temp_despues_borrar}°C" if temp_despues_borrar is not None else f"Verificación: No se encontró temperatura para {fecha_a_borrar} (borrado correcto).")

fecha_no_existente_borrar = "10/10/2020" # Una fecha que no existe
print(f"\nIntentando borrar temperatura de la fecha: {fecha_no_existente_borrar}")
resultado_borrado_no_existente = db.borrar_temperatura(fecha_no_existente_borrar)
print(f"Resultado del borrado (fecha no existente): {'Exitoso (no debería, o indica no encontrado)' if resultado_borrado_no_existente else 'Fallido o no encontrado (correcto)'}")
print("-" * 30)

print("\n--- Cantidad de Muestras Después del Borrado ---")
total_muestras_despues_borrado = db.cantidad_muestras()
print(f"Cantidad total de muestras después del borrado: {total_muestras_despues_borrado}")

if total_muestras_antes_borrado is not None and total_muestras_despues_borrado is not None and resultado_borrado:
     if total_muestras_antes_borrado - 1 == total_muestras_despues_borrado:
        print("Verificación de cantidad de muestras: Correcto.")
     else:
        print("Verificación de cantidad de muestras: Incorrecto.")
print("-" * 30)

print("\n--- Prueba de Guardar Temperatura Duplicada (Actualización) ---")
fecha_duplicada = "22/08/2002"
temp_original = db.devolver_temperatura(fecha_duplicada)
print(f"Temperatura original para {fecha_duplicada}: {temp_original}°C")
db.guardar_temperatura(99.9, fecha_duplicada) # Actualizar
temp_actualizada = db.devolver_temperatura(fecha_duplicada)
print(f"Temperatura actualizada para {fecha_duplicada}: {temp_actualizada}°C")
if temp_actualizada == 99.9:
    print("Verificación de actualización: Correcto.")
else:
    print("Verificación de actualización: Incorrecto.")
print("-" * 30)

print("\n--- Pruebas Adicionales de Rangos ---")
# Rango que incluye el primer y último elemento
todas_las_fechas_guardadas = db.devolver_temperaturas("01/01/2000", "31/12/2030")
print(f"Todas las {len(todas_las_fechas_guardadas)} temperaturas guardadas (ordenadas):")
for item in todas_las_fechas_guardadas:
    print(item)

# Comparar con cantidad de muestras
if len(todas_las_fechas_guardadas) == db.cantidad_muestras():
    print("Verificación: devolver_temperaturas con rango amplio coincide con cantidad_muestras.")
else:
    print("Error: devolver_temperaturas con rango amplio NO coincide con cantidad_muestras.")
print("-" * 30)

print("\nFIN DE LAS PRUEBAS")