# -*- coding: utf-8 -*-

from funciones_text import cargar_documentos_desde_directorio, procesar_documentos
from config import DIRECTORIO_TXTS, QUERY, MODEL_SUMMARIZATION


# Ejemplo de uso:
documentos = cargar_documentos_desde_directorio(DIRECTORIO_TXTS)
indicadores = procesar_documentos(documentos, QUERY, MODEL_SUMMARIZATION)

# Muestra el DataFrame con los indicadores
indicadores.to_excel(f'{DIRECTORIO_TXTS}/indicadores.xlsx')
