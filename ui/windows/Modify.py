import customtkinter

from ui.config import constants, windows, frames, labels

from ui.components.Window import WindowComponent
from ui.frames.Modify import ModifyFrame

class ModifyWindow(customtkinter.CTk):
    def __init__(self, app):
        super().__init__()

        self.app = app

        self.title(windows["main"]["title"])
        self.minsize(constants["x"], constants["y"])
        self.maxsize(constants["x"], constants["y"])

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.window_component = WindowComponent(
            master=self,
            app=app,
            label_text="Add or Modify Information",
            body_frame_class=ModifyFrame,
            is_main=False
        )
        self.window_component.grid(**frames["blank"]["placement"], **frames["window"]["placement"])