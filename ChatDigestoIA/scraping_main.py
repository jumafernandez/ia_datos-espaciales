import os
nueva_carpeta = 'C:/Users/jumaf/Documents/GitHub/ChatDigestoIA'
os.chdir(nueva_carpeta)

import random
import time
from funciones import descargar_pdf, encontrar_proximo_id_a_descargar
from config import URL_MODELO_PDF, CARPETA_DESTINO, TIEMPO_ALEATORIO

proximo_id_a_descargar = encontrar_proximo_id_a_descargar(CARPETA_DESTINO)
print(f'El próximo id de PDF a descargar es {proximo_id_a_descargar}.')

# Itera sobre los IDs desde el último documento descargado + 1 hasta 100000
# El último ID se verifica con el número de la última resolución
# del último boletín publicado en el Digesto
for id_pdf in range(proximo_id_a_descargar, 135000):
    # Llama a la función para descargar el PDF
    descargar_pdf(URL_MODELO_PDF, id_pdf, CARPETA_DESTINO)
    
    # Agrega un tiempo aleatorio entre 1 y 5 segundos
    if TIEMPO_ALEATORIO:
        tiempo_aleatorio = random.randint(1, 5)
        print(f'El scraper esperará {tiempo_aleatorio}" antes del próximo GET.')
        time.sleep(tiempo_aleatorio)

