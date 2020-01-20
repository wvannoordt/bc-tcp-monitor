import bitcartinterlib
class ConcurrentDataHandler:
    def __init__(self, _host):
        self.host = _host

    def on_tick(self):
        data_in = bitcartinterlib.ReceiveObject()
        if data_in is not None:
            print(data_in)
        else:
            self.host.has_valid_connection = False
