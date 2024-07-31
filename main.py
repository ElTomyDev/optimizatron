import os

def eliminar_archivos_de_una_carpeta(ruta_carpeta):
    
    seleccionar_carpeta = os.listdir(ruta_carpeta)
    for file in seleccionar_carpeta:
        seleccionar_archivo = f"{ruta_carpeta}/{file}"
        os.remove(seleccionar_archivo)
        

eliminar_archivos_de_una_carpeta("C:/Users/Administrator/Documents/sss")