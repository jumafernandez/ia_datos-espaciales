# -*- coding: utf-8 -*-
"""
Created on Sat May  6 11:26:43 2023

@author: Juan
"""

# -*- coding: utf-8 -*-

# Módulos para los requests
from bs4 import BeautifulSoup
import requests
# Módulo para trabajar con df
import pandas as pd
# Módulos para randomizar los requests
import time
import random

# Se inicializan las estructuras de datos
item_dict = {}
df_info = pd.DataFrame()


# Se van a tomar los primeros 2000 artículos
start = 1
while start < 2000:

    # Se preparan los headers y la url request
    headers = {'User-Agent':'Mozilla/6.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    url = f'https://scholar.google.es/scholar?start={start}&q=ciudad+de+luj%C3%A1n&hl=es&as_sdt=0'
    # Se hace el request y se formatea
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content,'lxml')

    for item in soup.select('[data-lid]'): 
        try: 
            print('----------------------------------------')
            print(item.select('h3')[0].get_text())
            
            item_dict = {'titulo': item.select('h3')[0].get_text(),
                         'enlace': item.select('a')[0]['href'],
                         'previa_texto': item.select('.gs_rs')[0].get_text()}
            
            df_info = df_info.append(item_dict, ignore_index=True)
        
        except Exception as e: 
            #raise e 
            print(e)
    
    # Se pasan a los siguientes 10 resultados (Scholar muestra 10 p/página)
    start+=10
    
    # Hago una pausa con intervalo random (1"-100")
    N_seconds = random.randint(10, 100)
    print(f'\nEl modelo esperará {N_seconds} segundos.\n')
    
    time.sleep(N_seconds)
