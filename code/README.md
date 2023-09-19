# Software del proyecto

## scraping.py

1. Para ejecutar el script de web scraping y descargarse los papers en torno a un tema de consulta, se deben configurar previamente los siguientes parámetros en `config.py`:
- CANTIDAD_RESULTADOS = 20 # Cantidad de resultados generales buscados
- QUERY = 'Ambiente' # Concepto de búsqueda
- DIRECTORIO_DESTINO = "data/papers" # Directorio donde se guardaran los PDFs
2. Luego, se debe ejecutar `scraping.py`, el cual generará un directorio con la consulta y la fecha y hora y almacenará los archivos pdf (y el txt correspondiente con el texto del doc) en ese directorio.

## text_procesing.py

1. Para ejecutar el script que prcocesa los txt, se deben configurar previamente los siguientes parámetros en `config.py`:
- DIRECTORIO_TXTS = "C:/Users/jumaf/Documents/GitHub/ia_datos-espaciales/code/data/papers/20230919-174050-Ambiente" # Directorio donde se desea guardar el procesamiento
2. Luego, se debe ejecutar `text_procesing.py`, el cual generará un archivo .xlsx con los indicadores de cada documento txt que forme parte del directorio.
