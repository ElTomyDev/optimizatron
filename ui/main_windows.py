import customtkinter as ctk
from config.app_config import *
from ui.widgets.clean_disk_panel_widget import clean_disk_panel
from ui.widgets.windows_services_panel_widget import WindowsServicesPanel

class MainWindows(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        ### APP CONFIG ###
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.title("Optimizatron")
        
        ### WIDGETS ###
        self.main_grid = ctk.CTkFrame(self)
        self.main_grid.pack(padx=10, pady=10)
        
        self.windows_service_panel = WindowsServicesPanel(self.main_grid)
        
        ##########################################################
        
        clean_disk_panel(self.main_grid)
        
        ##########################################################
        
        self.windows_service_panel.windows_service_panel()
        
        ########################################################## 
    
    ### Función para correr el programa ###
    def run(self):
        self.mainloop()

