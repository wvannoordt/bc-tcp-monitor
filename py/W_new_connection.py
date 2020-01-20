import GlobalStates
from tkinter import messagebox
import tkinter as tk
import os


class W_NewConnectionWindow:
    def __init__(self, underlying_window, root, connection_settings, _assets, _host_worker):
        self.root_module = root
        self.window = underlying_window
        self.current_connection_settings = connection_settings
        self.assets = _assets
        self.host_worker = _host_worker
        self.init_data()
        self.init_config()

    def init_data(self):
        self.most_recent_error = "No recent error."

    def init_config(self):
        self.import_connection_settings(self.current_connection_settings)
        self.window.accept_button.configure(command=self.on_try_accept_current_connection_settings)

        absdir = os.path.dirname(os.path.realpath(__file__))

        self.assets.set_image(self.window.file_input_button, 'file')
        self.assets.set_image(self.window.accept_button, 'accept')
        self.assets.set_image(self.window.file_detect_button, 'seek')

    def import_connection_settings(self, connection_settings):
        self.window.ip_addr_entry.delete(0, tk.END)
        self.window.port_number_entry.delete(0, tk.END)
        self.window.buffer_size_entry.delete(0, tk.END)

        self.window.ip_addr_entry.insert(0, connection_settings.ip_addr)
        self.window.port_number_entry.insert(0, connection_settings.port_number)
        self.window.buffer_size_entry.insert(0, connection_settings.buffer_size)

    def on_try_accept_current_connection_settings(self):
        candidate_new_settings = self.try_parse_connection_settings()
        if not (candidate_new_settings is None):
            if self.host_worker.try_connect(candidate_new_settings):
                self.root_module.destroy()
            else:
                self.most_recent_error = "Connection could not be activated for these settings. A simulation may not be running on this port."
                self.show_error()
        else:
            self.show_error()

    def show_error(self):
            messagebox.showinfo("Error!", self.most_recent_error)

    def try_parse_connection_settings(self):
        candidate_ip = self.window.ip_addr_entry.get()
        candidate_port = -1
        candidate_buf = -1
        try:
            candidate_port = int(self.window.port_number_entry.get())
        except Exception:
            self.most_recent_error = "Bad port number."
            return None
        try:
            candidate_buf = int(self.window.buffer_size_entry.get())
        except Exception:
            self.most_recent_error = "Bad buffer size."
            return None
        if candidate_port <= 1024 or candidate_buf <= 0 or candidate_port > 9999 or candidate_buf > 8192:
            self.most_recent_error = "Port out of range [1025-9999] or buffer size out of range [0-8192]."
            return None
        return GlobalStates.GlobalConnectionSettings(candidate_ip, candidate_port, candidate_buf)
