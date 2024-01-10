# Script para generar hash md5

import hashlib
import os
import json

with open("hash_para_analizar.json", "r") as archivo:
    hash_para_analizar = json.load(archivo)


def obtener_archivos_carpeta(carpeta):
    archivos = []
    for ruta, carpetas, archivos_carpeta in os.walk(carpeta):
        for archivo in archivos_carpeta:
            archivos.append({ "name": archivo, "path": os.path.join(ruta, archivo)})
    return archivos

def calcular_md5sum(ruta_archivo):
    try:
        with open(ruta_archivo, 'rb') as archivo:
            md5 = hashlib.md5(archivo.read()).hexdigest()    
        return md5
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no se encontró.")
        return None
    except Exception as e:
        print(f"Error al calcular el hash MD5: {e}")
        return None

if __name__ == '__main__':
    ruta_carpeta  = input("Ingrese la ruta de la carpeta: ")
    archivos = obtener_archivos_carpeta(ruta_carpeta)
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
                    