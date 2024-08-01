import customtkinter as ctk
from config.app_config import WIDTH, HEIGHT

class MainWindows(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        ### APP CONFIG ###
        
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.title("Optimizatron")
        
        ### WIDGETS ###
    
    def run(self):
        self.mainloop()

