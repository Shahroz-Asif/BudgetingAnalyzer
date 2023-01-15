import customtkinter

from ui.config import frames, labels

class MenuComponent(customtkinter.CTkFrame):
    def __init__(self, *args, app, title, values, textvariable, **kwargs):
        super().__init__(*args, **frames["blank"]["design"], **frames["window"]["design"], **kwargs)
        
        self.app = app

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.title_label = customtkinter.CTkLabel(master=self, text=title, **labels["heading"]["design"])
        self.title_label.grid(**labels["heading"]["placement"])

        self.option_menu = customtkinter.CTkOptionMenu(
            master=self,
            values=values,
            variable=textvariable
        )
        self.option_menu.grid(row=1, column=0, sticky="wes")
