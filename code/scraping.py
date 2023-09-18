# -*- coding: utf-8 -*-
"""
Created on Sat May  6 11:26:43 2023

@author: Juan
"""

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
CANTIDAD_RESULTADOS = 20
query = 'Medio ambiente'
query_encoding = urllib.parse.quote(query)

# Se van a tomar los primeros CANTIDAD_RESULTADOS artículos que esten en pdf
pagina_google = 1
start = 1
while start < CANTIDAD_RESULTADOS:

    # Se preparan los headers y la url request "ambiente"
    headers = {'User-Agent':'Mozilla/6.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    url = f'https://scholar.google.es/scholar?start={start}&q={query_encoding}&hl=es&as_sdt=0'
    
    # Se muestra el número de página y se incrementa en 1
    print(f'Resultados de la página {pagina_google} que poseen paper en PDF: \n')
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

# Convertir la lista de diccionarios en un DataFrame
df_info = pd.DataFrame(data_list)
df_info.to_excel('resultados.xlsx')
