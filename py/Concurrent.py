import bitcartinterlib
class ConcurrentDataHandler:
    def __init__(self, _host):
        self.host = _host

    def on_tick(self):
        if self.host.has_valid_connection:
            data_in = bitcartinterlib.ReceiveObjectAsync()
            if not (data_in == "NODATA"):
                print(data_in)
            elif data_in is None:
                self.host.disconnect()
                print(data_in)
