import customtkinter

from ui.components.Display import DisplayComponent
from ui.components.Splitview import SplitviewComponent
from ui.components.Graph import GraphComponent

class TrendsFrame(customtkinter.CTkFrame):
    def __init__(self, *args, app, **kwargs):
        super().__init__(*args, **kwargs)

        self.app = app

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        categories = [ "All", "Diary", "Meat", "Bakery" ]

        user_items = []
        user_categories = []

        self.trends_splitview = SplitviewComponent(master=self, app=app)

        self.item_trends_component = DisplayComponent(
            master=self.trends_splitview.left_view,
            app=app,
            text="ITEM TRENDS",
            values=categories,
            filter_label="Item",
            filter_callback=self.filter_item_trends
        )

        self.category_trends_component = DisplayComponent(
            master=self.trends_splitview.right_view,
            app=app,
            text="CATEGORY TRENDS",
            values=categories,
            filter_label="Category",
            filter_callback=self.filter_category_trends
        )

        self.item_trends_graph = GraphComponent(master=self.item_trends_component.display_view, app=app)
        self.category_trends_graph = GraphComponent(master=self.category_trends_component.display_view, app=app)

    def filter_item_trends(self, product_brand):
        print("ITEM TRENDS", product_brand)
        # Get all entries of the selected item type
        # Generate smoothened graph

    def filter_category_trends(self, category):
        print("CATEGORY TRENDS", category)
        # Get all entries of items
        # Get Products that belong to category
        # months_categories = [  ]
        # For all months, sum the amount numbers of products with the same categories
