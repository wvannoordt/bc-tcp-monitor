import new_connection
import GlobalStates
import tkinter as tk
import W_new_connection
import os
import bitcartinterlib
import Concurrent

class W_TcpMonitorHub:
    def __init__(self, underlying_window, root):
        self.root_module = root
        self.window = underlying_window
        self.init_data()
        self.init_config()
        self.data_stream_handler = Concurrent.ConcurrentDataHandler(self)
        self.sentinel_thread_run()
        self.root_module.protocol("WM_DELETE_WINDOW", self.close_concurrent)

    def close_concurrent(self):
        self.disconnect()
        self.root_module.destroy()

    def sentinel_thread_run(self):
        if self.has_valid_connection:
            self.data_stream_handler.on_tick()
        self.root_module.after(1, self.sentinel_thread_run)

    def init_data(self):
        self.connection_settings = GlobalStates.GlobalConnectionSettings()
        self.assets = GlobalStates.GlobalInstanceAssets()
        self.buffer_object_display_list = []
        self.has_valid_connection = False

    def init_config(self):
        absdir = os.path.dirname(os.path.realpath(__file__))

        self.assets.set_image(self.window.open_connection_button, 'add')

        self.window.open_connection_button.configure(command=self.user_set_global_connection)

    def user_set_global_connection(self):
        new_root = tk.Toplevel(self.root_module)
        new_window = new_connection.NewConnectionWindow(new_root)
        new_window_worker = W_new_connection.W_NewConnectionWindow(new_window, new_root, self.connection_settings, self.assets, self)

    def try_connect(self, candidate_connection_settings):
        if bitcartinterlib.SetConnectionAsync(candidate_connection_settings.ip_addr, candidate_connection_settings.port_number, candidate_connection_settings.buffer_size):
            self.connection_settings = candidate_connection_settings
            self.has_valid_connection = True
            return True
        else:
            return False

    def disconnect(self):
        self.data_stream_handler.block_from_callback = True
        self.has_valid_connection = False
        bitcartinterlib.CloseConnection()
        self.data_stream_handler.block_from_callback = False
