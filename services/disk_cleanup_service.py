from models.clean_disk import CleanDisk
from config.app_config import *

clean_disk = CleanDisk()

def empty_bin_service():
    """
    Llama a la función 'empty_bin' de la clase 'CleanDisk' para
    vaciar la papelera de reciclaje.
    """
    CleanDisk.empty_bin()

def cleanup_temp_files():
    """
    Recorre una lista donde se almacenan las rutas donde se ubican
    las carpetas de los archivos temporales y elimina el contenido 
    dentro del mismo llamando a 'delete_folder_service' de la clase
    'CleanDisk'.
    """
    for temp_rute in [TEMP_RUTE_1, TEMP_RUTE_2]:
        clean_disk.delete_files_folder(temp_rute)

def empty_download_folder_service():
    """
    Llama a la función 'delete_files_folder' de la clase 'CleanDisk' para
    vaciar la carpeta de descarga, pasándole el la ruta de la misma como 
    parámetro de 'delete_files_folder'.
    """
    clean_disk.delete_files_folder(DOWNLOADS_RUTE)