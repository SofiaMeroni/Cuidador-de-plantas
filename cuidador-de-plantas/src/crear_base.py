import os
import sqlite3

def crear_base_de_datos(carpeta):
    if not os.path.exists(carpeta):
        os.makedirs(carpeta) 

    conn = sqlite3.connect(os.path.join(carpeta, 'plantas.db'))
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS plantas (
            id TEXT PRIMARY KEY,
            cuidados TEXT
        )
    ''')
    conn.commit()
    conn.close()

def guardar_datos(plantas, carpeta):
    conn = sqlite3.connect(os.path.join(carpeta, 'plantas.db'))
    cursor = conn.cursor()
    
    cursor.executemany('''
        INSERT OR IGNORE INTO plantas (id, cuidados)
        VALUES (?, ?)
    ''', plantas)
    
    conn.commit()
    conn.close()
