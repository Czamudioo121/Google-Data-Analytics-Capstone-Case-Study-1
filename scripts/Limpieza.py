import pandas as pd
import glob
import os

# 1. Definir la ruta donde guardaste los 12 archivos CSV extraídos
ruta_carpeta = r'D:\Users\Administrador\Pictures\Caso de estudio 1\Data\Raw\CSV'
archivos_csv = glob.glob(os.path.join(ruta_carpeta, "*.csv"))

# 2. Leer y unificar todos los CSVs en un solo DataFrame
lista_dataframes = []
for archivo in archivos_csv:
    df_temp = pd.read_csv(archivo)
    lista_dataframes.append(df_temp)

df_unificado = pd.concat(lista_dataframes, ignore_index=True)

# Guardamos el conteo inicial
total_inicial = len(df_unificado)
print(f"--- REPORTE DE LIMPIEZA ---")
print(f"Total de datos iniciales (crudos): {total_inicial} filas")

# 3. Borrar cualquier fila que tenga al menos una celda en blanco (NaN/Null)
df_limpio = df_unificado.dropna().copy()

# 4. Asegurar que las columnas de fecha sean de tipo datetime
df_limpio['started_at'] = pd.to_datetime(df_limpio['started_at'])
df_limpio['ended_at'] = pd.to_datetime(df_limpio['ended_at'])

# 5. Calcular el tiempo de viaje (ride_length)
df_limpio['ride_length'] = df_limpio['ended_at'] - df_limpio['started_at']

# 6. Limitar a viajes que duren máximo 4 horas y que sean mayores a 0 minutos
# (Esto elimina errores donde la fecha de fin es anterior a la de inicio)
limite_superior = pd.Timedelta(hours=4)
limite_inferior = pd.Timedelta(minutes=0)

filtro_tiempo = (df_limpio['ride_length'] > limite_inferior) & (df_limpio['ride_length'] <= limite_superior)
df_limpio = df_limpio[filtro_tiempo]

# Guardamos el conteo final
total_final = len(df_limpio)
print(f"Total de datos finales (limpios): {total_final} filas")
print(f"Se eliminaron {total_inicial - total_final} filas (por celdas vacías o tiempos fuera de rango).")

# 7. Exportar el DataFrame limpio a un nuevo archivo CSV para la fase de análisis
ruta_salida = os.path.join(ruta_carpeta, 'cyclistic_datos_limpios.csv')
df_limpio.to_csv(ruta_salida, index=False)
print(f"¡Listo! Archivo limpio guardado en: {ruta_salida}")