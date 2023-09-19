# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:33:11 2023

@author: jumaf
"""

import pdfplumber
import os
import re
from unidecode import unidecode  # Importa la función unidecode

def clean_text(text):
    """
    Realiza una limpieza básica del texto preservando caracteres acentuados.

    Args:
        text (str): El texto a limpiar.

    Returns:
        str: El texto limpio.
    """
    # Convierte caracteres a Unicode sin acentos
    cleaned_text = unidecode(text)
    
    # Elimina caracteres especiales y espacios adicionales
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', cleaned_text)
    cleaned_text = ' '.join(cleaned_text.split())  # Elimina espacios adicionales

    return cleaned_text

def pdf_to_text(pdf_directory):
    """
    Convierte archivos PDF en archivos de texto (TXT) en el directorio especificado.

    Args:
        pdf_directory (str): La ruta al directorio que contiene los archivos PDF.
    """
    # Verifica si el directorio existe
    if not os.path.exists(pdf_directory):
        print(f"El directorio '{pdf_directory}' no existe.")
        return

    # Itera a través de los archivos PDF en el directorio
    for filename in os.listdir(pdf_directory):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_directory, filename)

            # Abre el archivo PDF
            pdf_file = pdfplumber.open(pdf_path)

            # Lee el contenido del PDF
            pdf_text = ''
            for page in pdf_file.pages:
                pdf_text += page.extract_text()

            # Cierra el archivo PDF
            pdf_file.close()

            # Realiza la limpieza del texto
            cleaned_text = clean_text(pdf_text)

            # Genera un archivo de texto (TXT) con el contenido limpio del PDF
            txt_filename = os.path.splitext(filename)[0] + '.txt'
            txt_path = os.path.join(pdf_directory, txt_filename)

            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(cleaned_text)

            print(f'Se ha creado {txt_filename} con el contenido limpio del PDF en {pdf_directory}.')

    print('Proceso completado.')

