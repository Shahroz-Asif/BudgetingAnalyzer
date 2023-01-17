import customtkinter
import matplotlib

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from ui.config import frames, labels, buttons

class ResultFrame(customtkinter.CTkFrame):
    def __init__(self, *args, app, **kwargs):
        super().__init__(*args, **kwargs)

        self.app = app

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=2)
        self.grid_rowconfigure(4, weight=4)

        self.replying_label = customtkinter.CTkLabel(master=self, **labels["replying"]["design"])
        self.replying_label.grid(**labels["replying"]["placement"])

        self.summary_category_label = customtkinter.CTkLabel(master=self, **labels["summary_category"]["design"])
        self.summary_category_label.grid(**labels["summary_category"]["placement"])

        self.summary_differences_label = customtkinter.CTkLabel(master=self, **labels["summary_differences"]["design"])
        self.summary_differences_label.grid(**labels["summary_differences"]["placement"])

        self.summary_category_frame = customtkinter.CTkFrame(master=self, **frames["summary_category"]["design"])
        self.summary_category_frame.grid(**frames["summary_category"]["placement"])

        self.summary_category_container = customtkinter.CTkFrame(master=self.summary_category_frame)
        self.summary_category_container.grid()

        summary_category_figure = Figure(figsize=(12, 10.5), dpi=18)
        summary_category_plots = summary_category_figure.add_subplot(111)
        summary_category_data = [ i ** 2 for i in range(13) ]
        summary_category_plots.plot(summary_category_data)

        summary_category_canvas = FigureCanvasTkAgg(summary_category_figure, master=self.summary_category_container)
        summary_category_canvas.draw()

        summary_category_toolbar = NavigationToolbar2Tk(summary_category_canvas, self.summary_category_container)
        summary_category_toolbar.update()
        
        self.summary_category_graph = summary_category_canvas.get_tk_widget()
        self.summary_category_graph.pack()

        self.summary_category_toolbar = summary_category_canvas.get_tk_widget()
        self.summary_category_toolbar.pack()

        self.summary_differences_frame = customtkinter.CTkFrame(master=self, **frames["summary_differences"]["design"])
        self.summary_differences_frame.grid(**frames["summary_differences"]["placement"])

        self.summary_differences_container = customtkinter.CTkFrame(master=self.summary_differences_frame)
        self.summary_differences_container.grid()

        summary_differences_figure = Figure(figsize=(12, 10.5), dpi=18)
        summary_differences_plots = summary_differences_figure.add_subplot(111)
        summary_differences_data = [ i ** 2 for i in range(13) ]
        summary_differences_plots.plot(summary_differences_data)

        summary_differences_canvas = FigureCanvasTkAgg(summary_differences_figure, master=self.summary_differences_container)
        summary_differences_canvas.draw()

        summary_differences_toolbar = NavigationToolbar2Tk(summary_differences_canvas, self.summary_differences_container)
        summary_differences_toolbar.update()
        
        self.summary_differences_graph = summary_differences_canvas.get_tk_widget()
        self.summary_differences_graph.pack()

        self.summary_differences_toolbar = summary_differences_canvas.get_tk_widget()
        self.summary_differences_toolbar.pack()

        self.separator_frame = customtkinter.CTkFrame(master=self, **frames["separator"]["design"])
        self.separator_frame.grid(row=3, columnspan=2, **frames["separator"]["placement"])

        self.analysis_button = customtkinter.CTkButton(
            master=self,
            command=app.windows.open_analysis,
            **buttons["analysis"]["design"]
        )
        self.analysis_button.grid(**buttons["analysis"]["placement"])

        self.download_button = customtkinter.CTkButton(master=self, **buttons["download"]["design"])
        self.download_button.grid(**buttons["download"]["placement"])
