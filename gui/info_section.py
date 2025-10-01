import tkinter as tk
from tkinter import ttk, scrolledtext

class InfoSection(ttk.LabelFrame):
    """Bottom info area using a Notebook to avoid side-by-side clutter."""
    def __init__(self, parent):
        super().__init__(parent, text="Model Information & Explanation", padding=4)

        nb = ttk.Notebook(self)
        nb.pack(fill="both", expand=True)

        # Tab 1: Selected Model Info
        frame_info = ttk.Frame(nb, padding=6)
        nb.add(frame_info, text="Model Info")
        self.info_box = scrolledtext.ScrolledText(frame_info, height=7, wrap="word")
        self.info_box.pack(fill="both", expand=True)

        # Tab 2: OOP Concepts
        frame_expl = ttk.Frame(nb, padding=6)
        nb.add(frame_expl, text="OOP Concepts")
        self.expl_box = scrolledtext.ScrolledText(frame_expl, height=7, wrap="word")
        self.expl_box.pack(fill="both", expand=True)

    def set_info(self, info, expl):
        self.info_box.config(state="normal")
        self.info_box.delete("1.0", tk.END)
        self.info_box.insert(tk.END, info)
        self.info_box.config(state="disabled")

        self.expl_box.config(state="normal")
        self.expl_box.delete("1.0", tk.END)
        self.expl_box.insert(tk.END, expl)
        self.expl_box.config(state="disabled")

    def clear(self):
        self.info_box.config(state="normal")
        self.info_box.delete("1.0", tk.END)
        self.info_box.config(state="disabled")
        self.expl_box.config(state="normal")
        self.expl_box.delete("1.0", tk.END)
        self.expl_box.config(state="disabled")
