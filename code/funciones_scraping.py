# -*- coding: utf-8 -*-

from datetime import datetime
import os
from bs4 import BeautifulSoup # Módulos para los requests
import requests # Módulos para los requests
import pandas as pd # Módulo para trabajar con df
import time # Módulos para randomizar los requests
import random # Módulos para randomizar los requests
import urllib.parse # Importo el parser para encodear el query

import fake_useragent

def get_user_agents(cantidad):
    """
    Devuelve una lista de user_agents random
    Args:
        cantidad: Cantidad de user_agents a generar
    Returns:
        Lista de user_agents
    """

    user_agents = []
    for i in range(cantidad):
        user_agent = fake_useragent.UserAgent().random
        user_agents.append(user_agent)

    return user_agents


def scraping(query_user, resultados_pedidos, offset_resultados_pedidos=1, proxies=None):
    """
    Esta función es la que realiza el scraping
    Parameters
    ----------
    query_user : str
        Query con el que se generan los resultados
    resultados_pedidos : int
        Cantidad de resultados solicitados
    proxies : list
        Proxies válidos para las solicitudes requests.

    Returns
    -------
    df_info : dataframe
        dataframe con los pdfs encontrados y algunos datos
    resultados_relevantes : int
        Cantidad de resultados encontrados (sin discriminar pdf)
    paginas_google : int
        Cantidad de páginas encontradas

    """
    # Se inicializan contadores y estructuras de datos
    start = offset_resultados_pedidos
    resultados_pdf = 0
    resultados_relevantes = 0
    paginas_google = 1
    item_dict = {}
    data_list = []
    
    query_encoding = urllib.parse.quote(query_user) # Encoding del query
    
    # La cantidad de resultados pedidos se conforma finalmente con la cantidad de
    # resultados + el offset (numero a partir del que empieza a guardar)
    resultados_pedidos = resultados_pedidos + offset_resultados_pedidos
    
    while start < resultados_pedidos:
    
        # Se preparan los headers y la url request
        # Genero una lista de user agents aleatorios por página (c/página tiene 10 resultados)
        useragent_list = get_user_agents(1+(resultados_pedidos//10))
        # Se toma un user agent por página
        useragent_random = useragent_list[paginas_google-1]
        headers = {'User-Agent':useragent_random}
        url = f'https://scholar.google.es/scholar?start={start}&q={query_encoding}&hl=es&as_sdt=0'
        
        # Se muestra el número de página y se incrementa en 1
        print(f'\nResultados de la página {paginas_google} que poseen paper en PDF: ')
        paginas_google+=1
    
        # Elegir aleatoriamente un proxy de la lista
        # proxy_elegido = random.choice(proxies)
    
        # Se hace el request y se formatea
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content,'html.parser')
        
        for item in soup.select('[data-lid]'): 
    
            try: 
                
                item_dict = {'titulo': item.select('h3')[0].get_text(),
                             'autor/origen':  item.select('.gs_a')[0].get_text(),
                             'enlace': item.select('a')[0]['href'],
                             'previa_texto': item.select('.gs_rs')[0].get_text()}
     
                resultados_relevantes+=1
                
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
        
        if start < resultados_pedidos:
            # Hago una pausa con intervalo random ("3-20")
            N_seconds = random.randint(3, 20)
            print(f'\nEl modelo esperará {N_seconds} segundos.\n')
        
            time.sleep(N_seconds)
        
        # Convertir la lista de diccionarios en un DataFrame
        df_info = pd.DataFrame(data_list)
        
    return df_info, resultados_relevantes, paginas_google



def fecha_hora_actual_str():
    """
    Se genera la fecha y hora actual en un str para incorporar como nombre de archivo/directorio

    Returns
    -------
    fecha_hora_str : str
    """

    # Obtén la fecha y hora actual
    fecha_hora_actual = datetime.now()
    
    # Formatea la fecha y hora en una cadena de texto
    fecha_hora_str = fecha_hora_actual.strftime("%Y%m%d-%H%M%S")
    
    # Retorna la fecha y hora actual en formato de cadena
    return fecha_hora_str



def descargar_pdfs(urls, directorio, query_busqueda):
    """
    Se descargan los pdf de los resultados del scraping

    Parameters
    ----------
    urls : list
        Lista de urls de pdfs
    directorio : str
        String donde se generará el directorio en el que guardan los pdfs
    query_busqueda : str
        query utilizado en la búsqueda de resultados

    Returns
    -------
    directorio_busqueda : str
        Directorio donde se guardaron los pdfs

    """

    # Crear el directorio de destino si no existe
    if not os.path.exists(directorio):
        os.makedirs(directorio)

    directorio_busqueda = f'{directorio}/{fecha_hora_actual_str()}-{query_busqueda}'
    os.makedirs(directorio_busqueda)
    
    numero_resultado = 0
    for url in urls:
        try:
            # Obtener el nombre del archivo desde la URL
            nombre_archivo = f'resultado_{numero_resultado}.pdf'
            numero_resultado += 1

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
        except Exception as e:
            print(f"Error al descargar el archivo desde '{url}': {str(e)}")
            
    return directorio_busqueda
