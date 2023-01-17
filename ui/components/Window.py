import customtkinter

from ui.config import frames, labels

class WindowComponent(customtkinter.CTkFrame):
    def __init__(self, *args, app, label_text, body_frame_class, is_main, **kwargs):
        super().__init__(*args, **frames["blank"]["design"], **frames["window"]["design"], **kwargs)

        self.app = app

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=100)

        self.title_type = "title" if is_main else "subtitle"
        self.title_label = customtkinter.CTkLabel(master=self, **labels[self.title_type]["design"], text=label_text)
        self.title_label.grid(**labels[self.title_type]["placement"])

        self.set_body_frame(body_frame_class)

    def set_body_frame(self, body_frame_class):
        self.body_frame = body_frame_class(master=self, app=self.app, **frames["body"]["design"])
        self.body_frame.grid_forget()
        self.body_frame.grid(**frames["body"]["placement"])