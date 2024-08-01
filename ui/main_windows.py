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
        self.boton_eliminar_temps = ctk.CTkButton(self, text="Eliminar archivos temporales",command=self.eliminar_archivos_temporales)
        self.boton_eliminar_temps.grid(row=0, column=0, padx=20, pady=10)
    
    ### FUNCIONES PARA BOTONES ###
    def eliminar_archivos_temporales(self):
        for ruta_temp in [RUTA_TEMP_1, RUTA_TEMP_2]:
            eliminar_archivos_de_una_carpeta(ruta_temp)
        
    def run(self):
        self.mainloop()

