import requests
import os

def encontrar_proximo_id_a_descargar(ruta_directorio):
    """
    Encuentra el próximo ID a asignar para un archivo PDF en un directorio dado.

    Parámetros:
    ruta_directorio (str): La ruta del directorio donde se encuentran los archivos PDF.

    Retorna:
    int: El próximo ID a asignar para el archivo PDF.
    """
    # Esta lista almacena los números de los nombres de los archivos PDF
    numeros = []
    
    # Itera a través de los archivos en el directorio
    for archivo in os.listdir(ruta_directorio):
        # Verifica si el archivo es un PDF
        if archivo.endswith('.pdf'):
            try:
                # Intenta convertir el nombre del archivo a un número
                numero = int(os.path.splitext(archivo)[0])
                # Agrega el número a la lista
                numeros.append(numero)
            except ValueError:
                # Si no se puede convertir a número, continúa con el siguiente archivo
                continue
    
    # Si se encontraron números en los nombres de los archivos
    if numeros:
        # Calcula el mayor número y agrega 1 para obtener el próximo ID a asignar
        proximo_id = max(numeros) + 1
        return proximo_id
    else:
        # Si no se encontraron números, el próximo ID es 1
        return 1

# Ejemplo de uso:
# id = encontrar_proximo_id_a_descargar('/ruta/donde/persistimos/pdfs')

def descargar_pdf(url, id, carpeta_destino):
    """
    Descarga un archivo PDF desde una URL y lo guarda en una carpeta especificada.

    Parámetros:
    url (str): La URL del archivo PDF, donde {ID} será reemplazado por el valor proporcionado.
    id (int): El ID que se usará para reemplazar {ID} en la URL.
    carpeta_destino (str): La ruta de la carpeta donde se guardará el archivo PDF descargado.

    Retorna:
    None
    """
    # Reemplaza {ID} en la URL con el valor proporcionado
    url_con_id = url.format(ID=id)
    
    # Realiza la solicitud HTTP para obtener el PDF
    respuesta = requests.get(url_con_id)
    
    # Verifica si la solicitud fue exitosa (código 200) y si la respuesta contiene un PDF
    if respuesta.status_code == 200 and 'Content-Type' in respuesta.headers and 'application/pdf' in respuesta.headers['Content-Type']:
        # Si la respuesta es exitosa y contiene un PDF, crea la ruta completa para guardar el PDF
        ruta_pdf = os.path.join(carpeta_destino, f"{id}.pdf")
        
        # Guarda el contenido del PDF en la ruta especificada
        with open(ruta_pdf, "wb") as archivo_pdf:
            archivo_pdf.write(respuesta.content)
        
        print(f"PDF descargado en {ruta_pdf}")
    else:
        # Si la solicitud no fue exitosa o la respuesta no es un PDF, imprime un mensaje indicando el problema
        print(f"No se pudo descargar el PDF (o no es un PDF) para el ID {id}.")

# Ejemplo de uso:
# descargar_pdf('http://ejemplo.com/pdf/{ID}', 123, '/ruta/para/guardar/pdfs')
