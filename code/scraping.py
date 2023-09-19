# -*- coding: utf-8 -*-

# Módulos propios que generan funciones para el scraping
from funciones_scraping import descargar_pdfs, scraping
from funciones_text import pdf_to_text
from config import CANTIDAD_RESULTADOS, QUERY, DIRECTORIO_DESTINO
# from proxy_functions import fetch_proxies_freeproxy, fetch_proxies_sslproxies, get_valid_proxies

# Se inicializan los proxys libres que se hacen para no ser banneados en el request
# proxies_list_ssl = fetch_proxies_sslproxies(30)
# proxies_list_freeproxies = fetch_proxies_freeproxy(30)
# proxies_validos = get_valid_proxies(proxies_list_ssl)
# proxies_validos.extend(get_valid_proxies(proxies_list_freeproxies))

data, resultados, paginas_recorridas = scraping(QUERY, CANTIDAD_RESULTADOS)

# Se realiza un resumen:
print('\n----------------------------------------\n')
print(f'Query realizado: {QUERY}.')
print(f'Cantidad de páginas de Google recorridas: {paginas_recorridas}.')
print(f'Cantidad de artículos relevantes en PDF encontrados: {len(data)}.')
print(f'Cantidad de artículos relevantes totales pedidos/encontrados: {CANTIDAD_RESULTADOS}/{resultados}.')


# Una vez procesados los resultados se descargan los pdf
urls_pdf = data['enlace']

# Llamar a la función para descargar los PDFs
directorio_generado = descargar_pdfs(urls_pdf, DIRECTORIO_DESTINO, QUERY)

# Ahora paso a txt el texto de los archivos pdf descargados
pdf_to_text(directorio_generado)

# Se guardan en un xlsx y un csv
data.to_excel(f'{directorio_generado}/resultados-excel.xlsx')
data.to_csv(f'{directorio_generado}/resultados-csv.csv')