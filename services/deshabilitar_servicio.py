import os
from querys.services_win_query import *
import win32serviceutil

def detener_servicio(nombre_del_servicio:str):
    """
    Detiene un servicio de windows indicado SOLO si este esta Activo.
    
    :nota: ingora los servicios de que dependen de {nombre_del_servicio}.
    
    :param nombre_del_servicio: String. Nombre del servicio a detener.
    """
    if win32serviceutil.QueryServiceStatus(nombre_del_servicio)[1] ==  4: # Verifica si el estado de un servicio es 4 (RUNNING)
        win32serviceutil.StopService(nombre_del_servicio)

def detener_y_deshabilitar_servicio(nombre_del_servicio:str):
    """
    Detiene y Deshabilita el servicio de windows indicado.
    
    :param nombre_del_servicio: String. Nombre del servicio a modificar.
    """
    detener_servicio(nombre_del_servicio)
    os.system(f"sc config {nombre_del_servicio} start= disabled")

