import customtkinter

from ui.config import frames, labels, menus

class DisplayComponent(customtkinter.CTkFrame):
    def __init__(self, *args, app, text, values, filter_label, filter_callback, **kwargs):
        super().__init__(*args, **frames["blank"]["design"], **frames["window"]["design"], **kwargs)

        self.app = app

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.component_label = customtkinter.CTkLabel(master=self, text=text, **labels["component"]["design"])
        self.component_label.grid(**labels["component"]["placement"])

        self.sort_label = customtkinter.CTkLabel(master=self, text=f"Select {filter_label}:", **labels["sort"]["design"])
        self.sort_label.grid(**labels["sort"]["placement"])

        # Dropdown
        self.category_menu = customtkinter.CTkOptionMenu(
            master=self,
            values=values,
            command=filter_callback,
            **menus["category"]["design"]
        )
        self.category_menu.grid(**menus["category"]["placement"])

        # Data Component
        self.display_view = customtkinter.CTkFrame(master=self, **frames["blank"]["design"], **frames["split"]["design"])
        self.display_view.grid_rowconfigure(0, weight=1)
        self.display_view.grid_columnconfigure(0, weight=1)
        self.display_view.grid(row=2, column=0, columnspan=2, pady=10, sticky="wes")
        
        self.grid(**frames["blank"]["placement"], **frames["window"]["placement"])