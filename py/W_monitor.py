import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import GlobalStates
import PlotItems

class W_MonitorWindow:
    def __init__(self, underlying_window, root, _plot_type, _host):
        self.plot_type = _plot_type
        self.root_module = root
        self.window = underlying_window
        self.appearance_hanlder = None
        self.figure = None
        self.axis = None
        self.init_data()
        self.init_config()
        self.root_module.protocol("WM_DELETE_WINDOW", self.on_close)
        self.host = _host
        self.initialize_figure()
        self.plot_item = None
        self.set_plot_item()

    def set_plot_item(self):
        if self.plot_type == "time_series":
            self.plot_item = PlotItems.PlotCurveTimeSeries()

    def init_data(self):
        self.id = 0
        self.figure_magnification_factor = 1.2

    def recieve_data(self, data):
        self.plot_item.recieve_new_data(data)
        self.plot_item.show_on_figure(self.figure, self.axis)
        if not self.plot_item.get_if_using_user_axis_limits():
            self.plot_item.auto_set_axis_bouds(self.figure, self.axis)

    def init_config(self):
        self.window.placeholder_canvas.configure(background="#212121")
        self.window.placeholder_canvas.configure(highlightbackground="#212121")
        self.window.placeholder_canvas.configure(selectbackground="#212121")

    def initialize_figure(self):
        self.root_module.update()
        self.figure = Figure(figsize=(17, 6), dpi=100)
        self.axis = self.figure.add_subplot(111)
        canvas = FigureCanvasTkAgg(self.figure, self.root_module)
        self.appearance_hanlder = GlobalStates.PlotAppearance(self.figure, self.axis, canvas)
        x_root = self.window.placeholder_canvas.winfo_x()
        y_root = self.window.placeholder_canvas.winfo_y()
        width_root = self.window.placeholder_canvas.winfo_width()
        height_root = self.window.placeholder_canvas.winfo_height()
        x_center = x_root + 0.5*width_root
        y_center = y_root + 0.5*height_root
        x_new = x_center - 0.5*width_root*self.figure_magnification_factor
        y_new = y_center - 0.5*height_root*self.figure_magnification_factor
        width_new = width_root*self.figure_magnification_factor
        height_new = height_root*self.figure_magnification_factor
        canvas.get_tk_widget().place(x=x_new, y=y_new, width=width_new, height=height_new)

    def on_close(self):
        if not self.host.closing:
            self.host.reduce_monitors()
            self.root_module.destroy()
