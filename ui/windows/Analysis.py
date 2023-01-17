import customtkinter

from ui.config import constants, windows, frames, tabviews

from ui.components.Window import WindowComponent
from ui.frames.Spendings import SpendingsFrame
from ui.frames.Trends import TrendsFrame
from ui.frames.Analytics import AnalyticsFrame

class AnalysisWindow(customtkinter.CTk):
    def __init__(self, app):
        super().__init__()

        self.app = app

        self.title(windows["main"]["title"])
        self.minsize(constants["x"], constants["y"])
        self.maxsize(constants["x"], constants["y"])

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.analysis_tabview = customtkinter.CTkTabview(master=self, **tabviews["analysis"]["design"])
        self.analysis_tabview.grid(**tabviews["analysis"]["placement"])

        self.spendings_tab = self.analysis_tabview.add("Spendings")
        self.trends_tab = self.analysis_tabview.add("Trends")

        self.spendings_tab.grid_rowconfigure(0, weight=1)
        self.spendings_tab.grid_columnconfigure(0, weight=1)
        self.spendings_window_component = WindowComponent(
            master=self.spendings_tab,
            app=app,
            label_text="Spendings",
            body_frame_class=SpendingsFrame,
            is_main=False
        )
        self.spendings_window_component.grid_rowconfigure(0, weight=1)
        self.spendings_window_component.grid_columnconfigure(0, weight=1)
        self.spendings_window_component.grid(**frames["blank"]["placement"], **frames["window"]["placement"])

        self.trends_tab.grid_rowconfigure(0, weight=1)
        self.trends_tab.grid_columnconfigure(0, weight=1)
        self.trends_window_component = WindowComponent(
            master=self.trends_tab,
            app=app,
            label_text="Trends",
            body_frame_class=TrendsFrame,
            is_main=False
        )
        self.trends_window_component.grid_rowconfigure(0, weight=1)
        self.trends_window_component.grid_columnconfigure(0, weight=1)
        self.trends_window_component.grid(**frames["blank"]["placement"], **frames["window"]["placement"])