import pandas as pd


original_file_path = 'C:/Users/smero/OneDrive/Documentos/repos/Cuidador-de-plantas/tabla_datos.csv'

# IGNORA líneas problemáticas
df = pd.read_csv(original_file_path, on_bad_lines='warn')


print("Contenido del DataFrame:")
print(df.head())


df.columns = df.columns.str.strip()  
# Elimina posibles espacios en blanco de los nombres de columnas

# Divide el DataFrame en diferentes tablas según las columnas
nombres_df = df[['nombre']].copy()  # EJEMPLO Copia del DataFrame con solo la columna 'nombre'
cuidados_df = df[['cuidado']].copy()  
estaciones_df = df[['estación']].copy()  
riego_df = df[['riego']].copy()  
sol_directo_df = df[['sol_directo']].copy()  
humedad_df = df[['humedad']].copy()  
poda_df = df[['poda']].copy()  
abono_df = df[['abono']].copy()  
imagen_df = df[['enlace_a_imagen']].copy()  

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
