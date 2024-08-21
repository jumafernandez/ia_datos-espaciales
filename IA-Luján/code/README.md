# Ejecución del prototipo

Hasta el momento, el prototipo de software está dividido en dos pequeños módulos:
1. Un primer módulo `scraping.py` que ejecuta una consulta sobre [Google Scholar](https://scholar.google.com/) y retorna los primeros N artículos que se muestran relevantes según el repositorio de _papers_. Sobre esos artículos, selecciona aquellos que poseen un enlace a un pdf y descarga los pdf (cuyo enlace está activo) así cómo el texto en un archivo txt a un directorio pasado como parámetro por el usuario.
2. Un segundo módulo `text_procesing.py` que procesa el texto (archivo txt) de los artículos que no se encontraban en formato imagen y genera un conjunto de indicadores para cada uno de los artículos, el cual persiste en el directorio donde se encuentran los artículos descargados y procesados.

## scraping.py

1. Para ejecutar el script de web scraping y descargarse los papers en torno a un tema de consulta, se deben configurar previamente los siguientes parámetros en `config.py`:
- CANTIDAD_RESULTADOS = 20 # Cantidad de resultados generales buscados
- QUERY = 'Ambiente' # Concepto de búsqueda
- DIRECTORIO_DESTINO = "data/papers" # Directorio donde se guardaran los PDFs
- OFFSET = 1 # Número de resultado a partir del cual se comienzan a guardar los resultados encontrados en la búsqueda
2. Luego, se debe ejecutar `scraping.py`, el cual generará un directorio con la consulta y la fecha y hora y almacenará los archivos pdf (y el txt correspondiente con el texto del doc) en ese directorio.

## text_procesing.py

1. Para ejecutar el script que prcocesa los txt, se deben configurar previamente los siguientes parámetros en `config.py`:
- DIRECTORIO_TXTS = "C:/Users/jumaf/Documents/GitHub/ia_datos-espaciales/code/data/papers/20230919-174050-Ambiente" # Directorio donde se desea guardar el procesamiento
2. Luego, se debe ejecutar `text_procesing.py`, el cual generará un archivo .xlsx con los indicadores de cada documento txt que forme parte del directorio.
