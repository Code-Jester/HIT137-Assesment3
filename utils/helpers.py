from tkinter import messagebox
import traceback

#for safe checking
def safe_run(func):
    try:
        func()
    except Exception as e:
        traceback.print_exc()
        messagebox.showerror('Error', str(e))
