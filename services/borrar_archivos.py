import os
from send2trash import send2trash

def eliminar_archivos_de_una_carpeta(ruta_carpeta):
    
    seleccionar_carpeta = os.listdir(ruta_carpeta)
    for file in seleccionar_carpeta:
        seleccionar_archivo = fr"{ruta_carpeta}\{file}"
        send2trash(seleccionar_archivo)
        

