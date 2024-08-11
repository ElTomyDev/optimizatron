import winshell

def vaciar_papelera():
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)