# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 16:35:09 2023

@author: jumaf
"""

from datetime import datetime

def fecha_hora_actual_str():
    # Obtén la fecha y hora actual
    fecha_hora_actual = datetime.now()
    
    # Formatea la fecha y hora en una cadena de texto
    fecha_hora_str = fecha_hora_actual.strftime("%Y%m%d-%H%M%S")
    
    # Retorna la fecha y hora actual en formato de cadena
    return fecha_hora_str

import os
import requests

def descargar_pdfs(urls, directorio, query_busqueda):

    # Crear el directorio de destino si no existe
    if not os.path.exists(directorio):
        os.makedirs(directorio)

    directorio_busqueda = f'{directorio}/{fecha_hora_actual_str()}-{query_busqueda}'
    os.makedirs(directorio_busqueda)
    
    numero_resultado = 0
    for url in urls:
        # Obtener el nombre del archivo desde la URL
        nombre_archivo = f'resultado_{numero_resultado}.pdf'
        numero_resultado+=1

        # Realizar la solicitud HTTP para descargar el PDF
        response = requests.get(url)

        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Guardar el contenido del PDF en un archivo local
            with open(f'{directorio_busqueda}/{nombre_archivo}', 'wb') as file:
                file.write(response.content)
            print(f"El archivo '{nombre_archivo}' se ha descargado con éxito.")
        else:
            print(f"No se pudo descargar el archivo '{nombre_archivo}'. Código de estado: {response.status_code}")
            
    return directorio_busqueda
