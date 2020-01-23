import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class W_MonitorWindow:
    def __init__(self, underlying_window, root, _plot_type, _host):
        self.plot_type = _plot_type
        self.root_module = root
        self.window = underlying_window
        self.init_data()
        self.init_config()
        self.root_module.protocol("WM_DELETE_WINDOW", self.on_close)
        self.host = _host

    def init_data(self):
        self.id = 0
        self.data_title = None
        self.figure_magnification_factor = 1.2

    def init_config(self):
        self.window.placeholder_canvas.configure(background="#212121")
        self.window.placeholder_canvas.configure(highlightbackground="#212121")
        self.window.placeholder_canvas.configure(selectbackground="#212121")

    def initialize_figure(self):
        self.root_module.update()
        fig = Figure(figsize=(17, 6), dpi=100)
        a = fig.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        canvas = FigureCanvasTkAgg(fig, self.root_module)
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
        fig.patch.set_facecolor('#212121')
        a.set_facecolor('#191919')
        a.spines['bottom'].set_color('#dddddd')
        a.spines['top'].set_color('#dddddd')
        a.spines['right'].set_color('#dddddd')
        a.spines['left'].set_color('#dddddd')
        a.xaxis.label.set_color('#dddddd')
        a.tick_params(axis='x', colors='#dddddd')
        a.yaxis.label.set_color('#dddddd')
        a.tick_params(axis='y', colors='#dddddd')
        canvas.get_tk_widget().place(x=x_new, y=y_new, width=width_new, height=height_new)

    def on_close(self):
        self.host.open_monitors.pop(self.data_title)
        self.root_module.destroy()
