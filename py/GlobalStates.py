import os
import tkinter as tk
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
        'seek' : tk.PhotoImage(file=os.path.join(absdir, "../assets/seek_aa.png"))
        }

    def set_image(self, widget, image_key):
        widget.configure(image=self.images[image_key])
