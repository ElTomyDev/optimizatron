import os
import winshell

class FilesManager:
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
    
    def empty_bin(self):
        """
        Vacía la papelera de reciclaje sin pedir confirmaciones.
        """
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
    
    def get_downloads_folder(self):
        """
        Devuelve la ruta a la carpeta de descargas del usuario actual en un sistema operativo Windows.

        Esta función construye y retorna la ruta estándar a la carpeta de descargas para el usuario
        actual utilizando la variable de entorno 'USERPROFILE'. Esta ruta es la predeterminada en
        Windows para almacenar archivos descargados desde el navegador u otras aplicaciones.
        """
        
        downloads_path = os.path.join(os.getenv('USERPROFILE'), 'Downloads')
        return downloads_path
    
    def get_temps_files(self):
        """
        devuelve una lista que contiene las rutas de las carpetas temporales en un sistema 
        operativo Windows 10. Estas rutas incluyen la carpeta temporal específica del usuario 
        actual y la carpeta temporal utilizada por el sistema operativo para almacenar archivos 
        temporales compartidos.
        """
        user_temp_path = os.getenv('TEMP')
        
        system_temp_path = os.path.join(os.getenv('SystemRoot'), 'Temp')
        return [user_temp_path, system_temp_path]

