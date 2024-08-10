import customtkinter as ctk

def custom_title(root, title_text:str):
    """
    Crea un Label personalizado para ser usado como titulo o encabezado tipo 1.
    
    :param root: Ruta del bloque padre.
    :param title_text: String. Texto del titulo.
    """
    return ctk.CTkLabel(root, text=title_text, font=("Arial", 16))