import customtkinter

import utils
from ui.components.Display import DisplayComponent
from ui.components.Splitview import SplitviewComponent
from ui.components.Graph import GraphComponent

class TrendsFrame(customtkinter.CTkFrame):
    def __init__(self, *args, app, **kwargs):
        super().__init__(*args, **kwargs)

        self.app = app

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        user_categories = self.app.data.all_categories
        user_items = self.app.data.get_products_of_user()

        self.trends_splitview = SplitviewComponent(master=self, app=app)

        self.item_trends_component = DisplayComponent(
            master=self.trends_splitview.left_view,
            app=app,
            text="ITEM TRENDS",
            values=user_items,
            filter_label="Item",
            filter_callback=self.filter_item_trends
        )

        self.category_trends_component = DisplayComponent(
            master=self.trends_splitview.right_view,
            app=app,
            text="CATEGORY TRENDS",
            values=user_categories,
            filter_label="Category",
            filter_callback=self.filter_category_trends
        )

        self.item_trends_graph = GraphComponent(master=self.item_trends_component.display_view, app=app)
        self.category_trends_graph = GraphComponent(master=self.category_trends_component.display_view, app=app)

        self.filter_item_trends(user_items[0])
        self.filter_category_trends(user_categories[0])

    def filter_item_trends(self, product_brand):
        product_purchases = self.app.data.get_purchases_of_item(product_brand)
        min_year = min([ int(purchase[0]) for purchase in product_purchases ])
        purchase_coordinates = [
            [int(purchase[1]) + (12 * (int(purchase[0]) % min_year)), purchase[3]]
            for purchase in product_purchases
        ]
        self.item_trends_graph.plot_figure(purchase_coordinates)

    def filter_category_trends(self, category):
        category_product_brands = self.app.data.get_product_brands_of_category(category)

        monthly_amounts = {}

        for product_brand in category_product_brands:
            product_purchases = self.app.data.get_purchases_of_item(product_brand[1])
            min_year = min([ int(purchase[0]) for purchase in product_purchases ])
            for purchase in product_purchases:
                numerical_month = int(purchase[1]) + (12 * (int(purchase[0]) % min_year))
                if numerical_month not in monthly_amounts:
                    monthly_amounts[numerical_month] = purchase[3]
                else:
                    monthly_amounts[numerical_month] += purchase[3]

        category_coordinates = [ [i, amount] for i, amount in monthly_amounts.items() ]
        self.category_trends_graph.plot_figure(category_coordinates)
