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
        user_years_desc = list(set([ int(user_date.split()[1]) for user_date in user_dates_desc ]))
        user_years_desc.sort()
        user_years_desc.reverse()
        user_years_desc = [ str(year) for year in user_years_desc ]

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

        self.category_spending_graph = GraphComponent(
            master=self.category_spending_component.display_view,
            app=app
        )

        self.yearly_spending_graph = GraphComponent(
            master=self.yearly_spending_component.display_view,
            app=app
        )

        self.filter_category_spending(user_dates_desc[0])
        self.filter_yearly_spending(user_years_desc[0])

    def filter_category_spending(self, compound_date):
        month, year = compound_date.split()
        purchases = self.app.data.get_purchases_on_date(f"{utils.get_month_index(month)}", year)

        category_costs = {}

        for purchase in purchases:
            product_brand = self.app.data.get_product_brand_from_id(purchase[2])
            product_type = self.app.data.get_product_type_from_id(product_brand[2])
            category = product_type[1]

            product_cost = purchase[3] * product_brand[3]
            if not category in category_costs:
                category_costs[category] = product_cost
            else:
                category_costs[category] += product_cost

        chart_labels = [ category for category in category_costs.keys() ]
        chart_sizes = [ size for size in category_costs.values() ]
        self.category_spending_graph.plot_pie(chart_labels, chart_sizes)
    
    def filter_yearly_spending(self, year):
        purchases = self.app.data.get_purchases_on_year(year)

        monthly_costs = {}
        for purchase in purchases:
            product_brand = self.app.data.get_product_brand_from_id(purchase[2])
            product_cost = purchase[3] * product_brand[3]
            
            purchase_month_index = int(purchase[1])
            if purchase_month_index not in monthly_costs:
                monthly_costs[purchase_month_index] = product_cost
            else:
                monthly_costs[purchase_month_index] += product_cost

        chart_labels = [ category for category in monthly_costs.keys() ]
        chart_sizes = [ size for size in monthly_costs.values() ]
        self.yearly_spending_graph.plot_bar(chart_labels, chart_sizes)