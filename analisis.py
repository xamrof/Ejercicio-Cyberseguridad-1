# Script para generar hash md5

import hashlib
import os

hash_para_analizar = [
    {"hash": "90965b0eb20e68b7d0b59accd2a3b4fd", "name": "copia.sh"},
    {"hash": "0b29406e348cd5f17c2fd7b47b1012f9", "name": "log.txt"},
    {"hash": "6d5e43a730490d75968279b6adbd79ec", "name": "pass.txt"},
    {"hash": "129ea0c67567301df1e1088c9069b946", "name": "plan-A.txt"},
    {"hash": "4e9878b1c28daf4305f17af5537f062a", "name": "plan-B.txt"},
    {"hash": "66bb9ec43660194bc066bd8b4d35b151", "name": "script.py"}
]

def obtener_archivos_carpeta(carpeta):
    archivos = []
    for ruta, carpetas, archivos_carpeta in os.walk(carpeta):
        for archivo in archivos_carpeta:
            archivos.append({ "name": archivo, "path": os.path.join(ruta, archivo)})
    return archivos

def calcular_md5sum(ruta_archivo, tamano_bloque=65536):
    md5 = hashlib.md5()
    try:
        with open(ruta_archivo, 'rb') as archivo:
            for bloque in iter(lambda: archivo.read(tamano_bloque), b''):
                md5.update(bloque)
        return md5.hexdigest()
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no se encontró.")
        return None
    except Exception as e:
        print(f"Error al calcular el hash MD5: {e}")
        return None

if __name__ == '__main__':
    ruta_carpeta  = input("Ingrese la ruta de la carpeta: ")
    archivos = obtener_archivos_carpeta(ruta_carpeta)
    print(archivos)
    for archivo in archivos:
        ruta_archivo = archivo["path"]
        nombre_archivo = archivo["name"]
        hash_md5 = calcular_md5sum(ruta_archivo)
        if hash_md5:
            for hash_analizar in hash_para_analizar:
                if hash_analizar["name"] == nombre_archivo:
                    if hash_analizar["hash"] == hash_md5:
                        print(f"El hash MD5 del archivo '{nombre_archivo}' es correcto.")
                    else:
                        print(f"El hash MD5 del archivo '{nombre_archivo}' es incorrecto. el archivo fue alterado")
                    break
    
            # print(f"El hash MD5 del archivo '{nombre_archivo}' es: {hash_md5} ")