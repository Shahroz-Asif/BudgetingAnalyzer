import customtkinter
import matplotlib

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from ui.config import frames

class GraphComponent(customtkinter.CTkFrame):
    def __init__(self, *args, app, **kwargs):
        super().__init__(*args, **kwargs)

        self.app = app

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.graph_frame = customtkinter.CTkFrame(master=self, **frames["summary_differences"]["design"])
        self.graph_frame.grid(row=0, column=0, **frames["summary_differences"]["placement"])

        graph_figure = Figure(figsize=(12, 11), dpi=18)
        graph_plots = graph_figure.add_subplot(111)
        graph_data = [ i ** 2 for i in range(13) ]
        graph_plots.plot(graph_data)

        graph_canvas = FigureCanvasTkAgg(graph_figure, master=self.graph_frame)
        graph_canvas.draw()

        graph_toolbar = NavigationToolbar2Tk(graph_canvas, self.graph_frame)
        graph_toolbar.update()
        
        self.graph_widget = graph_canvas.get_tk_widget()
        self.graph_widget.pack()

        self.graph_toolbar = graph_canvas.get_tk_widget()
        self.graph_toolbar.pack()

        self.grid(row=0, column=0, sticky="wnes")