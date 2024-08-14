from  win32 import win32service
import subprocess

def get_all_services():
    """
    Devuelve una lista con todos los servicios de windows que tiene el usuario en forma de diccionario.
    """
    services = win32service.EnumServicesStatus(win32service.OpenSCManager(None, None, win32service.SC_MANAGER_ALL_ACCESS))
    services_list = []
    for service in services:
        name_id, display_name, state = service
        service_dict = {
            'name': display_name,
            'name_id': name_id,
            'state': state[1]
        }
        services_list.append(service_dict)
    return services_list

def get_service_pid(id_service_name:str):
    '''
    Consulta el PID del servicio de windows que este habilitado.
    
    :param id_service_name: String. Nombre del servicio a consultar.
    '''
    try:
        query = subprocess.run(["sc", "queryex", id_service_name], capture_output=True, text=True, check=True)
        output = query.stdout
        for line in output.splitlines():
            if "PID" in line:
                pid = int(line.split()[-1])
                return pid
        return None
    except subprocess.CalledProcessError as e:
        return f"Error al ejecutar el comando: {e}"
