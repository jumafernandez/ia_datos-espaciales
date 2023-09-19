# -*- coding: utf-8 -*-

# Módulos propios que generan funciones para el scraping
from funciones_scraping import descargar_pdfs
# from proxy_functions import fetch_proxies_freeproxy, fetch_proxies_sslproxies, get_valid_proxies
from funciones_text import pdf_to_text
from config import CANTIDAD_RESULTADOS, QUERY, DIRECTORIO_DESTINO

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

query_encoding = urllib.parse.quote(QUERY) # Encoding del query

# Se inicializan los proxys libres que se hacen para no ser banneados en el request
# proxies_list_ssl = fetch_proxies_sslproxies(30)
# proxies_list_freeproxies = fetch_proxies_freeproxy(30)
# proxies_validos = get_valid_proxies(proxies_list_ssl)
# proxies_validos.extend(get_valid_proxies(proxies_list_freeproxies))

# Se inicializan contadores y estructuras de datos
start = 1
resultados_pdf = 0
pagina_google = 1
item_dict = {}
data_list = []

while start < CANTIDAD_RESULTADOS:

    # Se preparan los headers y la url request "ambiente"
    headers = {'User-Agent':'Mozilla/6.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    url = f'https://scholar.google.es/scholar?start={start}&q={query_encoding}&hl=es&as_sdt=0'
    
    # Se muestra el número de página y se incrementa en 1
    print(f'\nResultados de la página {pagina_google} que poseen paper en PDF: ')
    pagina_google+=1

    # Elegir aleatoriamente un proxy de la lista
    # proxy_elegido = random.choice(proxies_validos)

    # Se hace el request y se formatea
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content,'html.parser')
    
    for item in soup.select('[data-lid]'): 

        try: 
            
            item_dict = {'titulo': item.select('h3')[0].get_text(),
                         'autor/origen':  item.select('.gs_a')[0].get_text(),
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
print(f'Query realizado: {QUERY}.')
print(f'Cantidad de páginas de Google recorridas: {pagina_google}.')
print(f'Cantidad de artículos relevantes en PDF encontrados: {resultados_pdf}.')
print(f'Cantidad de artículos relevantes totales pedidos/encontrados: {CANTIDAD_RESULTADOS}/{start}.')

# Convertir la lista de diccionarios en un DataFrame
df_info = pd.DataFrame(data_list)

# Una vez procesados los resultados se descargan los pdf
urls_pdf = df_info['enlace']

# Llamar a la función para descargar los PDFs
directorio_generado = descargar_pdfs(urls_pdf, DIRECTORIO_DESTINO, QUERY)

# Ahora paso a txt el texto de los archivos pdf descargados
pdf_to_text(directorio_generado)

# Se guardan en un xlsx y un csv
df_info.to_excel(f'{directorio_generado}/resultados-excel.xlsx')
df_info.to_csv(f'{directorio_generado}/resultados-csv.csv')