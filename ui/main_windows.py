import customtkinter as ctk
from config.app_config import *
from services.borrar_archivos import eliminar_archivos_de_una_carpeta
from services.vaciar_papelera import vaciar_papelera
from services.deshabilitar_servicio import *
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
        self.cleanup_frame = ctk.CTkFrame(self.main_grid, border_width=2, border_color="black")
        self.cleanup_frame.grid(row=0,column=0, padx=(10,0), pady=(10, 10))
        
        # Titulo Para el panel de limpieza
        self.title_cleanup_frame = custom_title(self.cleanup_frame, "Limpieza de disco")
        self.title_cleanup_frame.grid(row=0,column=0, padx=20,pady=(20,0))
        
        # Botón para eliminar archivos temporales
        self.button_empty_temps = ctk.CTkButton(self.cleanup_frame, text="Eliminar archivos temporales",command=self.click_eliminar_archivos_temporales)
        self.button_empty_temps.grid(row=1,column=0,padx=20,pady=(20,0))
        
        # Botón para eliminar las descargas
        self.button_empty_downloads = ctk.CTkButton(self.cleanup_frame, text="Eliminar Descargas", command=self.click_eliminar_descargas)
        self.button_empty_downloads.grid(row=2,column=0, padx=20, pady=(7,0))
        
        # Botón para vaciar la papelera
        self.button_empty_bin = ctk.CTkButton(self.cleanup_frame, text="Vaciar Papelera", command=self.click_vaciar_papelera)
        self.button_empty_bin.grid(row=3,column=0, padx=20, pady=(7,20))
        
        ##########################################################
        
        # Frame para el apartado de 'Deshabilitar servicios de windows'
        self.service_frame = ctk.CTkFrame(self.main_grid, border_width = 2, border_color="black")
        self.service_frame.grid(row=0, column=1, padx=(5,10), pady=(10,10))
        
        # Titulo para el frame de 'Deshabilitar servicios de windows'
        self.title_service_panel = custom_title(self.service_frame, "Deshabilitar Servicios")
        self.title_service_panel.grid(row=0, column=0, padx=20, pady=(20,0))
        
        # frame para los botones 'Compatibilidad' y 'Rendimiento'
        self.select_service_bottom_frame = ctk.CTkFrame(self.service_frame)
        self.select_service_bottom_frame.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        # Botón para seleccionar mas compatibilidad
        self.button_compatibility = ctk.CTkButton(self.select_service_bottom_frame, text="Mas Compatibilidad", command=self.click_opcion_de_compatibilidad)
        self.button_compatibility.grid(row=1, column=0, padx=(10, 0), pady=10)
        
        # Botón para seleccionar mas rendimiento
        self.button_performance  = ctk.CTkButton(self.select_service_bottom_frame, text="Mas Rendimiento", command=self.click_opcion_de_rendimiento)
        self.button_performance.grid(row=1, column=1, padx=10, pady=10)
        
        # Frame para Agregar los checkboxes
        self.checkboxes_frame = ctk.CTkFrame(self.service_frame)
        self.checkboxes_frame.grid(row=2, column=0, padx=10, pady=(0,5))
        
        # Agrega los checkboxes
        self.create_checkboxes_for_service_frame(self.checkboxes_frame)
        
        # Crea el botón para desactivar los servicios de windows seleccionados con los checkboxes
        self.button_disable_services = ctk.CTkButton(self.service_frame, text="Deshabilitar Servicios", command=self.click_deshabilitar_lista_de_servicios)
        self.button_disable_services.grid(row=3,column=0,padx=20, pady=(5,20))
        
        # Lista de servicios seleccionados
        self.selected_services_list = []
        
        
        ##########################################################
        
    def create_checkboxes_for_service_frame(self, root):
        """
        Compara la lista con los servicios que se pueden deshabilitar con la lista
        de todos los servicios y si coinciden los servicios crea un checkbox con los
        valores adecuados.
        
        :param root: Ruta de la vista donde se ven los checkboxes.
        """
        row_index = 0
        column_index = 0
        for service_display in LISTA_SERVICIOS:
            for service_dict in obtener_todos_los_servicios():
                for value_type, value in service_dict.items():
                    if value_type == 'name':
                        service_name = value
                    if service_name == service_display:
                        if value_type == 'name_id':
                            self.crear_checkbox_con_un_servicio_asignado(root, value, service_name, row_index, column_index)
                            row_index += 1
                            if row_index == 10:
                                row_index = 0
                                column_index += 1
    
    def crear_checkbox_con_un_servicio_asignado(self, root, id_nombre_servicio:str, nombre_servicio:str, row_index:int, column_index:int):
        """
        Crea un checkbox con un nombre de servicio asignado.
        
        :param nombre_servicio: String. Nombre del servicio a asignarle al checkbox.
        """
        return ctk.CTkCheckBox(root, text=nombre_servicio, command= lambda: self.agregar_un_servicio_a_la_lista(id_nombre_servicio)).grid(row=row_index, column=column_index, padx=5, pady=4, sticky="w")
        
    def agregar_un_servicio_a_la_lista(self, nombre_servicio:str):
        """
        Agrega el nombre de un servicio de windows a una lista y luego la retorna.
        
        :param nombre_servicio: String. Nombre del servicio de windows que se va agregar a la lista
        """
        if nombre_servicio not in self.selected_services_list:
            self.selected_services_list.append(nombre_servicio)
        else:
            self.selected_services_list.remove(nombre_servicio)
        print(self.selected_services_list)
    
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
        Vacía la papelera cuando se haga click en el boton
        """
        vaciar_papelera()
        
    
    def click_deshabilitar_lista_de_servicios(self):
        """
        Recorre una lista con los nombres de los servicios que se desean deshabilitar.
        """
        for service in self.selected_services_list:
            detener_y_deshabilitar_servicio(service)
        self.desmarcar_todos_checkboxes()
    
    def click_opcion_de_rendimiento(self):
        """
        Selecciona TODOS los checkboxes.
        """
        for checkbox in self.checkboxes_frame.winfo_children():
            if isinstance(checkbox, ctk.CTkCheckBox):
                if checkbox.get() == 0:
                    checkbox.toggle(1)
                else:
                    checkbox.toggle(0)
    
    def click_opcion_de_compatibilidad(self):
        """
        Selecciona SOLO los checkbox que no afecten a la compatibilidad del sistema.
        """
        
        for service in LISTA_SERVICIOS_COMPATIBILIDAD:
            for checkbox in self.checkboxes_frame.winfo_children():
                if isinstance(checkbox, ctk.CTkCheckBox):
                    if checkbox.cget("text") != service:
                        if checkbox.get() == 0:
                            checkbox.toggle(1)
                        else:
                            checkbox.toggle(0)
    
    ### Funciones de UTILIDAD ###
    def desmarcar_todos_checkboxes(self):
        """
        Desmarca todos los checkboxes que estén seleccionados y limpia la lista de servicios
        seleccionados.
        """
        for checkbox in self.checkboxes_frame.winfo_children():
            if isinstance(checkbox, ctk.CTkCheckBox):
                if checkbox.get() == 1:
                    checkbox.toggle(0)
                
    
    ### Función para correr el programa ###
    def run(self):
        self.mainloop()

