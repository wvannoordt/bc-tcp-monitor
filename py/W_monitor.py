class W_MonitorWindow:
    def __init__(self, underlying_window, root, _plot_type, _host):
        self.plot_type = _plot_type
        self.root_module = root
        self.window = underlying_window
        self.init_data()
        self.root_module.protocol("WM_DELETE_WINDOW", self.on_close)
        self.host = _host

    def init_data(self):
        self.id = 0
        self.data_title = None

    def on_close(self):
        self.host.open_monitors.pop(self.data_title)
        self.root_module.destroy()
