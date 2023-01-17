import customtkinter

from ui.config import frames, labels, buttons

class WelcomeFrame(customtkinter.CTkFrame):
    def __init__(self, *args, app, **kwargs):
        super().__init__(*args, **kwargs)

        self.app = app

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=3)
        self.grid_rowconfigure(3, weight=2)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=2)
        self.grid_rowconfigure(6, weight=3)

        self.welcome_label = customtkinter.CTkLabel(master=self, **labels["welcome"]["design"])
        self.welcome_label.grid(**labels["welcome"]["placement"])

        self.instruction_label = customtkinter.CTkLabel(master=self, **labels["instruction"]["design"])
        self.instruction_label.grid(**labels["instruction"]["placement"])

        self.import_button = customtkinter.CTkButton(
            master=self,
            command=app.data.pick_purchases_database,
            **buttons["import"]["design"]
        )
        self.import_button.grid(**buttons["import"]["placement"])
        self.modify_button = customtkinter.CTkButton(master=self, command=app.windows.open_modify, **buttons["modify"]["design"])
        self.modify_button.grid(**buttons["modify"]["placement"])

        self.loaded_label = customtkinter.CTkLabel(master=self, **labels["loaded"]["design"])
        self.loaded_label.grid(**labels["loaded"]["placement"])

        self.separator_frame = customtkinter.CTkFrame(master=self, **frames["separator"]["design"])
        self.separator_frame.grid(row=4, columnspan=2, **frames["separator"]["placement"])

        self.proceed_label = customtkinter.CTkLabel(master=self, **labels["proceed"]["design"])
        self.proceed_label.grid(**labels["proceed"]["placement"])

        self.analyze_button = customtkinter.CTkButton(
            master=self,
            command=app.windows.open_analysis,
            **buttons["generate"]["design"]
        )
        self.analyze_button.grid(**buttons["generate"]["placement"])

    def generate_data(self):
        self.app.windows.main.display_result_frame()
