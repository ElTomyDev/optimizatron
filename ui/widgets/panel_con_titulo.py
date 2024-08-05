import customtkinter as ctk

def panel(root, activo:bool=False, panel_title:str="Example Title", panel_width:int=0, panel_height:int=0, panel_border_width:int=0, panel_border_color:str="black", position_x:int=0, position_y:int=0):
    """
    Crea un panel con un titulo.
    
    :param root: Ruta de la ventana donde sa va a mostrar el panel.
    :param activo: Booleano. Activa o desactiva el panel.
    :param panel_title: String. Titulo del panel.
    :param panel_width: Num Entero. Tamaño de ancho del panel.
    :param panel_height: Num Entero. Tamaño de alto del panel.
    :param panel_border_width: Num Entero. Grosor del borde del panel.
    :param panel_border_color: String. Color del borde del panel.
    :param position_x: Num Entero. Posicion Horizontal del panel.
    :param position_y: Num Entero. Posicion Vertical del panel.
    """
    panel_frame = ctk.CTkFrame(root,
                               width = panel_width,
                               height = panel_height,
                               border_width = panel_border_width,
                               border_color = panel_border_color)
    
    panel_title = ctk.CTkLabel(panel_frame, 
                               text = panel_title, 
                               font = ("Arial", 16))
    if activo:
        panel_frame.place(x=position_x, y=position_y)
        panel_title.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)