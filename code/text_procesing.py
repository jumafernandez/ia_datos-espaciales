# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 14:26:46 2023

@author: jumaf
"""

from funciones_text import cargar_documentos_desde_directorio, procesar_documentos


# Ejemplo de uso:
directorio = "C:/Users/jumaf/Documents/GitHub/ia_datos-espaciales/code/data/papers/20230919-152910-Ambiente"
documentos = cargar_documentos_desde_directorio(directorio)
indicadores = procesar_documentos(documentos)

# Muestra el DataFrame con los indicadores
indicadores.to_excel(f'{directorio}/indicadores.xlsx')





