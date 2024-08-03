import os
import subprocess

def estado_del_servicio(nombre_del_servicio):
    try:
        resultado = subprocess.run(["sc", "query", nombre_del_servicio], capture_output=True, text=True, check=True)
        salida = resultado.stdout
        return salida
    except subprocess.CalledProcessError as e:
        return f"Error al ejecutar el comando: {e}"

def obtener_pid_del_servicio(nombre_del_servicio):
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

def detener_servicio(nombre_del_servicio):
    
    if "RUNNING" in estado_del_servicio(nombre_del_servicio):
        pid = obtener_pid_del_servicio(nombre_del_servicio)
        if pid:
            os.system(f"taskkill /PID {pid} /F")
        else:
            print(f"El servicio {nombre_del_servicio} no esta en ejecucion o no se pudo consultar su estado")
    

def detener_y_deshabilitar_servicio(nombre_del_servicio):
    detener_servicio(nombre_del_servicio)
    os.system(f"sc config {nombre_del_servicio} start= disabled")
