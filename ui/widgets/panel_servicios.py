import customtkinter as ctk

def panel_para_deshabilitar_servicios(root, activo:bool=False, panel_title:str="Example Title", panel_border_width:int=0, panel_border_color:str="black", position_x:float=0, position_y:float=0):
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
                               border_width = panel_border_width,
                               border_color = panel_border_color)
    
    panel_title = ctk.CTkLabel(panel_frame, 
                               text = panel_title, 
                               font = ("Arial", 16))
    
    crear_check_boxs(panel_frame, 0.1)
    
    
    
    if activo:
        panel_frame.place(relx=position_x, rely=position_y)
        
        panel_frame.pack_propagate(False)
        
        # Ajusta el tamaño del panel_frame segun su contenido
        #panel_frame.update_idletasks()
        panel_frame.configure(width=panel_frame.winfo_reqwidth(), height=panel_frame.winfo_reqheight())
        
        panel_title.pack(padx=20, pady=20, anchor=ctk.CENTER)
        
def crear_check_boxs(root, margen:float):
    
    for i in range(5):
        margen += 0.2
        check_box = ctk.CTkCheckBox(root,text=f"servicio {i}")
        check_box.place(relx=0.1, rely=margen)

def ajustar_vista(widget, x:float, y:float, activo:bool):
    if activo:
        pass