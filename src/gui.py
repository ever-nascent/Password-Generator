import customtkinter as ctk
import pyperclip
from password_generator import create_password

DEFAULT_PASSWORD_LENGTH = 20
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 32

class PasswordGeneratorApp:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.setup_window()
        self.create_variables()
        self.create_widgets()

    def setup_window(self):
        self.root.title("Password Generator")
        self.root.geometry("500x650")
        self.root.resizable(False, False)

        # Try to set icon, but don't fail if it doesn't exist
        try:
            self.root.iconbitmap('./assets/icon.ico')
        except:
            pass

    def create_variables(self):
        self.use_lower = ctk.BooleanVar(value=True)
        self.use_upper = ctk.BooleanVar(value=True)
        self.use_numbers = ctk.BooleanVar(value=True)
        self.use_symbols = ctk.BooleanVar(value=True)

    def create_widgets(self):
        # Main container with padding
        main_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=30, pady=30)

        # Title
        title_label = ctk.CTkLabel(
            main_frame,
            text="Password Generator",
            font=("Helvetica", 28, "bold")
        )
        title_label.pack(pady=(0, 30))

        # Password display frame
        password_frame = ctk.CTkFrame(main_frame)
        password_frame.pack(fill="x", pady=(0, 20))

        initial_password = create_password(
            DEFAULT_PASSWORD_LENGTH,
            self.use_lower.get(),
            self.use_upper.get(),
            self.use_numbers.get(),
            self.use_symbols.get()
        )

        self.password_label = ctk.CTkLabel(
            password_frame,
            text=initial_password,
            font=("Courier", 18, "bold"),
            wraplength=420
        )
        self.password_label.pack(padx=20, pady=20)

        # Buttons frame
        buttons_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        buttons_frame.pack(fill="x", pady=(0, 20))

        copy_button = ctk.CTkButton(
            buttons_frame,
            text="Copy Password",
            command=self.copy_to_clipboard,
            font=("Helvetica", 14),
            height=40,
            corner_radius=10
        )
        copy_button.pack(side="left", expand=True, fill="x", padx=(0, 10))

        regenerate_button = ctk.CTkButton(
            buttons_frame,
            text="Regenerate",
            command=self.regenerate_password,
            font=("Helvetica", 14),
            height=40,
            corner_radius=10
        )
        regenerate_button.pack(side="left", expand=True, fill="x", padx=(10, 0))

        # Length slider section
        length_frame = ctk.CTkFrame(main_frame)
        length_frame.pack(fill="x", pady=(0, 20))

        length_title = ctk.CTkLabel(
            length_frame,
            text="Password Length",
            font=("Helvetica", 16, "bold")
        )
        length_title.pack(pady=(15, 5))

        self.length_value_label = ctk.CTkLabel(
            length_frame,
            text=str(DEFAULT_PASSWORD_LENGTH),
            font=("Helvetica", 24, "bold")
        )
        self.length_value_label.pack(pady=(0, 10))

        self.password_length_slider = ctk.CTkSlider(
            length_frame,
            from_=MIN_PASSWORD_LENGTH,
            to=MAX_PASSWORD_LENGTH,
            number_of_steps=MAX_PASSWORD_LENGTH - MIN_PASSWORD_LENGTH,
            command=self.on_slider_change
        )
        self.password_length_slider.set(DEFAULT_PASSWORD_LENGTH)
        self.password_length_slider.pack(fill="x", padx=20, pady=(0, 15))

        # Options section
        options_frame = ctk.CTkFrame(main_frame)
        options_frame.pack(fill="x")

        options_title = ctk.CTkLabel(
            options_frame,
            text="Character Options",
            font=("Helvetica", 16, "bold")
        )
        options_title.pack(pady=(15, 10))

        # Checkboxes
        self.lowercase_checkbox = ctk.CTkCheckBox(
            options_frame,
            text="Lowercase (a-z)",
            variable=self.use_lower,
            command=self.regenerate_password,
            font=("Helvetica", 14)
        )
        self.lowercase_checkbox.pack(pady=5, padx=25, anchor="w")

        self.uppercase_checkbox = ctk.CTkCheckBox(
            options_frame,
            text="Uppercase (A-Z)",
            variable=self.use_upper,
            command=self.regenerate_password,
            font=("Helvetica", 14)
        )
        self.uppercase_checkbox.pack(pady=5, padx=25, anchor="w")

        self.numbers_checkbox = ctk.CTkCheckBox(
            options_frame,
            text="Numbers (0-9)",
            variable=self.use_numbers,
            command=self.regenerate_password,
            font=("Helvetica", 14)
        )
        self.numbers_checkbox.pack(pady=5, padx=25, anchor="w")

        self.symbols_checkbox = ctk.CTkCheckBox(
            options_frame,
            text="Symbols (!@#$%...)",
            variable=self.use_symbols,
            command=self.regenerate_password,
            font=("Helvetica", 14)
        )
        self.symbols_checkbox.pack(pady=(5, 15), padx=25, anchor="w")

    def on_slider_change(self, value):
        length = int(value)
        self.length_value_label.configure(text=str(length))
        self.regenerate_password()

    def regenerate_password(self):
        password_length = int(self.password_length_slider.get())
        password = create_password(
            password_length,
            self.use_lower.get(),
            self.use_upper.get(),
            self.use_numbers.get(),
            self.use_symbols.get()
        )
        self.password_label.configure(text=password)

    def copy_to_clipboard(self):
        password = self.password_label.cget("text")
        pyperclip.copy(password)

    def run(self):
        self.root.mainloop()
