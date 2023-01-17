import customtkinter

import utils
from ui.components.Display import DisplayComponent
from ui.components.Splitview import SplitviewComponent
from ui.components.Graph import GraphComponent

class SpendingsFrame(customtkinter.CTkFrame):
    def __init__(self, *args, app, **kwargs):
        super().__init__(*args, **kwargs)

        self.app = app

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        user_dates_desc = app.data.get_purchase_dates()
        user_years_desc = set([ user_date.split()[1] for user_date in user_dates_desc ])

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
        purchases = self.app.data.get_purchases_on_date(f"{utils.get_month_index(month)}", year)

        category_costs = {}

        for purchase in purchases:
            product_brand = self.app.data.get_product_brand_from_id(purchase[2])
            product_type = self.app.get_product_type_from_id(product_brand[2])
            category = product_type[1]

            product_cost = purchase[3] * product_brand[3]
            if not category in category_costs:
                category_costs[category] = product_cost
            else:
                category_costs[category] += product_cost

        chart_fields = [ (category, cost) for category, cost in category_costs.items() ]
        print("CATEGORY COSTS", chart_fields)

    def filter_category_spending(self, compound_date):
        month, year = compound_date.split()
        category_data = self.get_category_data_for(month, year)
        # Create pie chart

        # Generate a new Graph widget and replace the placement of current with this one
    
    def filter_yearly_spending(self, year):
        purchases = self.app.data.get_purchases_on_year(year)

        monthly_costs = []
        for purchase in purchases:
            product_brand = self.app.data.get_product_brand_from_id(purchase[2])
            product_cost = purchase[3] * product_brand[3]
            
            purchase_month_index = utils.get_month_index(purchase[1])
            if purchase_month_index > len(monthly_costs):
                monthly_costs[purchase_month_index] = product_cost
            else:
                monthly_costs[purchase_month_index] += product_cost

        chart_fields = [ (i, monthly_costs[i]) for i in range(len(monthly_costs)) ]
        print("YEARLY COSTS", chart_fields)