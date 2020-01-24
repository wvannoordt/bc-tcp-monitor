from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import math

class PlotViewable(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def recieve_new_data(self, data_in):
        pass

    @abstractmethod
    def depends_on(self, data_in):
        pass

    @abstractmethod
    def show_on_figure(self, figure):
        pass

    @abstractmethod
    def set_log_scale(self, _x_is_log, _y_is_log, _z_is_log):
        pass

class PlotCurveTimeSeries(PlotViewable):
    def __init__(self):
        self.all_x_datas = []
        self.all_y_datas = []
        self.data_name = None
        self.is_initialized = False
        self.series_count = 0
        self.max_time_history = 1000
        self.x_is_log = False
        self.y_is_log = False
        self.z_is_log = False

    def set_log_scale(self, _x_is_log, _y_is_log, _z_is_log):
        self.x_is_log = _x_is_log
        self.y_is_log = _y_is_log
        self.z_is_log = _z_is_log

    def recieve_new_data(self, data_in):
        if self.depends_on(data_in) or not self.is_initialized:
            if not self.is_initialized:
                self.initialize_using_data(data_in)
            else:
                for i in range(self.series_count):
                    #TEMPORARY
                    self.all_y_datas[i].append(math.log(data_in.data[i]))
                    #self.all_y_datas[i].append(data_in.data[i])
                    if len(self.all_x_datas[i]) <= self.max_time_history:
                        self.all_x_datas[i].append(len(self.all_x_datas[i])+1)
                    if len(self.all_y_datas[i]) > self.max_time_history:
                        self.all_y_datas[i].pop(0)

    def initialize_using_data(self, data_in):
        self.series_count = data_in.total_dim
        self.data_name = data_in.name
        for i in range(self.series_count):
            self.all_y_datas.append([])
            self.all_y_datas[i].append(data_in.data[i])
            self.all_x_datas.append([])
            self.all_x_datas[i].append(1)
        self.is_initialized = True

    def show_on_figure(self, figure, axis):
        axis.set_xlim(0, 1000)
        axis.set_ylim(-5, 10)
        for i in range(len(self.all_x_datas)):
            cur_line = axis.plot(self.all_x_datas[i],self.all_y_datas[i])
        figure.canvas.draw_idle()

    def depends_on(self, data_in):
        return data_in.name == self.data_name
