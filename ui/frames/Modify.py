import customtkinter

from ui.config import buttons, labels, frames

from ui.components.Display import DisplayComponent
from ui.components.Splitview import SplitviewComponent
from ui.components.List import ListComponent
from ui.components.Menu import MenuComponent
from ui.components.Entry import EntryComponent

available_years = [ f"{year}" for year in range(2023, 2010, -1) ]
available_months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

class ModifyFrame(customtkinter.CTkFrame):
    def __init__(self, *args, app, **kwargs):
        super().__init__(*args, **kwargs)

        self.app = app

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Years descending
        # Months descending
        user_dates_desc = []

        categories = [ "All", "Diary", "Meat", "Bakery" ]
        products = []

        self.year_value = customtkinter.Variable(value="Select...")
        self.month_value = customtkinter.Variable(value="Select...")
        self.category_value = customtkinter.Variable(value="Select...")
        self.product_value = customtkinter.Variable(value="Select...")
        self.amount_value = customtkinter.Variable(value="Select...")

        self.modify_splitview = SplitviewComponent(master=self, app=app, weight_right=4) 
        left_view = self.modify_splitview.left_view
        right_view = self.modify_splitview.right_view

        right_view.grid_columnconfigure(0, weight=1)
        right_view.grid_columnconfigure(1, weight=1)
        right_view.grid_rowconfigure(0, weight=1)
        right_view.grid_rowconfigure(1, weight=1)
        right_view.grid_rowconfigure(2, weight=1)
        right_view.grid_rowconfigure(3, weight=1)
        right_view.grid_rowconfigure(4, weight=1)
        right_view.grid_rowconfigure(5, weight=1)
        right_view.grid_rowconfigure(6, weight=1)
        right_view.grid_rowconfigure(7, weight=1)
        right_view.grid_rowconfigure(8, weight=1)

        self.item_list_component = DisplayComponent(
            master=left_view,
            app=app,
            text="ITEM LIST",
            values=user_dates_desc,
            filter_label="Date",
            filter_callback=self.filter_item_list
        )

        self.item_list_view = ListComponent(
            master=self.item_list_component.display_view,
            app=app,
            columns=["Category Names"],
            rows=[ [ category ] for category in categories[1:] ],
            height=12
        )

        self.load_button = customtkinter.CTkButton(
            master=left_view,
            text="LOAD",
            **buttons["big"]["design"]
        )
        self.load_button.grid(row=1, column=0, sticky="wes")

        step_a_text = "Step 1: Specify Year and Month"
        self.step_a_label = customtkinter.CTkLabel(master=right_view, text=step_a_text, **labels["component"]["design"])
        self.step_a_label.grid(row=0, column=0, columnspan=2)
        
        step_a_describe_text = "Selet a year and month of the product you are adding"
        self.step_a_describe_label = customtkinter.CTkLabel(
            master=right_view,
            text=step_a_describe_text,
            wraplength=300,
            **labels["small_text"]["design"]
        )
        self.step_a_describe_label.grid(row=1, column=0, columnspan=2)
        
        self.year_menu = MenuComponent(
            master=right_view,
            app=app,
            title="YEAR",
            values=available_years,
            textvariable=self.year_value
        )
        self.year_menu.grid(row=2, column=0)
        
        self.month_menu = MenuComponent(
            master=right_view,
            app=app,
            title="MONTH",
            values=available_months,
            textvariable=self.month_value
        )
        self.month_menu.grid(row=2, column=1)

        step_b_text = "Step 2: Modify Item Details"
        self.step_b_label = customtkinter.CTkLabel(master=right_view, text=step_b_text, **labels["component"]["design"])
        self.step_b_label.grid(row=3, column=0, columnspan=2)

        step_b_describe_text = "Add or modify items to the provided month and year"
        self.step_b_describe_label = customtkinter.CTkLabel(master=right_view, text=step_b_describe_text, **labels["small_text"]["design"])
        self.step_b_describe_label.grid(row=4, column=0, columnspan=2)

        self.category_menu = MenuComponent(
            master=right_view,
            app=app,
            title="CATEGORY",
            values=categories,
            textvariable=self.category_value
        )
        self.category_menu.grid(row=5, column=0)
        
        self.amount_entry = EntryComponent(
            master=right_view,
            app=app,
            title="AMOUNT (in units)",
            placeholder="Enter amount...",
            textvariable=self.amount_value
        )
        self.amount_entry.grid(row=5, column=1)
        
        self.product_menu = MenuComponent(
            master=right_view,
            app=app,
            title="PRODUCT",
            values=products,
            textvariable=self.product_value
        )
        self.product_menu.grid(row=6, column=0)

        self.cost_frame = customtkinter.CTkFrame(master=right_view, **frames["blank"]["design"])
        self.cost_frame.grid_rowconfigure(0, weight=1)
        self.cost_frame.grid_rowconfigure(1, weight=1)
        self.cost_frame.grid_columnconfigure(0, weight=1)
        self.cost_frame.grid(row=6, column=1)

        self.cost_label = customtkinter.CTkLabel(
            master=self.cost_frame,
            text="ESTIMATED COST",
            **labels["heading"]["design"]
        )
        self.cost_label.grid(row=0, column=0)
        
        self.cost_default_text = "Please enter AMOUNT first!"
        self.cost_result_label = customtkinter.CTkLabel(
            master=self.cost_frame,
            text=self.cost_default_text,
            wraplength=100,
            **labels["small_text"]["design"]
        )
        self.cost_result_label.grid(row=1, column=0)

        self.separator_frame = customtkinter.CTkFrame(master=right_view, **frames["separator"]["design"])
        self.separator_frame.grid(row=7, columnspan=2, **frames["separator"]["placement"])

        self.delete_button = customtkinter.CTkButton(
            master=right_view,
            text="DELETE",
            **buttons["small"]["design"]
        )
        self.delete_button.grid(row=8, column=0, columnspan=1)
        
        self.save_button = customtkinter.CTkButton(
            master=right_view,
            text="SAVE",
            **buttons["small"]["design"]
        )
        self.save_button.grid(row=8, column=1)


    def filter_item_list(self, compound_date):
        print("ITEM SAVINGS", compound_date)
        month, year = compound_date.split()

        # Filter items that have corresponding month and year
        self.item_list_view