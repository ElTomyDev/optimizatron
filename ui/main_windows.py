import customtkinter as ctk
from config.app_config import WIDTH, HEIGHT, RUTA_TEMP_1, RUTA_TEMP_2
from services.borrar_archivos import eliminar_archivos_de_una_carpeta

class MainWindows(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        ### APP CONFIG ###
        
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.title("Optimizatron")
        
        ### WIDGETS ###
        self.main_grid = ctk.CTkFrame(self)
        self.main_grid.pack(padx=10, pady=10)
        
        # Boton para eliminar archivos temporales
        self.boton_eliminar_temps = ctk.CTkButton(self.main_grid, text="Eliminar archivos temporales",command=self.eliminar_archivos_temporales)
        self.boton_eliminar_temps.grid(row=0,column=0)
        
        # Panel para el apartado de 'Deshabilitar servicios de windows'
        self.panel_service_frame = ctk.CTkFrame(self.main_grid, border_width = 2, border_color = "black")
        self.panel_service_frame.grid(row=0, column=1)
        
        # Titulo para el panel de 'Deshabilitar servicios de windows'
        self.title_service_panel = ctk.CTkLabel(self.panel_service_frame, text="Deshabilitar Servicios", font=("Arial", 16))
        self.title_service_panel.pack(padx=20, pady=(20,0))
        
        ### WIDGETS PARA DESHABILITAR SERVICIOS ###
        self.lista_de_servicios_seleccionados = []
        
        # Crea los checkbox para el panel de 'Deshabilitar servicios de windows'
        self.check_box_frame = ctk.CTkFrame(self.panel_service_frame)
        self.check_box_frame.pack(padx=10, pady=(10,5))
        self.create_checkboxs_for_service_panel(self.check_box_frame)
        
        # Crea el boton para desactivar los servicios de windows seleccionados con los checkboxs
        self.boton_deshabilitar_servicios = ctk.CTkButton(self.panel_service_frame,text="Deshabilitar Servicios")
        self.boton_deshabilitar_servicios.pack(padx=20, pady=(5,20))

    def create_checkboxs_for_service_panel(self, root, lista_de_servicios:list):
        """
        Crea varios CheckBoxs para el panel del apartado de 'Deshabilitar Servicios de Windows'.
        
        :param root: Ruta de la vista donde se ven los checkboxs.
        """
        row_index = 0
        for service in lista_de_servicios:
            self.crear_checkbox_con_un_servicio_asignado(root, service, row_index)
            row_index += 1
    
    def crear_checkbox_con_un_servicio_asignado(self, root,nombre_servicio:str, row_index):
        """
        Crea un checkbox con un nombre de servicio asignado.
        
        :param nombre_servico: String. Nombre del servico a asignarle al checkbox.
        """
        return ctk.CTkCheckBox(root,text=f"servicio {nombre_servicio}", command= lambda: self.agregar_un_servicio_a_la_lista(nombre_servicio)).grid(row=row_index, column=0, padx=5, pady=5)
        
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
    def eliminar_archivos_temporales(self):
        """
        Recorre una lista de carpetas/rutas y elimina sus archivos.
        """
        for ruta_temp in [RUTA_TEMP_1, RUTA_TEMP_2]:
            eliminar_archivos_de_una_carpeta(ruta_temp)
    
    ### Funcion para correr el programa ###
    def run(self):
        self.mainloop()

