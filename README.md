# OPTIMIZATRON

Una aplicación que sirve para optimizar tu PC al máximo posible.

## Contenidos

1. [Introduccion](#introduccion)
2. [Instalacion](#instalacion)
3. [Uso](#uso)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Ejemplos de Codigo](#ejemplos-de-codigo)
6. [Contribuir](#contribuir)
7. [Licencia](#licencia)
8. [Creditos](#creditos)

## introduccion

Esta aplicación está dedicada, sobre todo, a aquellas personas con una PC de bajos recursos o que han quedado rezagadas en cuanto a rendimiento, debido a que cada vez las aplicaciones exigen más y más recursos.

Con esta aplicación podrás borrar archivos temporales, así como también desactivar servicios que no se utilizan de manera cotidiana, junto con otras funcionalidades adicionales.

## instalacion
Para poder utilizar la aplicacion solo tienes que clonar este repositorio

## uso

1. Boton para borrar archivos temporales - El boton ejecuta la funcion '[Comando](services/borrar_archivos.py)'

## estructura-del-proyecto

OPTIMIZATRON
|--config/                          -> 'Archivos de configuracion'
|  |-- app_config.py                -> 'Configuracion general del proyecto'
|--services/                        -> 'Archivos con la logica de la aplicacion'
|  |-- borrar_archivos.py           -> 'Logica para borrar los archivos temporales'
|  |-- deshabilitar_servicio.py     -> 'Logica para detener y deshabilitar servicios'
|--ui/                              -> 'Archivos para crear la interfaz de usuario'
|  |--widgets/                      -> 'Carpeta para los widgets personalizados de la interfaz'
|  |-- main_windows.py              -> 'Construccion de la interfaz'
|-- main.py                         -> 'Ejecucion de la app'
|-- README-PROJECT.md
|-- requirements.txt                -> 'Requerimientos y Dependencias'