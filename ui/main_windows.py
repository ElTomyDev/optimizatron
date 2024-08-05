import customtkinter as ctk
from config.app_config import WIDTH, HEIGHT, RUTA_TEMP_1, RUTA_TEMP_2
from services.borrar_archivos import eliminar_archivos_de_una_carpeta
from ui.widgets.panel_con_titulo import panel

class MainWindows(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        ### APP CONFIG ###
        
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.title("Optimizatron")
        
        ### WIDGETS ###
        self.boton_eliminar_temps = ctk.CTkButton(self, text="Eliminar archivos temporales",command=self.eliminar_archivos_temporales)
        self.boton_eliminar_temps.place(x=0, y=0,)
        
        panel(self, True, "Deshabilitar Servicios", 280, 200, 10, "black", 200, 0)
    
    ### FUNCIONES PARA BOTONES ###
    def eliminar_archivos_temporales(self):
        """
        Recorre una lista de carpetas/rutas y elimina sus archivos.
        """
        for ruta_temp in [RUTA_TEMP_1, RUTA_TEMP_2]:
            eliminar_archivos_de_una_carpeta(ruta_temp)
        
    def run(self):
        self.mainloop()

