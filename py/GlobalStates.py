import os
import tkinter as tk
import time



class GlobalConnectionSettings:
    def __init__(self, _ip_addr="127.0.0.1", _port_number = 8111, _buffer_size = 4096):
        self.port_number =_port_number
        self.buffer_size = _buffer_size
        self.ip_addr = _ip_addr

class GlobalInstanceAssets:
    def __init__(self):
        absdir = os.path.dirname(os.path.realpath(__file__))
        self.images = {
        'accept' : tk.PhotoImage(file=os.path.join(absdir, "../assets/accept_aa.png")),
        'add' : tk.PhotoImage(file=os.path.join(absdir, "../assets/add_aa.png")),
        'close' : tk.PhotoImage(file=os.path.join(absdir, "../assets/close_aa.png")),
        'file' : tk.PhotoImage(file=os.path.join(absdir, "../assets/file_aa.png")),
        'seek' : tk.PhotoImage(file=os.path.join(absdir, "../assets/seek_aa.png")),
        'time_series' : tk.PhotoImage(file=os.path.join(absdir, "../assets/time_series_L_aa.png")),
        'profile' : tk.PhotoImage(file=os.path.join(absdir, "../assets/profile_L_aa.png")),
        }

    def set_image(self, widget, image_key):
        widget.configure(image=self.images[image_key])

class DataDisplayState:
    def __init__(self):
        self.display_data_by_name = {}
        self.sample_max_count = 20
        self.t_values = []
        self.data_trans_values = []
        self.data_transfer_rate = 0

    def compute_data_transfer_rate(self):
        numerator = 0
        denominator = 0
        for i in range(len(self.t_values)):
            numerator = numerator + self.data_trans_values[i]
        denominator = max(self.t_values[-1] - self.t_values[0], 1e-5)
        self.data_transfer_rate = numerator / (1024*denominator)

    def process_new_data(self, input_data, list_box_display):
        name = input_data.name
        num_bytes = input_data.byte_count
        if input_data.name in self.display_data_by_name:
            data_tuple = self.display_data_by_name[name]
            try:
                previous_time = data_tuple[0]
            except:
                previous_time = data_tuple
            current_time = time.time()
            self.display_data_by_name[name] = (current_time, None)
            delta_t = current_time - previous_time
            self.t_values.append(current_time)
            self.data_trans_values.append(num_bytes)
            if len(self.t_values) > self.sample_max_count:
                self.t_values.pop(0)
                self.data_trans_values.pop(0)
            self.compute_data_transfer_rate()
        if name not in self.display_data_by_name:
            self.display_data_by_name[name] = (time.time(), None)
            list_box_display.insert(tk.END, name)

class PlotAppearance:
    def __init__(self, _root_figure, _root_axes, _root_canvas):
        self.root_figure = _root_figure
        self.root_axes = _root_axes
        self.root_canvas = _root_canvas
        self.delegates = {}
        self.initialize_delegates()
        self.set_defaults()

    def initialize_delegates(self):
        self.delegates['background_color'] = lambda input_value: self.root_figure.patch.set_facecolor(input_value)
        self.delegates['plot_color'] = lambda input_value: self.root_axes.set_facecolor(input_value)
        self.delegates['line_color_u'] = lambda input_value: self.root_axes.spines['top'].set_color(input_value)
        self.delegates['line_color_d'] = lambda input_value: self.root_axes.spines['bottom'].set_color(input_value)
        self.delegates['line_color_l'] = lambda input_value: self.root_axes.spines['left'].set_color(input_value)
        self.delegates['line_color_r'] = lambda input_value: self.root_axes.spines['right'].set_color(input_value)
        self.delegates['tick_color_x'] = lambda input_value: self.root_axes.tick_params(axis='x', colors=input_value)
        self.delegates['tick_color_y'] = lambda input_value: self.root_axes.tick_params(axis='y', colors=input_value)
        self.delegates['label_color_x'] = lambda input_value: self.root_axes.xaxis.label.set_color(input_value)
        self.delegates['label_color_y'] = lambda input_value: self.root_axes.yaxis.label.set_color(input_value)

    def set_property(self, prop, val):
        delegate_cur = self.delegates[prop]
        delegate_cur(val)

    def set_defaults(self):
        self.set_property('background_color', '#212121')
        self.set_property('plot_color', '#191919')
        self.set_property('line_color_u', '#dddddd')
        self.set_property('line_color_d', '#dddddd')
        self.set_property('line_color_l', '#dddddd')
        self.set_property('line_color_r', '#dddddd')
        self.set_property('tick_color_x', '#dddddd')
        self.set_property('tick_color_y', '#dddddd')
        self.set_property('label_color_x', '#dddddd')
        self.set_property('label_color_y', '#dddddd')
