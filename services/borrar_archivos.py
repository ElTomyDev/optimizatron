import os
#from send2trash import send2trash

def eliminar_archivos_de_una_carpeta(ruta_carpeta):
    
    seleccionar_carpeta = os.listdir(ruta_carpeta)
    for file in seleccionar_carpeta:
        seleccionar_archivo = fr"{ruta_carpeta}\{file}"
        try:
            os.remove(seleccionar_archivo)
        except PermissionError:
            print(f"El archivo {seleccionar_archivo} esta en uso y no puede ser eliminado")
            continue

