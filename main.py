import customtkinter as ctk
from tkinter import filedialog
from tkinter import messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class ShortsAutomatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("YouTube Shorts Automator")
        self.geometry("900x700")

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = ctk.CTkLabel(self, text="YouTube Shorts Automator", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=20)

        # Frame for Inputs
        self.input_frame = ctk.CTkFrame(self)
        self.input_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # User Ideas
        self.user_ideas_label = ctk.CTkLabel(self.input_frame, text="User Ideas")
        self.user_ideas_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.user_ideas_entry = ctk.CTkTextbox(self.input_frame, height=80)
        self.user_ideas_entry.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

        # Gemini Ideas
        self.gemini_ideas_label = ctk.CTkLabel(self.input_frame, text="Gemini Ideas")
        self.gemini_ideas_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.gemini_ideas_entry = ctk.CTkTextbox(self.input_frame, height=80)
        self.gemini_ideas_entry.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")

        # Script per Idea
        self.scripts_label = ctk.CTkLabel(self.input_frame, text="Scripts per Idea")
        self.scripts_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.scripts_entry = ctk.CTkTextbox(self.input_frame, height=120)
        self.scripts_entry.grid(row=3, column=0, padx=10, pady=5, columnspan=2, sticky="nsew")

        # Images (For Scripts)
        self.images_button = ctk.CTkButton(self.input_frame, text="Select Images Folder", command=self.select_images)
        self.images_button.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.image_path_label = ctk.CTkLabel(self.input_frame, text="No folder selected")
        self.image_path_label.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        # Progress Bar
        self.progress_bar = ctk.CTkProgressBar(self, width=500)
        self.progress_bar.pack(pady=20)
        self.progress_bar.set(0)

        # Start Button
        self.start_button = ctk.CTkButton(self, text="Start Generation", command=self.start_generation)
        self.start_button.pack(pady=10)

        # Status label
        self.status_label = ctk.CTkLabel(self, text="Idle", font=("Arial", 14))
        self.status_label.pack(pady=5)

        # Make widgets stretch
        self.input_frame.grid_columnconfigure(0, weight=1)
        self.input_frame.grid_columnconfigure(1, weight=1)
        self.input_frame.grid_rowconfigure(1, weight=1)
        self.input_frame.grid_rowconfigure(3, weight=1)

    def select_images(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.image_path_label.configure(text=folder_path)
            self.image_folder = folder_path
        else:
            self.image_path_label.configure(text="No folder selected")
            self.image_folder = None

    def start_generation(self):
        user_ideas = self.user_ideas_entry.get("1.0", "end").strip()
        gemini_ideas = self.gemini_ideas_entry.get("1.0", "end").strip()
        scripts = self.scripts_entry.get("1.0", "end").strip()

        if not (user_ideas and gemini_ideas and scripts):
            messagebox.showerror("Missing Info", "Please fill in all fields.")
            return

        self.status_label.configure(text="Starting generation...")
        self.progress_bar.set(0.1)

        # Simulate steps (placeholder logic)
        self.after(1000, lambda: self.update_progress(0.3, "Generating scripts..."))
        self.after(2000, lambda: self.update_progress(0.6, "Generating images or assets..."))
        self.after(3000, lambda: self.update_progress(0.9, "Finalizing video..."))
        self.after(4000, lambda: self.update_progress(1.0, "Completed!"))

    def update_progress(self, value, status):
        self.progress_bar.set(value)
        self.status_label.configure(text=status)

if __name__ == "__main__":
    app = ShortsAutomatorApp()
    app.mainloop()
