import customtkinter as ctk
from ui.widgets.titulo import custom_title
from services.disk_cleanup_service import *

def clean_disk_panel(root):
    # Frame para botones de limpieza
    cleanup_frame = ctk.CTkFrame(root, border_width=2, border_color="black")
    cleanup_frame.grid(row=0,column=0, padx=(10,0), pady=(10, 10))
    
    # Titulo Para el panel de limpieza
    title_cleanup_frame = custom_title(cleanup_frame, "Limpieza de disco")
    title_cleanup_frame.grid(row=0,column=0, padx=20,pady=(20,0))
    
    # Botón para eliminar archivos temporales
    button_empty_temps = ctk.CTkButton(cleanup_frame, text="Eliminar archivos temporales",command=cleanup_temp_files)
    button_empty_temps.grid(row=1,column=0,padx=20,pady=(20,0))
    
    # Botón para eliminar las descargas
    button_empty_downloads = ctk.CTkButton(cleanup_frame, text="Eliminar Descargas", command=empty_download_folder_service)
    button_empty_downloads.grid(row=2,column=0, padx=20, pady=(7,0))
    
    # Botón para vaciar la papelera
    button_empty_bin = ctk.CTkButton(cleanup_frame, text="Vaciar Papelera", command=empty_bin_service)
    button_empty_bin.grid(row=3,column=0, padx=20, pady=(7,20))