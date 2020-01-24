import bitcartinterlib
class TransmittedDataObject:
    def __init__(self, data_in):
        self.name = data_in[0]
        self.byte_count = data_in[1]
        self.dims = data_in[2]
        self.dim_1 = self.dims[0]
        self.dim_2 = self.dims[1]
        self.dim_3 = self.dims[2]
        self.total_dim = self.dim_1*self.dim_2*self.dim_3
        self.data = data_in[3]

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
                    data_obj = TransmittedDataObject(data_in)
                    self.host.receive_data(data_obj)
