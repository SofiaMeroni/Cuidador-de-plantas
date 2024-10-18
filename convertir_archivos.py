import pandas as pd

# Cargar el archivo con codificación WIN1252 y manejar errores de decodificación
df = pd.read_csv('C:/Users/smero/OneDrive/Documentos/repos/Cuidador-de-plantas/nombres.csv', encoding='windows-1252', encoding_errors='ignore')

# Sobreescribir el archivo original con la nueva codificación UTF-8
df.to_csv('C:/Users/smero/OneDrive/Documentos/repos/Cuidador-de-plantas/nombres.csv', index=False, encoding='utf-8')
