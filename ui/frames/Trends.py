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

        categories = [ "All", "Diary", "Meat", "Bakery" ]

        user_categories = self.app.data.all_categories
        user_items = self.app.get_products_of_user()

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
        product_purchases = self.app.data.get_purchases_for_item(product_brand)
        min_year = min([ int(purchase[0]) for purchase in product_purchases ])
        purchase_coordinates = [
            (utils.get_month_index(purchase[1]) + (12 * (int(purchase[0]) % min_year)), purchase[3])
            for purchase in product_purchases
        ]
        print("ITEM TRENDS", purchase_coordinates)

    def filter_category_trends(self, category):
        category_product_brands = self.app.data.get_product_brands_from_category(category)

        monthly_amounts = []

        for product_brand in category_product_brands:
            product_purchases = self.app.data.get_purchases_for_item(product_brand)
            min_year = min([ int(purchase[0]) for purchase in product_purchases ])
            for purchase in product_purchases:
                numerical_month = utils.get_month_index(purchase) + (12 * (int(purchase[0]) % min_year))
                if (numerical_month / len(monthly_amounts)) < 1:
                    monthly_amounts[numerical_month] = purchase[3]
                else:
                    monthly_amounts[numerical_month] += purchase[3]

        category_coordinates = [ (i, monthly_amounts[i]) for i in range(len(monthly_amounts)) ]
        print("CATEGORY TRENDS", category_coordinates)
