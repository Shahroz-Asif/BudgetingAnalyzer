import customtkinter

from ui.config import constants, windows, frames, labels

from ui.components.Window import WindowComponent
from ui.frames.Welcome import WelcomeFrame
from ui.frames.Result import ResultFrame

class MainWindow(customtkinter.CTk):
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
            label_text=windows["main"]["title"],
            body_frame_class=WelcomeFrame,
            is_main=True
        )
        self.window_component.grid(**frames["blank"]["placement"], **frames["window"]["placement"])

    def display_result_frame(self):
        is_modify_open = self.app.state.modify_window_open
        if is_modify_open:
            return
        
        self.window_component.set_body_frame(ResultFrame)