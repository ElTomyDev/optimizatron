import os
import winshell

class CleanDisk:
    def __init__(self):
        pass
    
    def delete_files_folder(self, folder_location):
        '''
        Selecciona la carpeta indicada, y después recorre sus archivos para eliminarlos.
        
        :param folder_rute: String. Ruta *r* de la carpeta.
        '''
        select_folder = os.listdir(folder_location)
        for file in select_folder:
            select_file = fr"{folder_location}\{file}"
            try:
                os.remove(select_file)
            except PermissionError:
                print(f"El archivo {select_file} esta en uso y no puede ser eliminado")
                continue
    
    def empty_bin():
        """
        Vacía la papelera de reciclaje sin pedir confirmaciones.
        """
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)