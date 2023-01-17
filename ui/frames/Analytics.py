import random
import customtkinter

from ui.components.Display import DisplayComponent
from ui.components.Splitview import SplitviewComponent
from ui.components.List import ListComponent

class AnalyticsFrame(customtkinter.CTkFrame):
    def __init__(self, *args, app, **kwargs):
        super().__init__(*args, **kwargs)

        self.app = app

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.budget_splitview = SplitviewComponent(master=self, app=app)

        self.general_trend_component = DisplayComponent(
            master=self.budget_splitview.left_view,
            app=app,
            text="GENERAL TREND",
            values=categories,
            filter_label="Date",
            filter_callback=self.filter_item_list
        )
        
        self.overall_trend_component = DisplayComponent(
            master=self.budget_splitview.right_view,
            app=app,
            text="OVERALL TREND",
            values=categories,
            filter_callback=self.filter_differences
        )

    def filter_item_list(self, category):
        print("ITEM LIST", category)
    
    def filter_differences(self, category):
        print("DIFFERENCES", category)