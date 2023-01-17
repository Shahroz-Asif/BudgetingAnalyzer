import tkinter
import customtkinter

import utils
from ui.config import buttons, labels, frames

from ui.components.Display import DisplayComponent
from ui.components.Splitview import SplitviewComponent
from ui.components.List import ListComponent
from ui.components.Menu import MenuComponent
from ui.components.Entry import EntryComponent

available_years = [ f"{year}" for year in range(2023, 2010, -1) ]
available_months = [ "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC" ]

class ModifyFrame(customtkinter.CTkFrame):
    loaded_purchase_id = None
    loaded_purchase = None
    selected_product_brand = None
    
    def __init__(self, *args, app, **kwargs):
        super().__init__(*args, **kwargs)

        self.app = app

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        user_dates_desc = app.data.get_purchase_dates()

        self.selected_purchases = []

        self.year_value = customtkinter.Variable(value="Select...")
        self.month_value = customtkinter.Variable(value="Select...")
        self.category_value = customtkinter.Variable(value="Select...")
        self.product_value = customtkinter.Variable(value="Select...")
        self.amount_value = tkinter.StringVar(value="")

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
            columns=["Item Names"],
            rows=[],
            height=12
        )

        self.load_button = customtkinter.CTkButton(
            master=left_view,
            text="LOAD",
            command=self.load_item,
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
            values=app.data.all_categories,
            textvariable=self.category_value,
            selection_callback=self.set_menu_entries_of_category
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
            values=[],
            textvariable=self.product_value,
            selection_callback=self.pick_product_entry
        )
        self.product_menu.grid(row=6, column=0)

        self.cost_frame = customtkinter.CTkFrame(master=right_view, **frames["blank"]["design"])
        self.cost_frame.grid_rowconfigure(0, weight=1)
        self.cost_frame.grid_rowconfigure(1, weight=1)
        self.cost_frame.grid_columnconfigure(0, weight=1)
        self.cost_frame.grid(row=6, column=1)

        self.cost_label = customtkinter.CTkLabel(
            master=self.cost_frame,
            text="",
            **labels["heading"]["design"]
        )
        self.cost_label.grid(row=0, column=0)
        
        self.cost_text = customtkinter.Variable(value="Please enter AMOUNT first!")
        self.cost_result_label = customtkinter.CTkLabel(
            master=self.cost_frame,
            textvariable=self.cost_text,
            text="",
            wraplength=100,
            **labels["small_text"]["design"]
        )
        self.cost_result_label.grid(row=1, column=0)

        self.separator_frame = customtkinter.CTkFrame(master=right_view, **frames["separator"]["design"])
        self.separator_frame.grid(row=7, columnspan=2, **frames["separator"]["placement"])

        self.delete_button = customtkinter.CTkButton(
            master=right_view,
            text="DELETE",
            command=self.delete_entry,
            **buttons["small"]["design"]
        )
        self.delete_button.grid(row=8, column=0, columnspan=1)
        
        self.save_button = customtkinter.CTkButton(
            master=right_view,
            text="SAVE",
            command=self.insert_or_update_purchase,
            **buttons["small"]["design"]
        )
        self.save_button.grid(row=8, column=1)

        # Show entries of picked date
        self.filter_item_list(user_dates_desc[0])

    def filter_item_list(self, compound_date):
        month, year = compound_date.split()

        self.selected_purchases = self.app.data.get_purchases_on_date(utils.get_month_index(month), year)
        selected_product_ids = [ selected_purchase[2] for selected_purchase in self.selected_purchases ]
        self.selected_product_names = [
            self.app.data.get_product_brand_from_id(selected_product_id)[1] for selected_product_id in selected_product_ids
        ]

        self.item_list_view.put_entries(self.selected_product_names)

        # Year, Month, Amount | Category, ProductName

    def load_item(self):
        selected_row = self.item_list_view.focus()
        row_details = self.item_list_view.item(selected_row)
        brand_name = " ".join(row_details["values"])

        if brand_name == None or brand_name == "":
            return

        purchase_index = self.selected_product_names.index(brand_name)
        purchase_entry = self.selected_purchases[purchase_index]
        purchase_year, purchase_month, product_id, unit_amount, purchase_id = purchase_entry

        product_brand = self.app.data.get_product_brand_from_id(product_id)
        product_category = self.app.data.get_product_type_from_id(product_brand[2])[1]

        self.loaded_purchase = purchase_entry
        self.loaded_purchase_id = purchase_id

        self.year_value.set(int(purchase_year))
        self.month_value.set(utils.get_month(int(purchase_month)))
        self.category_value.set(product_category)
        self.product_value.set(brand_name)
        self.amount_entry.entry_menu.insert(0, str(int(unit_amount)))

        self.load_button.configure(text="UNLOAD", command=self.unload_item)

    def reset_input_values(self):
        self.year_value.set("Select...")
        self.month_value.set("Select...")
        self.category_value.set("Select...")
        self.product_value.set("Select...")
        self.amount_entry.entry_menu.delete(0, 100)

    def unload_item(self):
        self.loaded_purchase_id = None
        self.loaded_purchase = None
        self.reset_input_values()

        self.load_button.configure(text="LOAD", command=self.load_item)

    def set_menu_entries_of_category(self, category):
        if category == "Select...":
            return
        
        self.product_brand_entries = self.app.data.get_product_brands_of_category(category)
        product_brand_names = [ product_brand_entry[1] for product_brand_entry in self.product_brand_entries ]

        self.product_menu.option_menu.configure(values=product_brand_names)

    def pick_product_entry(self, product_brand):
        for product_brand_entry in self.product_brand_entries:
            if product_brand_entry[1] == product_brand:
                self.selected_product_brand = product_brand_entry

                try:
                    unit_price = self.selected_product_brand[3]
                    unit_amount = int(self.amount_entry.entry_menu.get())
                    self.calculate_price(unit_amount, unit_price)
                except:
                    pass
                finally:
                    break

    def calculate_price_on_amount_change(self):
        if self.selected_product_brand == None:
            return
        
        try:
            unit_price = self.selected_product_brand[3]
            unit_amount = int(self.amount_entry.entry_menu.get())
            self.calculate_price(unit_amount, unit_price)
        except:
            return

    def calculate_price(self, unit_amount, unit_price):
        price = unit_amount * unit_price
        self.cost_text.set(price)

    def delete_entry(self):
        if self.loaded_purchase_id == None or self.loaded_purchase == None:
            return
        
        purchase = self.loaded_purchase
        
        self.app.data.delete_purchase_by_id(self.loaded_purchase_id)
        self.filter_item_list(f"{utils.get_month(int(purchase[1]))} {purchase[0]}")
        self.reset_input_values()
        self.unload_item()

    def insert_or_update_purchase(self):
        if self.selected_product_brand == None:
            return
        is_insert = self.loaded_purchase_id == None

        year = self.year_value.get()
        month = utils.get_month_index(self.month_value.get())
        amount = self.amount_entry.entry_menu.get()
        product_id = self.selected_product_brand[0]

        if is_insert:
            self.app.data.create_purchase_entry(year, month, product_id, amount)
        else:
            self.app.data.update_purchase_entry(self.loaded_purchase_id, year, month, product_id, amount)

        self.filter_item_list(f"{utils.get_month(month)} {year}")
        self.reset_input_values()