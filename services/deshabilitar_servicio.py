import os
import subprocess
from  win32 import win32service


def lista_de_todos_los_servicios():
    servicios = win32service
    
def estado_del_servicio(nombre_del_servicio:str):
    '''
    Consulta el estado en el que se encuentra el servicio de windows indicado
    y devuelve una "tabla" con sus valores.
    
    :param nombre_del_servicio: String. Nombre del servicio a verificar.
    '''
    try:
        resultado = subprocess.run(["sc", "query", nombre_del_servicio], capture_output=True, text=True, check=True)
        salida = resultado.stdout
        return salida
    except subprocess.CalledProcessError as e:
        return f"Error al ejecutar el comando: {e}"

def obtener_pid_del_servicio(nombre_del_servicio:str):
    '''
    Consulta el PID del servicio de windows que este habilitado.
    
    :param nombre_del_servicio: String. Nombre del servicio a consultar.
    '''
    
    try:
        resultado = subprocess.run(["sc", "queryex", nombre_del_servicio], capture_output=True, text=True, check=True)
        salida = resultado.stdout
        for line in salida.splitlines():
            if "PID" in line:
                pid = int(line.split()[-1])
                return pid
        return None
    except subprocess.CalledProcessError as e:
        return f"Error al ejecutar el comando: {e}"

def detener_servicio(nombre_del_servicio:str):
    """
    Detiene un servicio de windows indicado SOLO si este esta Activo.
    
    :nota: ingora los servicios de que dependen de {nombre_del_servicio}.
    
    :param nombre_del_servicio: String. Nombre del servicio a detener.
    """
    
    if "RUNNING" in estado_del_servicio(nombre_del_servicio): 
        pid = obtener_pid_del_servicio(nombre_del_servicio)
        if pid:
            os.system(f"taskkill /PID {pid} /F")
        else:
            print(f"El servicio {nombre_del_servicio} no esta en ejecucion o no se pudo consultar su estado")
    

def detener_y_deshabilitar_servicio(nombre_del_servicio:str):
    """
    Detiene y Deshabilita el servicio de windows indicado.
    
    :param nombre_del_servicio: String. Nombre del servicio a modificar.
    """
    detener_servicio(nombre_del_servicio)
    os.system(f"sc config {nombre_del_servicio} start= disabled")

