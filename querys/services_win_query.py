from  win32 import win32service
import subprocess

def obtener_todos_los_servicios():
    """
    Devuelve una lista con todos los servicios de windows que tiene el usuario en forma de diccionario
    """
    servicios = win32service.EnumServicesStatus(win32service.OpenSCManager(None, None, win32service.SC_MANAGER_ALL_ACCESS))
    lista_servicios = []
    for servicio in servicios:
        name_id, display_name, state = servicio
        servicio_dict = {
            'name': display_name,
            'name_id': name_id,
            'state': state[1]
        }
        lista_servicios.append(servicio_dict)
    return lista_servicios

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
