import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext

class InputSection(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="User Input", padding=8)
        self.parent = parent.winfo_toplevel()  # App root
        self.file_path = tk.StringVar(value="")

        # Layout: 3 columns, responsive
        for i in range(3):
            self.columnconfigure(i, weight=1)

        # Input type
        ttk.Label(self, text="Input Type:").grid(row=0, column=0, sticky="w")
        self.input_type = tk.StringVar(value="Text")
        ttk.Radiobutton(self, text="Text", variable=self.input_type, value="Text").grid(row=0, column=1, sticky="w")
        ttk.Radiobutton(self, text="Image", variable=self.input_type, value="Image").grid(row=0, column=2, sticky="w")

        # File picker row (only used for Image)
        btn_browse = ttk.Button(self, text="Browse Image...", command=self.browse_file)
        btn_browse.grid(row=1, column=0, sticky="w", pady=(4, 0))
        ttk.Label(self, textvariable=self.file_path, foreground="#555").grid(row=1, column=1, columnspan=2, sticky="w", padx=(6,0), pady=(4,0))

        # Text input
        self.text_input = scrolledtext.ScrolledText(self, height=8, wrap="word")
        self.text_input.grid(row=2, column=0, columnspan=3, sticky="nsew", pady=(8, 4))

        # Button row
        btns = ttk.Frame(self)
        btns.grid(row=3, column=0, columnspan=3, sticky="ew")
        for i in range(3):
            btns.columnconfigure(i, weight=1)

        ttk.Button(btns, text="Run Text Model", command=self.run_textgen).grid(row=0, column=0, sticky="ew", padx=(0, 4), pady=(4,0))
        ttk.Button(btns, text="Run Image Model", command=self.run_image_model).grid(row=0, column=1, sticky="ew", padx=4, pady=(4,0))
        ttk.Button(btns, text="Clear", command=self.clear_all).grid(row=0, column=2, sticky="ew", padx=(4,0), pady=(4,0))

    def browse_file(self):
        path = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.webp")])
        if path:
            self.file_path.set(path)
            if self.input_type.get() == "Image":
                self.text_input.insert("end", f"[Image Selected] {path}\n")

    def run_textgen(self):
        app = self.parent
        if getattr(app, "text_model", None):
            prompt = self.text_input.get("1.0", "end").strip()
            output, info, expl = app.text_model.run(prompt)
            app.output_section.set_output(output)
            app.info_section.set_info(info, expl)

    def run_image_model(self):
        app = self.parent
        if getattr(app, "image_model", None) and self.file_path.get():
            output, info, expl = app.image_model.run(self.file_path.get())
            app.output_section.set_output(output)
            app.info_section.set_info(info, expl)

    def clear_all(self):
        self.text_input.delete("1.0", "end")
        self.file_path.set("")
        app = self.parent
        app.output_section.clear()
        app.info_section.clear()
