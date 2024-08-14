import os
#from send2trash import send2trash

def delete_files_folder(folder_rute:str):
    '''
    Selecciona la carpeta indicada, y después recorre sus archivos para eliminarlos.
    
    :param folder_rute: String. Ruta *r* de la carpeta.
    '''
    select_folder = os.listdir(folder_rute)
    for file in select_folder:
        select_file = fr"{folder_rute}\{file}"
        try:
            os.remove(select_file)
        except PermissionError:
            print(f"El archivo {select_file} esta en uso y no puede ser eliminado")
            continue

