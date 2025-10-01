import tkinter as tk
from tkinter import ttk

class ModelInfoSection(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        ttk.Label(self, text='Model Information & Explanation').pack(anchor='w')
        self.info_text = tk.Text(self, height=6)
        self.info_text.pack(fill='x', pady=(4,4))

    def set_info(self, info_dict):
        self.info_text.delete('1.0', 'end')
        for k,v in info_dict.items():
            self.info_text.insert('end', f'{k}: {v}\n')
