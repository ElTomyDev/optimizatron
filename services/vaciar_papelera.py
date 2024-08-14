import winshell

def empty_bin():
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)