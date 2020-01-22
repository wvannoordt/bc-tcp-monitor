import bitcartinterlib
class ConcurrentDataHandler:
    def __init__(self, _host):
        self.host = _host
        self.tries = 0
        self.try_max = 150
        self.count  = 0
        self.block_from_callback = False

    def on_tick(self):
        if self.host.has_valid_connection:
            data_in = bitcartinterlib.ReceiveObjectAsync()
            if data_in is None:
                if self.tries > self.try_max:
                    if (not self.block_from_callback):
                        self.host.disconnect()
                    self.tries = 0
                else:
                    self.tries = self.tries + 1
            else:
                if not (data_in == "NODATA"):
                    self.count = self.count + 1
                    self.host.receive_data(data_in)
