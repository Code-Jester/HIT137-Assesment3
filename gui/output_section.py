import tkinter as tk
from tkinter import ttk, scrolledtext

class OutputSection(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Model Output", padding=8)
        self.output_display = scrolledtext.ScrolledText(self, height=18, wrap="word")
        self.output_display.configure(font=("Consolas", 10))
        self.output_display.pack(fill="both", expand=True)
        self.output_display.config(state="disabled")

    def set_output(self, text):
        self.output_display.config(state="normal")
        self.output_display.delete("1.0", tk.END)
        self.output_display.insert(tk.END, text)
        self.output_display.config(state="disabled")

    def append_text(self, text):
        self.output_display.config(state="normal")
        self.output_display.insert(tk.END, text)
        self.output_display.config(state="disabled")

    def clear(self):
        self.output_display.config(state="normal")
        self.output_display.delete("1.0", tk.END)
        self.output_display.config(state="disabled")
