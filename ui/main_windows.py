import customtkinter as ctk

class MainWindows(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("600x500")
        self.title("Optimizatron")
    
    def run(self):
        self.mainloop()
    
    
        
