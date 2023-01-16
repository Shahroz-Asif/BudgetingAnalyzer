from tkinter.filedialog import askopenfilename

from ui.config import constants
from ui.windows.Main import MainWindow
from ui.windows.Modify import ModifyWindow
from ui.windows.Analysis import AnalysisWindow

class ApplicationState:
    sufficient_data = False
    generating = False
    modify_window_open = False
    analysis_window_open = False
    descriptive_opened = False
    purchases_opened = False
    purchases_database = "INTERNAL.accdb"
    descriptive_database = "DESCRIPTIVE.accdb"

class Windows:
    def __init__(self, app):
        self.app = app

    def create_main(self):
        self.main = MainWindow(app=self.app)

    def open_modify(self):
        are_windows_open = self.app.state.analysis_window_open or self.app.state.modify_window_open
        if are_windows_open:
            return

        self.modify = ModifyWindow(app=self.app)
        self.modify.wm_protocol("WM_DELETE_WINDOW", self.close_modify)
        self.modify.geometry(f'{constants["x"]}x{constants["y"]}')
        self.app.state.modify_window_open = not are_windows_open

    def close_modify(self):
        is_modify_open = self.app.state.modify_window_open
        if not is_modify_open:
            return

        self.modify.destroy()
        self.app.state.modify_window_open = False

    def open_analysis(self):
        are_windows_open = self.app.state.analysis_window_open or self.app.state.modify_window_open
        if are_windows_open:
            return

        self.analysis = AnalysisWindow(app=self.app)
        self.analysis.wm_protocol("WM_DELETE_WINDOW", self.close_analysis)
        self.analysis.geometry(f'{constants["x"]}x{constants["y"]}')
        self.app.state.analysis_window_open = not are_windows_open

    def close_analysis(self):
        is_analysis_open = self.app.state.analysis_window_open
        if not is_analysis_open:
            return

        self.analysis.destroy()
        self.app.state.analysis_window_open = False

class Data:
    def __init__(self, app):
        self.app = app

        try:
            # Try creating connection with DESCRIPTIVE database
            pass

            self.descriptive_connection = 0
            self.descriptive_cursor = 0
            self.app.state.descriptive_opened = True
        except:
            # Show dialogue that an error has occured

            pass

        try:
            # Try creating connection with INTERNAL database
            pass

            self.purchases_connection = 0
            self.purchases_cursor = 0
            self.app.state.internal_opened = True
        except:
            # Show dialogue that an error has occured
            pass

        # Caches all descriptive data
        self.update_descriptive_data()

    def pick_purchases_database(self):
        database_filetypes = (("Microsoft Access Database", ".accdb"), ("Microsoft Access Database Legacy", ".mdb"))
        some_string = askopenfilename(filetypes=database_filetypes)

        # Get full path of internal database
        # Try forming connection
        # Check if it contains valid columns
        # Store connection

        self.app.state.purchases_database = some_string
        print(self.app.state.purchases_database)

    def update_descriptive_data(self):
        self.get_category_entries()
        self.get_product_type_entries()
        self.get_product_brand_entries()

    def get_category_entries(self):
        self.descriptive_cursor.execute(f"SELECT * FROM Category ORDER BY CategoryName")
        category_entries = self.descriptive_cursor.fetchall()
        self.all_categories = [ category_entry[0] for category_entry in category_entries ]
        return self.all_categories

    def get_product_type_entries(self):
        self.descriptive_connection.execute(f"SELECT * FROM ProductTypes")
        product_type_entries = self.descriptive_cursor.fetchall()
        self.all_product_types = [ product_type_entry[0] for product_type_entry in product_type_entries ]
        return self.all_product_types

    def get_product_brand_entries(self):
        self.descriptive_connection.execute(f"SELECT * FROM Products")
        product_brand_entries = self.descriptive_cursor.fetchall()
        self.all_product_brands = [ product_entry[0] for product_entry in product_brand_entries ]
        return self.all_product_brands

    def get_month_year_purchases(self, month, year):
        self.purchases_cursor.execute(f"SELECT * FROM Purchases WHERE PurchaseMonth='{month}' AND PurchaseYear={year}")
        data = self.purchases_cursor.fetchall()
        print(data, "\t Purchase Table Entries")

        return data
    
    def get_purchase_dates(self):
        self.purchases_cursor.execute(f"SELECT PurchaseYear, PurchaseMonth FROM Purchases ORDER BY PurchaseYear DESC, PurchaseMonth DESC")
        entries = self.purchases_cursor.fetchall()
        months = []
        years = []

        for purchase_month, purchase_year in entries:
            if not purchase_month in months:
                months.append(purchase_month)
            if not purchase_year in years:
                years.append(purchase_year)

        dates = [ (f"{month} {year}" for month in months) for year in years ]
        return dates
    
    def delete_purchase_by_id(self, id):
        self.purchases_cursor.execute(f"DELETE FROM Purchases WHERE PurchaseID = {id}")
        self.purchases_cursor.commit()

    def create_purchase_entry(self, purchase_year, purchase_month, product_id, unit_amount):
        self.purchases_cursor.execute(
            f"INSERT INTO Purchases(PurchaseYear, PurchaseMonth, ProductID, UnitAmount) VALUES"
            f"({purchase_year}, '{purchase_month}', {product_id}, {unit_amount})"
        )
        self.purchases_cursor.commit()

    def update_purchase_entry(self, purchase_id, purchase_year, purchase_month, product_id, unit_amount):
        self.purchases_cursor.execute(
            f"UPDATE Purchases SET PurchaseYear = {purchase_year}, PurchaseMonth = '{purchase_month}', ProductID = {product_id}, UnitAmount = {unit_amount} WHERE PurchaseID = {purchase_id}"
        )
        self.purchases_cursor.commit()
    
    def get_product_brand_from_id(self, id):
        for product_brand_entry in self.all_product_brands:
            if product_brand_entry[0] == id:
                return product_brand_entry
            
    def get_product_type_from_id(self, id):
        for product_type_entry in self.all_product_types:
            if product_type_entry[0] == id:
                return product_type_entry

    def get_product_brands_from_category(self, category):
        category_product_type_ids = [
            product_type_entry[0] for product_type_entry in self.all_product_types if product_type_entry[1] == category
        ]

        category_product_brands = [
            product_brand_entry for product_brand_entry in self.all_product_brands if product_brand_entry[2] in category_product_type_ids
        ]

        return category_product_brands

class Application:
    def __init__(self):
        self.state = ApplicationState()
        self.data = Data(app=self)
        self.windows = Windows(app=self)
        self.windows.create_main()

    def mainloop(self):
        if not self.state.descriptive_opened or not self.state.purchases_opened:
            return

        return self.windows.main.mainloop()