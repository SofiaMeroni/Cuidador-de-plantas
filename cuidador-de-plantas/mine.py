import time
from .src import lista_plantas
from .src import crear_base, guardar_datos

def main():
    with open(r'C:\Users\Sofia\OneDrive\Escritorio\llave-api-plantas\api_llave.txt', 'r') as file:
        api_key = file.read().strip()
    url = 'https://trefle.io/api/v1/plants'  
    carpeta = 'base_de_datos'  

    
    crear_base(carpeta)

    while True:
        print("Obteniendo datos de plantas...")
        plantas = lista_plantas(api_key, url)
        
        if not plantas:
            print("No se encontraron más datos.")
            break
        
        print("Guardando datos en la base de datos...")
        guardar_datos(plantas, carpeta)
        
        print("Esperando 60 segundos para la próxima solicitud...")
        time.sleep(60)

if __name__ == "__main__":
    main()
