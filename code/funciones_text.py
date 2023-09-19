# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:33:11 2023

@author: jumaf
"""

import pdfplumber
import os
import re
from unidecode import unidecode  # Importa la función unidecode
import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer  # Agregar esta línea

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


def cargar_documentos_desde_directorio(directorio):
    """
    Carga los documentos TXT desde un directorio específico y los devuelve en una lista.

    Args:
    directorio (str): La ruta al directorio que contiene los archivos TXT.

    Returns:
    list: Una lista de cadenas de texto, donde cada cadena es el contenido de un archivo TXT.
    """
    documentos = []

    # Enumera los archivos en el directorio
    for archivo in os.listdir(directorio):
        if archivo.endswith(".txt"):
            # Lee el contenido del archivo y agrégalo a la lista de documentos
            with open(os.path.join(directorio, archivo), 'r', encoding='utf-8') as file:
                contenido = file.read()
                documentos.append(contenido)

    return documentos

def procesar_documentos(documentos, idioma='spanish'):
    """
    Procesa una lista de documentos de texto y genera indicadores por documento.

    Args:
    documentos (list): Una lista de cadenas de texto que representan los documentos.
    idioma (str): El idioma para las stopwords. Por defecto, 'spanish'.

    Returns:
    pd.DataFrame: Un DataFrame con los indicadores de cada documento o None si no se pudo procesar ningun documento.
    """
    indicadores = []

    for documento in documentos:
        # Verifica si el documento tiene contenido
        if documento.strip():
            # Vectorización de documentos utilizando CountVectorizer
            vectorizador = CountVectorizer(stop_words=stopwords.words(idioma))
            matriz_documento = vectorizador.fit_transform([documento])

            # Obtiene el vocabulario (términos únicos)
            vocabulario = vectorizador.get_feature_names_out()

            # Verifica si el vocabulario no está vacío
            if len(vocabulario) > 0:
                # Convierte la matriz a un array NumPy si es necesario
                matriz_documento_np = matriz_documento.toarray()

                # Calcula la cantidad de palabras (incluyendo stopwords)
                cantidad_palabras_total = np.sum(matriz_documento_np)

                # Calcula la cantidad de palabras (sin stopwords)
                cantidad_palabras_sin_stopwords = np.sum(matriz_documento_np[:, [i for i, palabra in enumerate(vocabulario) if palabra not in stopwords.words(idioma)]])

                # Calcula la cantidad de términos diferentes sobre cantidad de palabras
                terminos_diferentes_por_palabra = len(vocabulario) / cantidad_palabras_total

                # Calcula los términos más utilizados
                frecuencia_terminos = np.sum(matriz_documento_np, axis=0)
                terminos_mas_utilizados = [vocabulario[i] for i in np.argsort(frecuencia_terminos)[::-1][:3]]

                # Agrega los indicadores a la lista
                indicadores.append({
                    "Cantidad de Palabras (Total)": cantidad_palabras_total,
                    "Cantidad de Palabras (Sin Stopwords)": cantidad_palabras_sin_stopwords,
                    "Términos Diferentes por Palabra": terminos_diferentes_por_palabra,
                    "Término Más Utilizado": terminos_mas_utilizados[0],
                    "2do Término Más Utilizado": terminos_mas_utilizados[1],
                    "3er Término Más Utilizado": terminos_mas_utilizados[2]
                })

    # Convierte la lista de indicadores en un DataFrame
    indicadores_df = pd.DataFrame(indicadores)

    return indicadores_df