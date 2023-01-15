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
    purchases_database = "INTERNAL.accdb"

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

    def pick_purchases_database(self):
        database_filetypes = (("Microsoft Access Database", ".accdb"), ("Microsoft Access Database Legacy", ".mdb"))
        some_string = askopenfilename(filetypes=database_filetypes)

        # Try forming connection
        # Check if it contains valid columns
        # Store connection

        self.app.state.purchases_database = some_string
        print(self.app.state.purchases_database)

class Application:
    def __init__(self):
        self.state = ApplicationState()
        self.data = Data(app=self)
        self.windows = Windows(app=self)
        self.windows.create_main()

    def mainloop(self):
        return self.windows.main.mainloop()