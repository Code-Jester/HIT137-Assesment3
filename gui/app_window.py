import tkinter as tk
from tkinter import ttk, Menu, messagebox
from .input_section import InputSection
from .output_section import OutputSection
from .info_section import InfoSection


try:
    from models.text_model import TextModel
    from models.image_model import ImageModel
except Exception:
    TextModel = ImageModel = None


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter AI Workbench")
        self.geometry("1000x700")
        self.minsize(900, 600)

        # ttk theming & spacing
        self.style = ttk.Style(self)
        if "clam" in self.style.theme_names():
            self.style.theme_use("clam")
        self.style.configure("TLabelFrame", padding=8)
        self.style.configure("TButton", padding=(10, 6))
        self.style.configure("TCombobox", padding=4)

        # Models (kept as attributes so existing logic still works)
        self.text_model = None
        self.image_model = None

        self._create_menu()
        self._create_layout()
        self._create_statusbar()

    # Menu
    def _create_menu(self):
        menubar = Menu(self)
        self.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.destroy)
        menubar.add_cascade(label="File", menu=file_menu)

        model_menu = Menu(menubar, tearoff=0)
        model_menu.add_command(label="Load Models", command=self.load_models)
        menubar.add_cascade(label="Models", menu=model_menu)

        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=lambda: messagebox.showinfo(
            "About", "Group 55 Assesment 3, TKinter Ai GUI project 2025"))
        menubar.add_cascade(label="Help", menu=help_menu)

    # Top Bar
    def _create_layout(self):
        container = ttk.Frame(self, padding=(10, 10, 10, 6))
        container.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Top Controls
        topbar = ttk.Frame(container)
        topbar.grid(row=0, column=0, sticky="ew", pady=(0, 8))
        topbar.columnconfigure(2, weight=1)

        ttk.Label(topbar, text="Model:").grid(row=0, column=0, sticky="w")
        self.model_combo = ttk.Combobox(
            topbar, values=["Text Generation", "Image Classification"], state="readonly", width=28
        )
        self.model_combo.current(0)
        self.model_combo.grid(row=0, column=1, padx=(6, 10), sticky="w")
        ttk.Button(topbar, text="Load", command=self.load_models).grid(row=0, column=3, sticky="w")

        # Split left (input) / right (output)
        paned = ttk.Panedwindow(container, orient="horizontal")
        paned.grid(row=1, column=0, sticky="nsew")
        container.rowconfigure(1, weight=1)
        container.columnconfigure(0, weight=1)

        # Left pane: Input
        left_frame = ttk.Frame(paned)
        self.input_section = InputSection(left_frame)
        self.input_section.pack(fill="both", expand=True)
        paned.add(left_frame, weight=1)

        # Right pane: Output
        right_frame = ttk.Frame(paned)
        self.output_section = OutputSection(right_frame)
        self.output_section.pack(fill="both", expand=True)
        paned.add(right_frame, weight=1)

        # Bottom info (full width)
        self.info_section = InfoSection(container)
        self.info_section.grid(row=2, column=0, sticky="nsew", pady=(8, 0))

        container.rowconfigure(2, weight=0)

        # Notes (subtle helper text)
        self.notes_var = tk.StringVar(value="Tip: Load models, enter text or pick an image, then run.")
        notes = ttk.Label(container, textvariable=self.notes_var, foreground="#666")
        notes.grid(row=3, column=0, sticky="w", pady=(6, 0))

    # Status
    def _create_statusbar(self):
        self.status = tk.StringVar(value="Ready")
        bar = ttk.Label(self, textvariable=self.status, anchor="w")
        bar.grid(row=1, column=0, sticky="ew")
        self.grid_rowconfigure(1, weight=0)

    # Actions
    def load_models(self):
        try:
            self.status.set("Loading models...")
            if TextModel:
                self.text_model = TextModel()
            if ImageModel:
                self.image_model = ImageModel()
            self.output_section.append_text(" Models loaded successfully!\n")
            self.status.set("Models loaded")
        except Exception as e:
            self.status.set("Error while loading models")
            messagebox.showerror("Error", f"Model loading failed: {e}")


if __name__ == "__main__":
    app = App()
    app.mainloop()
