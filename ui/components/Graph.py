import numpy
import customtkinter
import matplotlib

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from ui.config import frames

def generate_smoothened_points(points, degree):
    smoothened_points = []
    for i in range(len(points) - 1):
        prev_point = points[i - 1]
        curr_a_point = points[i]
        curr_b_point = points[(i + 1) % len(points)]
        next_point = points[(i + 2) % len(points)]

        
        point_range = numpy.array([prev_point, curr_a_point, (curr_a_point[0] + 1, curr_b_point[1]), (curr_a_point[0] + 2, next_point[1])])
        point_x = point_range[:,0]
        point_y = point_range[:,1]

        smoothing_eq = numpy.poly1d(numpy.polyfit(point_x, point_y, degree))
        smooth_x = numpy.linspace(curr_a_point[0], curr_b_point[0], 50)
        smooth_y = smoothing_eq(smooth_x)

        smooth_coord = [ ( smooth_x[i], smooth_y[i] ) for i in range(len(smooth_x)) ]
        smoothened_points.extend(smooth_coord)

    return smoothened_points

class GraphComponent(customtkinter.CTkFrame):
    def __init__(self, *args, app, **kwargs):
        super().__init__(*args, **kwargs)

        self.app = app

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.graph_frame = customtkinter.CTkFrame(master=self, **frames["summary_differences"]["design"])
        self.graph_frame.grid(row=0, column=0, **frames["summary_differences"]["placement"])

    def plot_figure(self, given_points):
        try:
            self.graph_widget.pack_forget()
            self.graph_toolbar.pack_forget()
        except:
            pass

        
        graph_figure = Figure(figsize=(12, 11), dpi=18)
        graph_plots = graph_figure.add_subplot(111)

        smoothened_points = numpy.array(generate_smoothened_points(given_points, 7))
        x_points = smoothened_points[:,0]
        y_points = smoothened_points[:,1]
        
        graph_plots.plot(x_points, y_points)

        graph_canvas = FigureCanvasTkAgg(graph_figure, master=self.graph_frame)
        graph_canvas.draw()

        graph_toolbar = NavigationToolbar2Tk(graph_canvas, self.graph_frame)
        graph_toolbar.update()
        
        self.graph_widget = graph_canvas.get_tk_widget()
        self.graph_widget.pack()

        self.graph_toolbar = graph_canvas.get_tk_widget()
        self.graph_toolbar.pack()

        self.grid(row=0, column=0, sticky="wnes")

    def plot_pie(self, labels, sizes):
        try:
            self.graph_widget.pack_forget()
            self.graph_toolbar.pack_forget()
        except:
            pass

        graph_figure = Figure(figsize=(12, 11), dpi=18)
        graph_axis = graph_figure.add_subplot(111)
        graph_axis.pie(sizes, labels=labels, radius=1)

        graph_canvas = FigureCanvasTkAgg(graph_figure, master=self.graph_frame)
        graph_canvas.draw()

        graph_toolbar = NavigationToolbar2Tk(graph_canvas, self.graph_frame)
        graph_toolbar.update()
        
        self.graph_widget = graph_canvas.get_tk_widget()
        self.graph_widget.pack()

        self.graph_toolbar = graph_canvas.get_tk_widget()
        self.graph_toolbar.pack()

        self.grid(row=0, column=0, sticky="wnes")

    def plot_bar(self, labels, sizes):
        try:
            self.graph_widget.pack_forget()
            self.graph_toolbar.pack_forget()
        except:
            pass

        graph_figure = Figure(figsize=(12, 11), dpi=18)
        graph_axis = graph_figure.add_subplot(111)
        graph_axis.bar(labels, sizes)

        graph_canvas = FigureCanvasTkAgg(graph_figure, master=self.graph_frame)
        graph_canvas.draw()

        graph_toolbar = NavigationToolbar2Tk(graph_canvas, self.graph_frame)
        graph_toolbar.update()
        
        self.graph_widget = graph_canvas.get_tk_widget()
        self.graph_widget.pack()

        self.graph_toolbar = graph_canvas.get_tk_widget()
        self.graph_toolbar.pack()

        self.grid(row=0, column=0, sticky="wnes")