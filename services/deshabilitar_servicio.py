import os
from querys.services_win_query import *
import win32serviceutil
import win32con

def detener_servicio(nombre_del_servicio:str):
    """
    Detiene un servicio de windows indicado SOLO si este esta Activo.
    
    :nota: ingora los servicios de que dependen de {nombre_del_servicio}.
    
    :param nombre_del_servicio: String. Nombre del servicio a detener.
    """
    try:
        
        if win32serviceutil.QueryServiceStatus(nombre_del_servicio)[1] ==  4: # Verifica si el estado de un servicio es 4 (RUNNING)
            win32serviceutil.StopServiceWithDeps(nombre_del_servicio)
    except Exception as e:
        print(f"No se pudo encontrar el servicio: '{nombre_del_servicio}': {e}")
def detener_y_deshabilitar_servicio(nombre_del_servicio:str):
    """
    Detiene y Deshabilita el servicio de windows indicado.
    
    :param nombre_del_servicio: String. Nombre del servicio a modificar.
    """
    detener_servicio(nombre_del_servicio)
    os.system(f"sc config {nombre_del_servicio} start= disabled")

