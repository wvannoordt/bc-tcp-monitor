import new_connection
import GlobalStates
import tkinter as tk
import W_new_connection
import os
import bitcartinterlib
import Concurrent
import monitor
import W_monitor

class W_TcpMonitorHub:
    def __init__(self, underlying_window, root):
        self.root_module = root
        self.window = underlying_window
        self.init_data()
        self.init_config()
        self.data_stream_handler = Concurrent.ConcurrentDataHandler(self)
        self.sentinel_thread_run()
        self.root_module.protocol("WM_DELETE_WINDOW", self.close_concurrent)
        self.display_state = GlobalStates.DataDisplayState()

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
        self.has_valid_connection = False
        self.open_monitors = {}

    def init_config(self):
        absdir = os.path.dirname(os.path.realpath(__file__))

        self.assets.set_image(self.window.open_connection_button, 'add')
        self.window.open_connection_button.configure(command=self.user_set_global_connection)
        self.assets.set_image(self.window.monitor_time_history_button, "time_series")
        self.window.monitor_time_history_button.configure(command=lambda plot_type="time_series": self.create_motitor(plot_type))
        self.assets.set_image(self.window.monitor_profile_button, "profile")
        self.window.monitor_profile_button.configure(command=lambda plot_type="profile": self.create_motitor(plot_type))

    def create_motitor(self, _plot_type):
        if self.has_valid_connection:
            target_title = self.window.monitor_list_box.get(tk.ACTIVE)
            if target_title not in self.open_monitors:
                new_root = tk.Toplevel(self.root_module)
                monitor_window = monitor.MonitorWindow(new_root)
                monitor_worker = W_monitor.W_MonitorWindow(monitor_window, new_root, _plot_type, self)
                monitor_worker.id = hash(monitor_worker)
                monitor_worker.data_title = target_title
                self.open_monitors[target_title] = monitor_worker

    def user_set_global_connection(self):
        new_root = tk.Toplevel(self.root_module)
        new_window = new_connection.NewConnectionWindow(new_root)
        new_window_worker = W_new_connection.W_NewConnectionWindow(new_window, new_root, self.connection_settings, self.assets, self)

    def try_connect(self, candidate_connection_settings):
        if bitcartinterlib.SetConnectionAsync(candidate_connection_settings.ip_addr, candidate_connection_settings.port_number, candidate_connection_settings.buffer_size):
            self.connection_settings = candidate_connection_settings
            self.has_valid_connection = True
            self.assets.set_image(self.window.open_connection_button, 'close')
            self.window.open_connection_button.configure(command=self.disconnect)
            return True
        else:
            return False

    def disconnect(self):
        if self.has_valid_connection:
            self.data_stream_handler.block_from_callback = True
            self.has_valid_connection = False
            bitcartinterlib.CloseConnection()
            self.data_stream_handler.block_from_callback = False
            self.window.monitor_list_box.delete(0, tk.END)
            self.assets.set_image(self.window.open_connection_button, 'add')
            self.window.open_connection_button.configure(command=self.user_set_global_connection)
        self.update_info()

    def update_info(self):
        if self.has_valid_connection:
            self.window.ip_addr_label.configure(text=("IP: " + self.connection_settings.ip_addr))
            self.window.port_label.configure(text=("Port: " + str(self.connection_settings.port_number)))
            self.window.transfer_rate_label.configure(text=("Transfer rate: " + "{:7.2f}".format(self.display_state.data_transfer_rate) + " (Kb/s)"))
        else:
            self.window.ip_addr_label.configure(text="IP: ")
            self.window.port_label.configure(text="Port: " )
            self.window.transfer_rate_label.configure(text="Transfer rate: ")

    def receive_data(self, input_data):
        self.display_state.process_new_data(input_data, self.window.monitor_list_box)
        self.update_info()
