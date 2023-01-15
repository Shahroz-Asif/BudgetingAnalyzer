import customtkinter
from Application import Application

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

if __name__ == "__main__":
    app = Application()
    app.mainloop()