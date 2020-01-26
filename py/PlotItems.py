from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import math

class PlotViewable(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_if_using_user_axis_limits(self):
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

    @abstractmethod
    def auto_set_axis_bouds(self, figure, axis):
        pass

class PlotCurveTimeSeries(PlotViewable):
    def __init__(self):
        self.all_x_datas = []
        self.all_y_datas = []
        self.line_objects = []
        self.data_name = None
        self.is_initialized = False
        self.series_count = 0
        self.max_time_history = 1000
        self.x_is_log = False
        #temporary
        self.y_is_log = True
        self.z_is_log = False
        self.using_user_defined_limits = False
        self.axis_inflation = 1.25
        self.first_plot = True

    def get_if_using_user_axis_limits(self):
        return self.using_user_defined_limits

    def auto_set_axis_bouds(self, figure, axis):
        xmin = math.inf
        xmax = -math.inf
        ymin = math.inf
        ymax = -math.inf
        for i in range(len(self.all_x_datas)):
            xmin = min([xmin, min(self.all_x_datas[i])])
            xmax = max([xmax, max(self.all_x_datas[i])])
            ymin = min([ymin, min(self.all_y_datas[i])])
            ymax = max([ymax, max(self.all_y_datas[i])])
        if xmin == xmax:
            xmin = xmax - 1
        if ymin == ymax:
            ymin = ymax - 1
        delta_y = (ymax-ymin)*0.5
        y_mean = (ymax+ymin)*0.5
        axis.set_xlim(xmin, xmax)
        axis.set_ylim(y_mean - self.axis_inflation*delta_y, y_mean + self.axis_inflation*delta_y)

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
                    if self.y_is_log:
                        self.all_y_datas[i].append(math.log10(data_in.data[i]))
                    else:
                        self.all_y_datas[i].append(data_in.data[i])
                    if len(self.all_x_datas[i]) <= self.max_time_history:
                        self.all_x_datas[i].append(len(self.all_x_datas[i])+1)
                    if len(self.all_y_datas[i]) > self.max_time_history:
                        self.all_y_datas[i].pop(0)

    def initialize_using_data(self, data_in):
        self.series_count = data_in.total_dim
        self.data_name = data_in.name
        for i in range(self.series_count):
            self.all_y_datas.append([])
            self.all_x_datas.append([])
            for k in range(self.max_time_history):
                if self.y_is_log:
                    self.all_y_datas[i].append(math.log10(data_in.data[i]))
                else:
                    self.all_y_datas[i].append(data_in.data[i])
                self.all_x_datas[i].append(1)
        self.is_initialized = True

    def show_on_figure(self, figure, axis):
        if self.first_plot:
            for i in range(len(self.all_x_datas)):
                cur_line, = axis.plot(self.all_x_datas[i],self.all_y_datas[i])
                self.line_objects.append(cur_line)
            figure.canvas.draw_idle()
            print("first done")
            self.first_plot = False
        else:
            for i in range(len(self.all_x_datas)):
                print("{}, {}".format(len(self.all_x_datas[i])), len(self.all_y_datas[i]))
                cur_line = self.line_objects[i]
                cur_line.set_ydata(self.all_y_datas[i])
                cur_line.set_xdata(self.all_x_datas[i])
        figure.canvas.draw()
        figure.canvas.flush_events()


    def depends_on(self, data_in):
        return data_in.name == self.data_name
