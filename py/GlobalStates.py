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
        'time_series' : tk.PhotoImage(file=os.path.join(absdir, "../assets/time_series_large.png")),
        'profile' : tk.PhotoImage(file=os.path.join(absdir, "../assets/profile_large.png")),
        }

    def set_image(self, widget, image_key):
        widget.configure(image=self.images[image_key])

class DataDisplayState:
    def __init__(self):
        self.display_data_by_name = {}
        self.sample_max_count = 20
        self.delta_t_values = []
        self.data_trans_values = []
        self.data_transfer_rate = 0

    def compute_data_transfer_rate(self):
        numerator = 0
        denominator = 0
        for i in range(len(self.delta_t_values)):
            numerator = numerator + self.delta_t_values[i]*self.data_trans_values[i]
            denominator = denominator + self.delta_t_values[i]
        self.data_transfer_rate = numerator / (1024*denominator)

    def process_new_data(self, input_data, list_box_display):
        name = input_data[0]
        num_bytes = input_data[1]
        if name in self.display_data_by_name:
            data_tuple = self.display_data_by_name[name]
            try:
                previous_time = data_tuple[0]
            except:
                previous_time = data_tuple
            current_time = time.time()
            self.display_data_by_name[name] = (current_time, "junk_value")
            delta_t = current_time - previous_time
            self.delta_t_values.append(delta_t)
            self.data_trans_values.append(num_bytes)
            if len(self.delta_t_values) > self.sample_max_count:
                self.delta_t_values.pop(0)
                self.data_trans_values.pop(0)
            self.compute_data_transfer_rate()
        if name not in self.display_data_by_name:
            self.display_data_by_name[name] = (time.time())
            list_box_display.insert(tk.END, name)
