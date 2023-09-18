# -*- coding: utf-8 -*-
"""
Created on Sat May  6 11:26:43 2023

@author: Juan
"""

# Módulo propio que genera funciones para el scraping
from funciones_scraping import descargar_pdfs

# Módulos para los requests
from bs4 import BeautifulSoup
import requests

# Módulo para trabajar con df
import pandas as pd

# Módulos para randomizar los requests
import time
import random

# Importo el parser para encodear el query
import urllib.parse

# Se inicializan las estructuras de datos
item_dict = {}
data_list = []

# Parámetros del bot
CANTIDAD_RESULTADOS = 20 # Cantidad de resultados generales buscados
query = 'Luján' # Concepto de búsqueda
query_encoding = urllib.parse.quote(query) # Encoding del query
directorio_destino = "data/papers_pdf" # Directorio donde se guardaran los PDFs


# Se van a tomar los primeros CANTIDAD_RESULTADOS artículos que esten en pdf
pagina_google = 1

# Se inicializan contadores
start = 1
resultados_pdf = 0

while start < CANTIDAD_RESULTADOS:

    # Se preparan los headers y la url request "ambiente"
    headers = {'User-Agent':'Mozilla/6.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    url = f'https://scholar.google.es/scholar?start={start}&q={query_encoding}&hl=es&as_sdt=0'
    
    # Se muestra el número de página y se incrementa en 1
    print(f'\nResultados de la página {pagina_google} que poseen paper en PDF: ')
    pagina_google+=1

    # Se hace el request y se formatea
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content,'html.parser')
    
    for item in soup.select('[data-lid]'): 

        try: 
            item_dict = {'titulo': item.select('h3')[0].get_text(),
                         'enlace': item.select('a')[0]['href'],
                         'previa_texto': item.select('.gs_rs')[0].get_text()}
           
            # Verifico si está el paper en pdf
            if "[PDF]" in item_dict['titulo']:
                
                # Si es así lo muestro
                print('----------------------------------------')
                print(item.select('h3')[0].get_text())
                
                # Si es un pdf además se agrega el diccionario a la lista
                data_list.append(item_dict)
                
                # Se incrementa el contador de resultados positivos
                resultados_pdf+=1

        except Exception as e: 
            #raise e 
            print(e)
    
    # Se pasan a los siguientes 10 resultados (Scholar muestra 10 p/página)
    start+=10
    
    if start < CANTIDAD_RESULTADOS:
        # Hago una pausa con intervalo random ("3-20")
        N_seconds = random.randint(3, 20)
        print(f'\nEl modelo esperará {N_seconds} segundos.\n')
    
        time.sleep(N_seconds)
        
# Se realiza un resumen:
print('\n----------------------------------------\n')
print(f'Query realizado: {query}.')
print(f'Cantidad de páginas de Google recorridas: {pagina_google}.')
print(f'Cantidad de artículos relevantes en PDF encontrados: {resultados_pdf}.')
print(f'Cantidad de artículos relevantes totales pedidos/encontrados: {CANTIDAD_RESULTADOS}/{start}.')

# Convertir la lista de diccionarios en un DataFrame
df_info = pd.DataFrame(data_list)

# Se guardan en un xlsx y un csv
df_info.to_excel('resultados-excel.xlsx')
df_info.to_csv('resultados-csv.csv')

# Una vez procesados los resultados se descargan los pdf
urls_pdf = df_info['enlace']

# Llamar a la función para descargar los PDFs
descargar_pdfs(urls_pdf, directorio_destino, query)


