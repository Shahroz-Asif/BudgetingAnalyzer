import customtkinter

from ui.components.Display import DisplayComponent
from ui.components.Splitview import SplitviewComponent
from ui.components.Graph import GraphComponent

class SpendingsFrame(customtkinter.CTkFrame):
    def __init__(self, *args, app, **kwargs):
        super().__init__(*args, **kwargs)

        self.app = app

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        categories = [ "All", "Diary", "Meat", "Bakery" ]

        user_years_desc = []
        user_months_desc = []

        user_dates_desc = []

        self.spendings_splitview = SplitviewComponent(master=self, app=app)

        self.category_spending_component = DisplayComponent(
            master=self.spendings_splitview.left_view,
            app=app,
            text="CATEGORY SPENDING",
            values=user_dates_desc,
            filter_label="Date",
            filter_callback=self.filter_category_spending
        )
        
        self.yearly_spending_component = DisplayComponent(
            master=self.spendings_splitview.right_view,
            app=app,
            text="YEARLY SPENDING",
            values=user_years_desc,
            filter_label="Year",
            filter_callback=self.filter_yearly_spending
        )

        self.item_trends_graph = GraphComponent(
            master=self.category_spending_component.display_view,
            app=app
        )

        self.category_trends_graph = GraphComponent(
            master=self.yearly_spending_component.display_view,
            app=app
        )

    def get_category_data_for(self, month, year):
        pass
        # Get data for month and year
        # Organise it into categories
        # For each category, find the total sum of prices

    def filter_category_spending(self, compound_date):
        print("CATEGORY SPENDING", compound_date)
        month, year = compound_date.split()
        category_data = self.get_category_data_for(month, year)
        # Create pie chart

        # Generate a new Graph widget and replace the placement of current with this one
    
    def filter_yearly_spending(self, year):
        print("YEARLY SPENDING", year)
        overall_data = []
        # For year, get all months that exist
        year_months = []

        for month in year_months:
            category_data = self.get_category_data_for(month, year)
            # Not particularly sure how to place this data