import customtkinter as ctk
from ui.widgets.titulo import custom_title
from services.disable_services import *
from querys.services_win_query import *
from config.app_config import *


class WindowsServicesPanel:
    def __init__(self, root):
        
        self.root = root
        # Lista de servicios seleccionados
        self.selected_services_list = []
        # Contador para la cantidad de veces que se presiono un botón
        self.count_click_button = 0
    
    def windows_service_panel(self): 
        
        # Frame para el apartado de 'Deshabilitar servicios de windows'
        self.service_frame = ctk.CTkFrame(self.root, border_width = 2, border_color="black")
        self.service_frame.grid(row=0, column=1, padx=(5,10), pady=(10,10))
        
        # Titulo para el frame de 'Deshabilitar servicios de windows'
        self.title_service_panel = custom_title(self.service_frame, "Deshabilitar Servicios")
        self.title_service_panel.grid(row=0, column=0, padx=20, pady=(20,0))
        
        # frame para los botones 'Compatibilidad' y 'Rendimiento'
        self.select_service_bottom_frame = ctk.CTkFrame(self.service_frame)
        self.select_service_bottom_frame.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        # Botón para seleccionar mas compatibilidad
        self.button_compatibility = ctk.CTkButton(self.select_service_bottom_frame, text="Mas Compatibilidad", command=self.click_compatibility_option)
        self.button_compatibility.grid(row=1, column=0, padx=(10, 0), pady=10)
        
        # Botón para seleccionar mas rendimiento
        self.button_performance  = ctk.CTkButton(self.select_service_bottom_frame, text="Mas Rendimiento", command=self.click_performance_option)
        self.button_performance.grid(row=1, column=1, padx=10, pady=10)
        
        # Frame para Agregar los checkboxes
        self.checkboxes_frame = ctk.CTkFrame(self.service_frame)
        self.checkboxes_frame.grid(row=2, column=0, padx=10, pady=(0,5))
        
        # Agrega los checkboxes
        self.create_checkboxes_for_service_frame(self.checkboxes_frame)
        
        # Crea el botón para desactivar los servicios de windows seleccionados con los checkboxes
        self.button_disable_services = ctk.CTkButton(self.service_frame, text="Deshabilitar Servicios", command=self.click_disable_service_list)
        self.button_disable_services.grid(row=3,column=0,padx=20, pady=(5,20))
        
        
    
    ### FUNCIONES PARA LOS WIDGETS ###
    def create_checkboxes_for_service_frame(self, root):
        """
        Compara la lista con los servicios que se pueden deshabilitar con la lista
        de todos los servicios y si coinciden los servicios crea un checkbox con los
        valores adecuados.
        """
        row_index = 0
        column_index = 0
        for service_display in REMOVABLE_SERVICE_LIST: # Recorre una lista con servicios que se pueden deshabilitar
            for service_dict in get_all_services(): # Recorre la lista con todos los servicios (En forma de diccionario)
                for value_type, value in service_dict.items(): # Recorre el diccionario con los valores del servicio
                    if value_type == 'name':
                        service_name = value
                    if service_name == service_display:
                        if value_type == 'name_id':
                            self.create_checkbox_with_service_assigned(root, value, service_name, row_index, column_index)
                            row_index += 1
                            if row_index == 10:
                                row_index = 0
                                column_index += 1
    
    def create_checkbox_with_service_assigned(self, root, id_service_name:str, service_name:str, row_index:int, column_index:int):
        """
        Crea un checkbox que guarda la id de un servicio de windows.
        
        :param id_service_name: String. ID del nombre del servicio a guardar en el checkbox.
        :param service_name: String. Nombre del servicio como descripción del checkbox.
        :param row_index: Integer. Index de la fila donde se ubica el checkbox.
        :param column_index: Integer. Index de la columna donde se ubica el checkbox.
        """
        return ctk.CTkCheckBox(root, text=service_name, command= lambda: self.add_service_to_list(id_service_name)).grid(row=row_index, column=column_index, padx=5, pady=4, sticky="w")
    
    ### FUNCIONES PARA BOTONES ###
    def click_disable_service_list(self):
        """
        Recorre una lista con los nombres de los servicios, los deshabilita y desmarca todos los checkboxes.
        
        """
        for service in self.selected_services_list:
            stop_and_disable_service(service)
        self.uncheck_all_checkboxes()
    
    def click_performance_option(self):
        """
        Selecciona TODOS los checkboxes.
        """
        self.count_click_button += 1
        for checkbox in self.checkboxes_frame.winfo_children():
            if isinstance(checkbox, ctk.CTkCheckBox):
                if checkbox.get() == 0:
                    checkbox.toggle(1)
        
        if self.count_click_button >= 2:
            self.uncheck_all_checkboxes()
            self.count_click_button = 0
    
    def click_compatibility_option(self):
        """
        Selecciona SOLO los checkbox que no afecten a la compatibilidad del sistema.
        """
        
        self.count_click_button += 1
        for service in REMOVABLE_FOR_MORE_COMPATIBILITY_LIST:
            for checkbox in self.checkboxes_frame.winfo_children():
                if isinstance(checkbox, ctk.CTkCheckBox):
                    if checkbox.cget("text") != service:
                        checkbox.toggle(1)
        
        if self.count_click_button >= 2:
            self.uncheck_all_checkboxes()
            self.count_click_button = 0
        
    ### Funciones de UTILIDAD ###
    def uncheck_all_checkboxes(self):
        """
        Desmarca todos los checkboxes que estén seleccionados.
        """
        for checkbox in self.checkboxes_frame.winfo_children():
            if isinstance(checkbox, ctk.CTkCheckBox):
                if checkbox.get() == 1:
                    checkbox.toggle(0)
                
    def add_service_to_list(self, id_service_name:str):
        """
        Agrega el nombre global(id) de un servicio de windows a una lista.
        
        :param id_service_name: String. Nombre (ID) del servicio de windows que se va agregar a la lista
        """
        if id_service_name not in self.selected_services_list:
            self.selected_services_list.append(id_service_name)
        else:
            self.selected_services_list.remove(id_service_name)
        print(self.selected_services_list)
