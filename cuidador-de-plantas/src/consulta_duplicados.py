import pandas as pd

df = pd.read_csv('C:/Users/smero/OneDrive/Documentos/repos/Cuidador-de-plantas/tabla_datos.csv')

duplicated_count = df.duplicated(subset=['nombre']).sum()
print(f'Número de registros duplicados: {duplicated_count}')

# Aqui se carga el archivo "tabla_datos.csv para ver si hay duplicados"+