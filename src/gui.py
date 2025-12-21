import tkinter as tk
import pyperclip
from password_generator import create_password

DEFAULT_PASSWORD_LENGTH = 20
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 32

class PasswordGeneratorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.create_variables()
        self.create_widgets()

    def setup_window(self):
        self.root.title("Password Generator")
        self.root.iconbitmap('./assets/icon.ico')
        self.root.geometry("700x300")
        self.root.configure(bg="#302c2c")
        self.root.resizable(False, False)

    def create_variables(self):
        self.use_lower = tk.BooleanVar(value=True)
        self.use_upper = tk.BooleanVar(value=True)
        self.use_numbers = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)

    def create_widgets(self):
        initial_password = create_password(
            DEFAULT_PASSWORD_LENGTH,
            self.use_lower.get(),
            self.use_upper.get(),
            self.use_numbers.get(),
            self.use_symbols.get()
        )

        self.password_label = tk.Label(
            self.root,
            font=("Helvetica", 20),
            text=initial_password,
            fg="#FFFFFF",
            bg=self.root["bg"]
        )
        self.password_label.pack()

        self.password_length_slider = tk.Scale(
            self.root,
            from_=MIN_PASSWORD_LENGTH,
            to=MAX_PASSWORD_LENGTH,
            orient=tk.HORIZONTAL,
            bg=self.root["bg"],
            highlightthickness=0,
            length=250,
            command=lambda value: self.regenerate_password()
        )
        self.password_length_slider.set(DEFAULT_PASSWORD_LENGTH)
        self.password_length_slider.pack()

        copy_password_button = tk.Button(
            self.root,
            text="Copy Password",
            command=self.copy_to_clipboard
        )
        copy_password_button.pack()

        new_password_button = tk.Button(
            self.root,
            text="Regenerate Password",
            command=self.regenerate_password
        )
        new_password_button.pack()

        use_lower_checkbox = tk.Checkbutton(
            self.root,
            text="Include Lowercase Characters",
            variable=self.use_lower,
            command=self.regenerate_password
        )
        use_lower_checkbox.pack()

        use_upper_checkbox = tk.Checkbutton(
            self.root,
            text="Include Uppercase Characters",
            variable=self.use_upper,
            command=self.regenerate_password
        )
        use_upper_checkbox.pack()

        use_numbers_checkbox = tk.Checkbutton(
            self.root,
            text="Include Numbers",
            variable=self.use_numbers,
            command=self.regenerate_password
        )
        use_numbers_checkbox.pack()

        use_symbols_checkbox = tk.Checkbutton(
            self.root,
            text="Include Symbols",
            variable=self.use_symbols,
            command=self.regenerate_password
        )
        use_symbols_checkbox.pack()

    def regenerate_password(self):
        password_length = self.password_length_slider.get()
        password = create_password(
            password_length,
            self.use_lower.get(),
            self.use_upper.get(),
            self.use_numbers.get(),
            self.use_symbols.get()
        )
        self.password_label.config(text=password)

    def copy_to_clipboard(self):
        password = self.password_label.cget("text")
        pyperclip.copy(password)

    def run(self):
        self.root.mainloop()
