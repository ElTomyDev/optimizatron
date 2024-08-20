from models.files_manager import FilesManager
from config.app_config import *

files_manager = FilesManager()

def empty_bin_service():
    """
    Llama a la función 'empty_bin' de la clase 'CleanDisk' para
    vaciar la papelera de reciclaje.
    """
    files_manager.empty_bin()

def cleanup_temp_files():
    """
    Recorre una lista donde se almacenan las rutas donde se ubican
    las carpetas de los archivos temporales y elimina el contenido 
    dentro del mismo llamando a 'delete_folder_service' de la clase
    'CleanDisk'.
    """
    for temp_rute in files_manager.get_temps_files():
        files_manager.delete_files_folder(temp_rute)

def empty_download_folder_service():
    """
    Llama a la función 'delete_files_folder' de la clase 'CleanDisk' para
    vaciar la carpeta de descarga, pasándole el la ruta de la misma como 
    parámetro de 'delete_files_folder'.
    """
    files_manager.delete_files_folder(files_manager.get_downloads_folder())