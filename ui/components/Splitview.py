import customtkinter

from ui.config import frames

class SplitviewComponent(customtkinter.CTkFrame):
    def __init__(self, *args, app, weight_left=1, weight_right=1, **kwargs):
        super().__init__(*args, **frames["blank"]["design"], **frames["window"]["design"], **kwargs)

        self.app = app

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=weight_left)
        self.grid_columnconfigure(1, weight=weight_right)

        self.left_view = customtkinter.CTkFrame(master=self, **frames["blank"]["design"], **frames["split"]["design"])
        self.left_view.grid(column=0, **frames["split"]["placement"])
        
        self.right_view = customtkinter.CTkFrame(master=self, **frames["blank"]["design"], **frames["split"]["design"])
        self.right_view.grid(column=1, **frames["split"]["placement"])

        self.grid(**frames["blank"]["placement"], **frames["window"]["placement"])
