import pandas as pd

# Ruta del archivo CSV original
original_file_path = 'C:/Users/smero/OneDrive/Documentos/repos/Cuidador-de-plantas/tabla_datos.csv'

# Lee el archivo CSV original, ignorando líneas problemáticas
df = pd.read_csv(original_file_path, on_bad_lines='warn')

# Muestra las primeras filas del DataFrame para verificar que se haya cargado correctamente
print("Contenido del DataFrame:")
print(df.head())

# Verifica si los nombres de las columnas están correctamente alineados
df.columns = df.columns.str.strip()  # Elimina posibles espacios en blanco de los nombres de columnas

# Divide el DataFrame en diferentes tablas según las columnas
nombres_df = df[['nombre']].copy()  # Copia del DataFrame con solo la columna 'nombre'
cuidados_df = df[['cuidado']].copy()  # Copia del DataFrame con solo la columna 'cuidado'
estaciones_df = df[['estación']].copy()  # Copia del DataFrame con solo la columna 'estación'
riego_df = df[['riego']].copy()  # Copia del DataFrame con solo la columna 'riego'
sol_directo_df = df[['sol_directo']].copy()  # Copia del DataFrame con solo la columna 'sol_directo'
humedad_df = df[['humedad']].copy()  # Copia del DataFrame con solo la columna 'humedad'
poda_df = df[['poda']].copy()  # Copia del DataFrame con solo la columna 'poda'
abono_df = df[['abono']].copy()  # Copia del DataFrame con solo la columna 'abono'
imagen_df = df[['enlace_a_imagen']].copy()  # Copia del DataFrame con solo la columna 'enlace_a_imagen'

# Guardar los DataFrames en archivos CSV separados
nombres_df.to_csv(r'C:\Users\smero\OneDrive\Documentos\repos\Cuidador-de-plantas\nombres.csv', index=False)
cuidados_df.to_csv(r'C:\Users\smero\OneDrive\Documentos\repos\Cuidador-de-plantas\cuidados.csv', index=False)
estaciones_df.to_csv(r'C:\Users\smero\OneDrive\Documentos\repos\Cuidador-de-plantas\estaciones.csv', index=False)
riego_df.to_csv(r'C:\Users\smero\OneDrive\Documentos\repos\Cuidador-de-plantas\riego.csv', index=False)
sol_directo_df.to_csv(r'C:\Users\smero\OneDrive\Documentos\repos\Cuidador-de-plantas\sol_directo.csv', index=False)
humedad_df.to_csv(r'C:\Users\smero\OneDrive\Documentos\repos\Cuidador-de-plantas\humedad.csv', index=False)
poda_df.to_csv(r'C:\Users\smero\OneDrive\Documentos\repos\Cuidador-de-plantas\poda.csv', index=False)
abono_df.to_csv(r'C:\Users\smero\OneDrive\Documentos\repos\Cuidador-de-plantas\abono.csv', index=False)
imagen_df.to_csv(r'C:\Users\smero\OneDrive\Documentos\repos\Cuidador-de-plantas\imagen.csv', index=False)

print("Archivos CSV separados han sido creados.")
