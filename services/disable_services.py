import os
from querys.services_win_query import *
import win32serviceutil
import win32con

def stop_service(id_service_name:str):
    """
    Detiene un servicio de windows indicado SOLO si este esta Activo.
    
    :nota: ignora los servicios de que dependen de {id_service_name}.
    
    :param id_service_name: String. Nombre (ID) del servicio a detener.
    """
    try:
        
        if win32serviceutil.QueryServiceStatus(id_service_name)[1] ==  4: # Verifica si el estado de un servicio es 4 (RUNNING)
            win32serviceutil.StopServiceWithDeps(id_service_name)
    except Exception as e:
        print(f"No se pudo encontrar el servicio: '{id_service_name}': {e}")

def stop_and_disable_service(id_service_name:str):
    """
    Detiene y Deshabilita el servicio de windows indicado.
    
    :param id_service_name: String. Nombre (id) del servicio a modificar.
    """
    stop_service(id_service_name)
    os.system(f"sc config {id_service_name} start= disabled")

