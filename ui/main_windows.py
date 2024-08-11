import customtkinter as ctk
from config.app_config import *
from services.borrar_archivos import eliminar_archivos_de_una_carpeta
from services.vaciar_papelera import vaciar_papelera
from services.deshabilitar_servicio import detener_y_deshabilitar_servicio
from querys.services_win_query import *
from ui.widgets.titulo import custom_title

class MainWindows(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        ### APP CONFIG ###
        
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.title("Optimizatron")
        
        ### WIDGETS ###
        self.main_grid = ctk.CTkFrame(self)
        self.main_grid.pack(padx=10, pady=10)
        
        ##########################################################
        
        # Frame para botones de limpieza
        self.limpieza_frame = ctk.CTkFrame(self.main_grid, border_width=2, border_color="black")
        self.limpieza_frame.grid(row=0,column=0, padx=(10,0), pady=(10, 10))
        
        # Titulo Para el panel de limpieza
        self.titulo_limpieza_panel = custom_title(self.limpieza_frame, "Limpieza de disco")
        self.titulo_limpieza_panel.grid(row=0,column=0, padx=20,pady=(20,0))
        
        # Boton para eliminar archivos temporales
        self.boton_eliminar_temps = ctk.CTkButton(self.limpieza_frame, text="Eliminar archivos temporales",command=self.click_eliminar_archivos_temporales)
        self.boton_eliminar_temps.grid(row=1,column=0,padx=20,pady=(20,0))
        
        # Boton para eliminar las descargas
        self.boton_eliminar_descargas = ctk.CTkButton(self.limpieza_frame, text="Eliminar Descargas", command=self.click_eliminar_descargas)
        self.boton_eliminar_descargas.grid(row=2,column=0, padx=20, pady=(7,0))
        
        # Botom para vaciar la papelera
        self.boton_vaciar_papelera = ctk.CTkButton(self.limpieza_frame, text="Vaciar Papelera", command=self.click_vaciar_papelera)
        self.boton_vaciar_papelera.grid(row=3,column=0, padx=20, pady=(7,20))
        
        ##########################################################
        
        # Panel para el apartado de 'Deshabilitar servicios de windows'
        self.panel_service_frame = ctk.CTkFrame(self.main_grid, border_width = 2, border_color="black")
        self.panel_service_frame.grid(row=0, column=1, padx=(5,10), pady=(10,10))
        
        # Titulo para el panel de 'Deshabilitar servicios de windows'
        self.title_service_panel = custom_title(self.panel_service_frame, "Deshabilitar Servicios")
        self.title_service_panel.grid(row=0, column=0, padx=20, pady=(20,0))
        
        # Frame para Agregar los checkbox
        self.check_box_frame = ctk.CTkFrame(self.panel_service_frame)
        self.check_box_frame.grid(row=1, column=0, padx=10, pady=(20,5))
        
        # Agrega los checkboxs
        self.create_checkboxs_for_service_panel(self.check_box_frame, LISTA_SERVICIOS)
        
        # Crea el boton para desactivar los servicios de windows seleccionados con los checkboxs
        self.boton_deshabilitar_servicios = ctk.CTkButton(self.panel_service_frame, text="Deshabilitar Servicios", command=self.click_deshabilitar_lista_de_servicios)
        self.boton_deshabilitar_servicios.grid(row=2,column=0,padx=20, pady=(5,20))
        
        # Lista de servicios seleccionados
        self.lista_de_servicios_seleccionados = []
        
        ##########################################################
        
    def create_checkboxs_for_service_panel(self, root, lista_de_servicios:list):
        """
        Crea varios CheckBoxs para el panel del apartado de 'Deshabilitar Servicios de Windows'.
        
        :param root: Ruta de la vista donde se ven los checkboxs.
        :param lista_de_servicios: Lista de servicios disponibles a seleccionar.
        """
        row_index = 0
        column_index = 0
        for service_display in lista_de_servicios:
            for service in obtener_todos_los_servicios():
                for key, value in service.items():
                    if key == 'name':
                        service_name = value
                    if service_name == service_display:
                        if key == 'name_id':
                            self.crear_checkbox_con_un_servicio_asignado(root, value, service_name, row_index, column_index)
                            row_index += 1
                            if row_index == 10:
                                row_index = 0
                                column_index += 1
    
    def crear_checkbox_con_un_servicio_asignado(self, root, id_nombre_servicio:str, nombre_servicio:str, row_index:int, column_index:int):
        """
        Crea un checkbox con un nombre de servicio asignado.
        
        :param nombre_servico: String. Nombre del servico a asignarle al checkbox.
        """
        self.check_box = ctk.CTkCheckBox(root, text=nombre_servicio, command= lambda: self.agregar_un_servicio_a_la_lista(id_nombre_servicio)).grid(row=row_index, column=column_index, padx=5, pady=4, sticky="w")
        return self.check_box
        
    def agregar_un_servicio_a_la_lista(self, nombre_servico:str):
        """
        Agrega el nombre de un servicio de windows a una lista y luego la retorna.
        
        :param nombre_servicio: String. Nombre del servicio de windows que se va agregar a la lista
        """
        if nombre_servico not in self.lista_de_servicios_seleccionados:
            self.lista_de_servicios_seleccionados.append(nombre_servico)
        else:
            self.lista_de_servicios_seleccionados.remove(nombre_servico)
        print(self.lista_de_servicios_seleccionados)
    
    ### FUNCIONES PARA BOTONES ###
    def click_eliminar_archivos_temporales(self):
        """
        Recorre una lista de carpetas/rutas y elimina sus archivos.
        """
        for ruta_temp in [RUTA_TEMP_1, RUTA_TEMP_2]:
            eliminar_archivos_de_una_carpeta(ruta_temp)
    
    def click_eliminar_descargas(self):
        """
        Elimina la carpeta descargas al cuando se haga click en el boton
        """
        eliminar_archivos_de_una_carpeta(RUTA_DESCARGAS)
    
    def click_vaciar_papelera(self):
        """
        Vacia la papelera cuando se haga click en el boton
        """
        vaciar_papelera()
    
    def click_deshabilitar_lista_de_servicios(self):
        """
        Recorre una lista con los nombres de los servicios que se desean deshabilitar.
        """
        for service in self.lista_de_servicios_seleccionados:
            
            detener_y_deshabilitar_servicio(service)
        
        self.lista_de_servicios_seleccionados.clear() # Limpia la lista de servicios que se seleccionaron
        
        
    
        
    
    
    ### Funcion para correr el programa ###
    def run(self):
        self.mainloop()

