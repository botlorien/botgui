import logging
import sys

try:
    import customtkinter
    import tkinter
except Exception as e:
    logging.exception(e)


def init_root():
    def on_close():
        # This function will be called when the window's close button is clicked
        logging.info("Window closed by user")
        ROOT.destroy()  # Destroy the tkinter window
        sys.exit(0)
    global ROOT
    try:
        customtkinter.CTkFrame(ROOT)
        tkinter._get_default_root('use font')
    except Exception as e:
        logging.exception(e)
        ROOT = customtkinter.CTk()
        ROOT.protocol("WM_DELETE_WINDOW", on_close)
        return ROOT
    else:
        return ROOT


# ROOT = init_root()